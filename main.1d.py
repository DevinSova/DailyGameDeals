#!/usr/bin/env PYTHONIOENCODING=UTF-8 /Library/Frameworks/Python.framework/Versions/3.6/Resources/Python.app/Contents/MacOS/Python

# <bitbar.title>DailyGameDeals</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Devin Sova</bitbar.author>
# <bitbar.author.github>DevinSova</bitbar.author.github>
# <bitbar.desc>Simple Python BitBar plugin for Video Game Deals from http://dailygamedeals.com/</bitbar.desc>
# <bitbar.image>https://d30y9cdsu7xlg0.cloudfront.net/png/20362-200.png</bitbar.image>
# <bitbar.dependencies>python</bitbar.dependencies>
# <bitbar.abouturl>http://url-to-about.com/</bitbar.abouturl>

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

def print_platform(platform):
    raw_html = get_webpage("http://dailygamedeals.com/")
    html = BeautifulSoup(raw_html, "html.parser")
    h1 = html.find(id=platform)
    print("---")
    print(h1.text)
    dealTable = h1.find_next_sibling("ul")
    for a in dealTable.find_all("a"):
        print("{0} | href={1}".format(a.text, a["href"]))

def print_info():
    print("---")
    print("Deals from:")
    print("http://dailygamedeals.com/ | href=http://dailygamedeals.com/")

def log_error(e):
    print(e)

def main():
    print("DailyGameDeals") 
    print_platform("ps4")
    print_platform("xb1")
    print_platform("switch")
    print_platform("pc")
    print_info()
main()

