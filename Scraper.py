from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def get_webpage(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if valid_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during request to {0} : {1}'.format(url, str(e)))
        return None

def valid_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)

def parse_platform(platform):
    raw_html = get_webpage('http://dailygamedeals.com/')
    html = BeautifulSoup(raw_html, 'html.parser')
    divTag = html.find_all("div", {"class": "entry-content"})

    for tag in divTag:
        ulTags = tag.find_all("ul")
        for ul in ulTags:
            print(ul.text)

def log_error(e):
    print(e)
