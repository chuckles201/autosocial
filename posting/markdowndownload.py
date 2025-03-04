import html2text
import requests

# 1. get raw text(html) w/ request
# 2. Parse html and send to place
# 3. Return error if bad request

def create_url_markdown(url):
    response = requests.get(url)
    if response.status_code == 200:
        # write to article
        with open('posting/recources/article.txt', 'w',encoding='utf-8') as article:
            # converts to MD, wow!!!
            article.write(html2text.html2text(response.text))
        return 0
    else:
        # is an error.
        return 1

# create_url_markdown('https://www.tutorialspoint.com/python/tk_scale.htm')