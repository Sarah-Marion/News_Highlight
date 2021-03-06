from flask import render_template, redirect, request
from .import main
from ..requests import get_articles, get_sources

@main.route('/')
def index():
    """
    View root page function that returns index page and the various news sources
    """
    title = "Home- Welcome to the News Highlights Website"
   
    # Getting the news sources
    news_sources = get_sources('general')
    return render_template('index.html', title=title, sources=news_sources)


@main.route('/articles/<source_id>')
def articles(source_id):
    """
    View source page function that returns a source page and its data
    """
    title = f"{source_id}"
    
    articles = get_articles(source_id)
    return render_template('articles.html',title = title, articles = articles)
