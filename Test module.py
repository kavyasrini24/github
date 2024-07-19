import unittest
from src.module import get_keywords_from_file, find_differences

class TestModule(unittest.TestCase):

    def test_get_keywords_from_file(self):
        keywords = get_keywords_from_file('test_application.properties')
        self.assertEqual(keywords, ['keyword1', 'keyword2'])

    def test_find_differences(self):
        file_1_keywords = ['key1', 'key2']
        file_2_keywords = ['key2', 'key3']
        file_1_difference, file_2_difference = find_differences(file_1_keywords, file_2_keywords)
        self.assertEqual(file_1_difference, {'key3'})
        self.assertEqual(file_2_difference, {'key1'})

if __name__ == '__main__':
    unittest.main()
