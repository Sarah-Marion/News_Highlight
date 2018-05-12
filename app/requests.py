import urllib.request
import json
from .models import News, Articles, Sources

# Getting the API KEY
api_key = None

# Getting the news base url
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_sources(source):
    """
    Function that receives news sources list from the News API
    """
    get_sources_url = base_url.format(source, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        Sources_results = None
        