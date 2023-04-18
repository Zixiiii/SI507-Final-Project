import requests
from bs4 import BeautifulSoup
import time
import json
import pandas as pd

BASE_URL = 'https://www.nba.com/players'
CACHE_FILE_NAME = 'player.json'
headers = {'User-Agent': 'UMSI 507 Course Project - Python Web Scraping','From': 'youremail@domain.com','Course-Info': 'https://www.si.umich.edu/programs/courses/507'}

def load_cache():
    try:
        cache_file = open(CACHE_FILE_NAME, 'r')
        cache_file_contents = cache_file.read()
        cache = json.loads(cache_file_contents)
        cache_file.close()
    except:
        cache = {}
    return cache


def save_cache(cache):
    cache_file = open(CACHE_FILE_NAME, 'w')
    contents_to_write = json.dumps(cache)
    cache_file.write(contents_to_write)
    cache_file.close()


def make_url_request_using_cache(url, cache):
    if (url in cache.keys()): # the url is our unique key
        print("Using cache")
        return cache[url]
    else:
        print("Fetching")
        time.sleep(1)
        response = requests.get(url, headers=headers)
        cache[url] = response.text
        save_cache(cache)
        return cache[url]

cache = load_cache()
new = make_url_request_using_cache(BASE_URL, cache)
    
    