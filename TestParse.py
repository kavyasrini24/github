import unittest
from src.parser import write_properties_not_in_env

class TestParser(unittest.TestCase):

    def test_write_properties_not_in_env(self):
        file_2_difference = {'key3'}
        write_properties_not_in_env(file_2_difference, 'test_properties-not-in-env.txt')
        with open('test_properties-not-in-env.txt', 'r') as f2d:
            lines = f2d.readlines()
        self.assertIn('key3\n', lines)

if __name__ == '__main__':
    unittest.main()
