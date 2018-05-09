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
    num = platform_to_number(platform)
    raw_html = get_webpage('http://dailygamedeals.com/')
    html = BeautifulSoup(raw_html, 'html.parser')
    divTag = html.find_all("div", {"class": "entry-content"})
    ulTags = divTag[0].find_all("ul")
    print(platform)
    print(ulTags[num].text)

def platform_to_number(platform):
    return {
            'PS4' : 0,
            'XBOX' : 1,
            'PC' : 2,
            'OTHER' : 3,
            }[platform]

def log_error(e):
    print(e)
