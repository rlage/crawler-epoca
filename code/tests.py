#coding: utf-8
#Arquivo de script de testes do crawler
import script
import unittest

class retrieveAllCategoryUrls(unittest.TestCase):

  def testEmpty(self):
    self.assertTrue(script.retrieveAllCategoryUrls(1))

  def testDefault(self):
    self.assertFalse(script.retrieveAllCategoryUrls())

class retrieveProductsFromCategory(unittest.TestCase):

  def testEmpty(self):
    self.assertTrue(script.retrieveProductsFromCategory(1))

  def testDefault(self):
    self.assertFalse(script.retrieveProductsFromCategory())

class retrieveProducts(unittest.TestCase):

  def testEmpty(self):
    self.assertTrue(script.retrieveProducts(1))

  def testDefault(self):
    self.assertFalse(script.retrieveProducts())

class writeInformationToCsv(unittest.TestCase):

  def testEmpty(self):
    self.assertTrue(script.writeInformationToCsv(1))

  def testDefault(self):
    self.assertFalse(script.writeInformationToCsv())

def main():
  unittest.main()

if __name__ == '__main__':
  main()