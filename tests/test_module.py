import unittest

import stactools.sentinel3_slstr


class TestModule(unittest.TestCase):
    def test_version(self):
        self.assertIsNotNone(stactools.sentinel3_slstr.__version__)
