# 🎥 YouTube Sentiment Analyzer

A Django-based web application that analyzes sentiments of comments on a YouTube video using modern NLP models.

---

## 📌 Overview

YouTube Sentiment Analyzer allows users to input a YouTube video URL and get an overview of public opinion based on the comments. It uses the **YouTube Data API** to fetch comments and **transformer models** to analyze sentiment as **Positive**, **Neutral**, or **Negative**.

---

## 🚀 Features

- 🔗 Enter any YouTube video URL  
- 💬 Fetch and analyze up to 100 top-level comments  
- 🧠 Perform sentiment analysis using pretrained transformer models  
- 📊 Display results as sentiment percentages and pie chart for better visualization
- 🌐 Deployable on platforms like **Render** or **Vercel**

---

## 📸 Screenshots

<img width="1470" alt="Screenshot 2025-06-03 at 4 56 47 PM" src="https://github.com/user-attachments/assets/3912badd-c0b9-4e01-b59d-2647a9d7157b" />

<img width="1470" alt="Screenshot 2025-06-03 at 4 56 55 PM" src="https://github.com/user-attachments/assets/74170eff-bda7-448b-bcfc-6be98895d944" />


---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Sentiment Model**: HuggingFace `transformers` (`cardiffnlp/twitter-roberta-base-sentiment`)
- **YouTube Data API v3**: For comment retrieval
- **Frontend**: HTML, CSS, Bootstrap
- **Deployment**: Render (can be adapted for Vercel)

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/sreemayi-25/youtube_sentiment.git
cd youtube_sentiment
````

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
# or
venv\Scripts\activate  # For Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

In your terminal or `.env` file, add:

```bash
SECRET_KEY=your_django_secret_key
DEBUG=False
YOUTUBE_API_KEY=your_youtube_api_key
```

Also update `ALLOWED_HOSTS` in `settings.py` if deploying:

```python
ALLOWED_HOSTS = ['your-subdomain.onrender.com', 'localhost']
```

---

## ▶️ Running Locally

```bash
python manage.py runserver
```

Open your browser and go to `http://127.0.0.1:8000/`

---

## 🧪 Example Input

Paste a valid YouTube video URL in the input field.
The app will:

1. Extract the video ID.
2. Fetch the top-level comments.
3. Use a transformer model to analyze each comment.
4. Return a summary of sentiment.

---

## 📝 To-Do

* Improve memory optimization for deployment
* Implement user login and comment history

---
