from flask import Flask
#from newsapi import NewsApiClient

#newsapi = NewsApiClient(api_key='4a18ae97130c4a8fb1c0f78823778bf3')


app = Flask(__name__)
from app import views