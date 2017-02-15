#coding: utf-8
#Arquivo de script com o código do crawler

import re
import mechanize
import csv
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
  try:
    
    html_doc = br.open(url)
  
    soup = BeautifulSoup(html_doc, 'html.parser')
    menu_items = soup.find_all("a", class_="princ")
    urls = []
    for link in menu_items:
        css_class = link.parent.get('class')[1]
        if ( css_class != 'm_marcas') and (css_class != 'solares'):
            urls.append(link.get('href'))       
    return urls

  except TypeError as (e):
    print "Type error({0})".format(e)
  except Exception as (e):
    print "Unexpected error({0})".format(e)

def retrieveProductsFromCategory(url):
  """
  Essa função recebe a url de uma categoria e retorna 
  a lista de objetos produto contendo os dados
  de cada produto daquela categoria
  """
  print url
  html_doc = br.open(url)

  soup = BeautifulSoup(html_doc, 'html.parser')
  items = soup.find_all("a", class_="productImage")
  products = []

  for item in items:
    name = item.parent.get('value')
    title = item.get('title')
    url = item.get('href')
    product = Product(name, title, url)
    products.append(product)
  return (products)

def retrieveProducts(category_urls):
  """
  Recebe um array com as urls de todas as categorias
  e retorna um array com todos os produtos de todas as categorias
  """
  products = []
  
  for url in category_urls:
    products += retrieveProductsFromCategory(url)

  return products

def writeInformationToCsv(products):
  """
  Recebe um array de produtos e escreve
  nome, titulo e url em um csv
  """
  f = open('products.csv', 'w')

  for product in products:
    f.write(
      product.name.encode("utf-8") + "," + 
      product.title.encode("utf-8") + "," + 
      product.url.encode("utf-8") + "\n")

  f.close()
  print "Arquivo products.csv escrito com sucesso."

url = 'http://www.epocacosmeticos.com.br/'
br = mechanize.Browser()
category_urls = retrieveAllCategoryUrls(url)
products = retrieveProducts(category_urls)
writeInformationToCsv(products)



