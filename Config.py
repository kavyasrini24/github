import os
from xml.etree import ElementTree as ET

def load_xml_files(*file_paths):
    xml_files = {}
    for file_path in file_paths:
        if os.path.exists(file_path):
            xml_files[file_path] = ET.parse(file_path).getroot()
        else:
            print(f"Warning: {file_path} does not exist")
    return xml_files
