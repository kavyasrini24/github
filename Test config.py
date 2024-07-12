import unittest
import xml.etree.ElementTree as ET
from src.config import append_additional_values

class TestConfig(unittest.TestCase):
    def test_append_additional_values(self):
        with open('test_env_file.txt', 'w') as env_file, open('test_env_file_op.txt', 'w') as env_file_op:
            namefinderinxml = ET.Element('root')
            value = ET.SubElement(namefinderinxml, 'value')
            value.text = '${dummy_value}'
            xml_files = ['test.xml']
            append_additional_values(env_file, env_file_op, namefinderinxml, xml_files)
        with open('test_env_file.txt', 'r') as env_file:
            lines = env_file.readlines()
        self.assertIn('dummy_value=value\n', lines)

if __name__ == "__main__":
    unittest.main()
