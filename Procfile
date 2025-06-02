web: gunicorn youtube_sentiment.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn youtube_sentiment.wsgi
