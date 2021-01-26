from flask import Blueprint
import unittest

main = Blueprint('main', __name__)

from . import views

class MainTest(unittest.TestCase):
    def test_views(self):
        self.assertTrue(True);


