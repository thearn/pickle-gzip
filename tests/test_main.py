import unittest
import gzp
import os


class TestLoadSaveFunctions(unittest.TestCase):

    def test_save(self):
        data = [1, 2, 3]
        gzp.save(data, "test.dat")
        self.assertTrue(os.path.exists("test.dat"))

if __name__ == '__main__':
    unittest.main()
