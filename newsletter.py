# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual API key
NEWS_API_KEY = 'YOUR_API_KEY'
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    params = {'apiKey': NEWS_API_KEY, 'q': query}
    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()
    articles = data.get('articles', [])
    return render_template('search_results.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
