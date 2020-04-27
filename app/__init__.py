from flask import Flask
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='fb20b3ee37e2452696f1a1b1724e6b2e')


app = Flask(__name__)
from app import views