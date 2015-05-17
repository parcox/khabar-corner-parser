#!/usr/bin/env python
import urllib2, sys
from bs4 import BeautifulSoup

def openurl(url):
    try:
        page = urllib2.urlopen(url).read()
    except:
        print "/!\ Error getting URL content!"
        sys.exit(1)
    return page

url = "http://www.republika.co.id"
soup = BeautifulSoup(openurl(url))
khabarc = soup.find('div', attrs={"class": "text-khabar-corner"})
print khabarc.get_text()