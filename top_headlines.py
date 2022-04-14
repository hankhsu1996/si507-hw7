import os

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Index page.

    When the user goes to the root of the website, we want to return the
    welcome message.

    """
    return '<h1>Welcome!</h1>'


@app.route('/name/<name>')
def name(name):
    """Name page.

    When the user goes to /name/<name>, we want to return a message with
    "Hello, <name>!" which is rendered by the template "name.html".

    """
    return render_template('name.html', name=name)


@app.route('/headlines/<name>')
def headlines(name):
    """Headlines page.

    When the user goes to /headlines/<name>, we want to return a message with
    "Hello <name>!" and today's New York Times Top Stories which is rendered
    by the template "headlines.html".

    """
    # Get the top headlines from the New York Times API
    # The API key is stored in an environment variable "API_KEY"
    api_key = os.environ['API_KEY']
    url = f'https://api.nytimes.com/svc/topstories/v2/home.json?api-key={api_key}'
    resp = requests.get(url)
    data = resp.json()
    headlines = data['results'][:5]
    # Only keep the 'title' field
    headlines = [{'title': h['title']} for h in headlines]
    return render_template('headlines.html', name=name, headlines=headlines)


@app.route('/link/<name>')
def link(name):
    """Headlines page with link.

    When the user goes to /link/<name>, we want to return a message with
    "Hello <name>!" and today's New York Times Top Stories which is rendered
    by the template "link.html".

    """
    # Get the top headlines from the New York Times API
    # The API key is stored in an environment variable "API_KEY"
    api_key = os.environ['API_KEY']
    url = f'https://api.nytimes.com/svc/topstories/v2/home.json?api-key={api_key}'
    resp = requests.get(url)
    data = resp.json()
    headlines = data['results'][:5]
    headlines = [{'title': h['title'], 'url': h['url']} for h in headlines]
    return render_template('link.html', name=name, headlines=headlines)


@app.route('/images/<name>')
def images(name):
    """Headlines page with images

    When the user goes to /images/<name>, we want to return a message with
    "Hello <name>!" and today's New York Times Top Stories which is rendered
    by the template "images.html".

    """
    # Get the top headlines from the New York Times API
    # The API key is stored in an environment variable "API_KEY"
    api_key = os.environ['API_KEY']
    url = f'https://api.nytimes.com/svc/topstories/v2/home.json?api-key={api_key}'
    resp = requests.get(url)
    data = resp.json()
    headlines = data['results'][:5]
    headlines = [{'title': h['title'], 'url': h['url'],
                  'thumbnail': h['multimedia'][1]['url']} for h in headlines]
    return render_template('images.html', name=name, headlines=headlines)


if __name__ == '__main__':
    app.run(debug=True)
