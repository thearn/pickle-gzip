import unittest
import gzp


class TestLoadSaveFunctions(unittest.TestCase):

    def test_save(self):
        data = [1, 2, 3]
        gzp.save()

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

if __name__ == '__main__':
    unittest.main()
