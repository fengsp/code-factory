#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import random
import unittest
import sys


class TestSequenceFunctions(unittest.TestCase):
    
    def setUp(self):
        self.seq = range(10)

    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("never get here")

    @unittest.skipIf(2 > 1, "true")
    def test_format(self):
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        pass

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")

if __name__ == '__main__':
    unittest.main()
