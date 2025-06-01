from django.shortcuts import render

from django.conf import settings
from googleapiclient.discovery import build
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
from urllib.parse import urlparse, parse_qs
import torch

# Load BERT model
model_name = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

import re

def get_video_id(url):
    # Regular expression to extract the video ID from a YouTube URL
    match = re.search(r'(?:v=|\/)([a-zA-Z0-9_-]{11})(?=&|\?|$)', url)
    if match:
        return match.group(1)
    return None


def get_comments(video_id):
    youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)
    try:
        print(f"Video ID: {video_id}")  # Debugging line to check the extracted video ID
        request = youtube.commentThreads().list(
            part="snippet", videoId=video_id,
            maxResults=100, textFormat="plainText"
        )
        response = request.execute()
        comments = [
            item['snippet']['topLevelComment']['snippet']['textDisplay']
            for item in response.get("items", [])
        ]
        return comments
    except Exception as e:
        print(f"Error fetching comments: {e}")
        return []


def analyze_sentiment(comment):
    encoded_input = tokenizer(comment, return_tensors='pt', truncation=True)
    output = model(**encoded_input)
    scores = softmax(output.logits.detach().numpy()[0])
    labels = ['Negative', 'Neutral', 'Positive']
    print(f"Comment: {comment}")  # Add this line to check the comment
    print(f"Scores: {scores}")    # Add this line to check the sentiment scores
    return labels[scores.argmax()], scores


def index(request):
    sentiment_data = None
    if request.method == 'POST':
        url = request.POST.get('video_url')
        if not url:
            return render(request, 'analyzer/index.html', {'error': "Please provide a valid YouTube URL."})

        video_id = get_video_id(url)
        print(f"Video ID: {video_id}")  # Add this line to check the videoId
        if video_id:
            comments = get_comments(video_id)
            if not comments:
                return render(request, 'analyzer/index.html', {'error': "No comments found or API error."})

            results = {"Positive": 0, "Negative": 0, "Neutral": 0}

            for comment in comments:
                label, _ = analyze_sentiment(comment)
                results[label] += 1
            total = sum(results.values())
            sentiment_data = {
                "positive": round((results["Positive"] / total) * 100, 2),
                "neutral": round((results["Neutral"] / total) * 100, 2),
                "negative": round((results["Negative"] / total) * 100, 2),
                "overall": max(results, key=results.get)
            }
        else:
            return render(request, 'analyzer/index.html', {'error': "Invalid YouTube URL."})

    return render(request, 'analyzer/index.html', {'sentiment_data': sentiment_data})


