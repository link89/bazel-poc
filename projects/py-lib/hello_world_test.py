from unittest import TestCase
import unittest
from .hello_world import say_hello_world

class HelloWorldTest(TestCase):
    def test_hello_world(self):
        say_hello_world()

if __name__ == '__main__':
    unittest.main()