#!/usr/bin/env python
from sys        import argv
from requests   import get
from HTMLParser import HTMLParser

def get_href(attr_list):
  href_attribute = list(filter(lambda x: x[0] == "href", attr_list))
  if href_attribute:
    return href_attribute[0][1]
  return None

class MyHTMLParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    if tag == 'a':
      href = get_href(attrs)
      if href:
        print(href)

target = argv[1]
html   = get(target).text
parser = MyHTMLParser()

parser.feed(html)
