from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual News API key
NEWS_API_KEY = 'fc2a6edc94fc44fdbfb7e1319643bfdf'
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'

@app.route('/')
def index():
    return render_template('newsletter.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    params = {'apiKey': NEWS_API_KEY, 'q': query}
    
    try:
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        articles = data.get('articles', [])
        return render_template('search_result.html', articles=articles)
    except requests.exceptions.RequestException as e:
        # Handle any request exceptions, such as network errors
        return render_template('error.html', error_message=str(e))

if __name__ == '__main__':
    app.run()
