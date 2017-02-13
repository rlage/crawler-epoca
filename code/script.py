#coding: utf-8
#Arquivo de script com o código do crawler

import re
import mechanize
from bs4 import BeautifulSoup

class Product:
  def __init__(self, name, title, url):
    self.name = name
    self.title = title
    self.url = url

def retrieveAllCategoryUrls(url):
  """
  Essa função recebe a url principal de um site
  e retorna a lista de URLs das categorias
  """
  all_urls = []
  for link in all_menu_items:
      css_class = link.parent.get('class')[1]
      if ( css_class != 'm_marcas') and (css_class != 'solares'):
          all_urls.append(link.get('href'))       
  return all_urls

def retrieveProductsInformation(url):
  """
  Essa função recebe a url de uma categoria e retorna 
  a lista de objetos produto contendo os dados
  de cada produto
  """
  product = Product("nome", "titulo", "url")
  return (product.name, product.title, product.url)




url = 'http://www.epocacosmeticos.com.br/'
br = mechanize.Browser()
html_doc = br.open(url)
soup = BeautifulSoup(html_doc, 'html.parser')
all_menu_items = soup.find_all("a", class_="princ")
all_category_urls = retrieveAllCategoryUrls(url)

print retrieveProductsInformation(all_category_urls[0])

