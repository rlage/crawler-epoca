#coding: utf-8
#Arquivo de script de testes do crawler
import script
import unittest

class retrieveAllUrls(unittest.TestCase):

    def testOne(self):
        self.assertTrue(script.retrieveAllUrls(1))

    def testTwo(self):
        self.assertFalse(script.retrieveAllUrls())

def main():
    unittest.main()

if __name__ == '__main__':
    main()