#!usr/bin/env python
# -*- coding: utf-8 -*-

'''
Docstring
**********

title: Final Project Codecademy
author: Adeel Ahmad
email: adeelahmad84@me.com

'''

from markov_python.cc_markov import MarkovChain
import urllib2
import unittest

__version__ = "0.1"

def main():
    def fun(x):
        return x + 1

    class MyTest(unittest.TestCase):
        def test(self):
            self.assertEqual(fun(3), 4)

if __name__ == "__main__":
    main()
    import doctest
    doctest.testmod()
