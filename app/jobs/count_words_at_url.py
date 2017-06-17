import os, requests

def count_words_at_url(url):
    resp = requests.get(url)
    print(resp.text.split())

    f = open("/app/temp.txt",'w')
    f.write("heeey")
    os.fsync(f)
    f.close()

    return len(resp.text.split())