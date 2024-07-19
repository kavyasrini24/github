import unittest
from xml.etree import ElementTree as ET
from src.interpreter import append_differences_to_files

class TestInterpreter(unittest.TestCase):

    def setUp(self):
        # Mock XML file structures
        self.xml_files = {
            'cbc-osb-common.xml': ET.ElementTree(ET.Element("root")).getroot(),
            'cbc-service-cbc-osb-dev01.xml': ET.ElementTree(ET.Element("root")).getroot(),
            'cbc-service-cbc-osb-common.xml': ET.ElementTree(ET.Element("root")).getroot(),
            'cbc-osb-dev01.xml': ET.ElementTree(ET.Element("root")).getroot(),
            'new-file.xml': ET.ElementTree(ET.Element("root")).getroot()
        }

    def test_append_differences_to_files(self):
        file_2_difference = {'key3'}
        append_differences_to_files(file_2_difference, 'test_environment.properties', 'test_environment_op.properties', self.xml_files)
        with open('test_environment.properties', 'r') as env_file:
            lines = env_file.readlines()
        self.assertIn('key3=value3\n', lines)
        with open('test_environment_op.properties', 'r') as env_file_op:
            lines = env_file_op.readlines()
        self.assertIn('key3=value3\n', lines)

if __name__ == '__main__':
    unittest.main()
