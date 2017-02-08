#coding: utf-8
#Arquivo de script com o código do crawler

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
import re
import mechanize
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
print soup.title


br = mechanize.Browser()
br.open("http://www.epocacosmeticos.com.br/")
# follow second link with element text matching regular expression
#response1 = br.follow_link(text_regex=r"cheese\s*shop", nr=1)
assert br.viewing_html()
print br.title()

def retrieveAllUrls(a):
	""" Recebe uma URL e retorna todas as URLs de produtos """
	if (a == 1):
		return True
	else:
		return False

