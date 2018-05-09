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

"""
Prints out deals for param platform in BitBar format

@param platform: name of platform
    ["ps4, "xb1", "switch", "pc"]
@return: nothing
"""

def parse_platform(platform):
    raw_html = get_webpage("http://dailygamedeals.com/")
    html = BeautifulSoup(raw_html, "html.parser")
    h1 = html.find(id=platform)
    print(h1.text)
    dealTable = h1.find_next_sibling("ul")
    for a in dealTable.find_all("a"):
        print("{0} | href={1}".format(a.text, a["href"]))

def log_error(e):
    print(e)
