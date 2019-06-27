import unittest
from lad import convert


class TestLad(unittest.TestCase):
    def test_major_minor_to_name(self):
        name = convert('sda5')
        self.assertEqual(name, '8:5')

    def test_name_to_major_minor(self):
        name = convert('8:212')
        self.assertEqual(name, 'sdn4')