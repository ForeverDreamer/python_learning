import unittest
import doctest
import yatzy


def load_test(loader, tests, ignore):
    """让unittest能检测到doctest， 执行：python -m unittest"""
    tests.addTests(doctest.DocTestSuite(yatzy))
    return tests
