
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys
def getTitle():
    try:
        import urllib.request

        with urllib.request.urlopen('https://taipeicity.github.io/traffic_realtime/') as html:
            print(html.read(500))
    except HTTPError as e:
        print(e)
        return None

result = getTitle()
print(result)