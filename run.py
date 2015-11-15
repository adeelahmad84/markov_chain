#!usr/bin/env python
# -*- coding: utf-8 -*-

'''
Docstring
**********
title: Final Project Codecademy
author: Adeel Ahmad
email: adeelahmad84@me.com

'''

__version__ = "0.1"

from markov_python.cc_markov import MarkovChain
from lxml import html
import requests
import unittest

def main():
    try:
        page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
        tree = html.fromstring(page.content)

        #This will create a list of buyers:
        buyers = tree.xpath('//div[@title="buyer-name"]/text()')
        #This will create a list of prices
        prices = tree.xpath('//span[@class="item-price"]/text()')

        print 'Buyers: ', buyers
        print 'Prices: ', prices

    except ValueError:
        print "Oops! There's been an issue"


if __name__ == "__main__":
    main()
    import doctest
    doctest.testmod()
    class MyTest(unittest.TestCase):
        def test(self):
            self.assertEqual(main(), )
