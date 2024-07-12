import unittest
from src.interpreter import append_differences_to_files

class TestInterpreter(unittest.TestCase):
    def test_append_differences_to_files(self):
        file_2_difference = {'key3'}
        xml_files = ['test.xml']
        append_differences_to_files(file_2_difference, 'test_environment.properties', 'test_environment_op.properties', xml_files)
        with open('test_environment.properties', 'r') as env_file:
            lines = env_file.readlines()
        self.assertIn('key3=value3\n', lines)
        with open('test_environment_op.properties', 'r') as env_file_op:
            lines = env_file_op.readlines()
        self.assertIn('key3=value3\n', lines)

if __name__ == "__main__":
    unittest.main()
