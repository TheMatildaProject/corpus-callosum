import requests

def count_words_at_url(url):
    resp = requests.get(url)
    return print(resp.text.split())
    return len(resp.text.split())