from unittest import TestCase

import task2_3

class TestTask2_3(TestCase):
    def setUp(self):
        """Init"""
    def test_hamming(self):
        self.assertEqual(task2_3.hamming(5,6), 2)
    def tearDown(self):
        """Finish"""