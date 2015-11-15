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
import unittest

def main():
    try:
        mc = MarkovChain()
        text = mc.add_file('ascii.txt')

        mc.generate_text(text)

    except ValueError:
        print "Oops! There's been an issue"

if __name__ == "__main__":
    main()
    import doctest
    doctest.testmod()
    class MyTest(unittest.TestCase):
        def test(self):
            self.assertEqual(main(), )
