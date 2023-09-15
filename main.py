import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt

def scrape_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []

    for article in soup.find_all('article'):
        title = article.h2.a.text
        content = article.p.text
        articles.append({'title': title, 'content': content})

    return articles

def analyze_sentiment(text):
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity
    return 'positive' if sentiment > 0 else 'negative' if sentiment < 0 else 'neutral'

news_url = 'https://example.com/news'
articles = scrape_news(news_url)

data = []
for article in articles:
    title = article['title']
    content = article['content']
    sentiment = analyze_sentiment(content)
    data.append({'Title': title, 'Sentiment': sentiment})

df = pd.DataFrame(data)
sentiment_counts = df['Sentiment'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Sentiment Distribution of News Articles')
plt.show()