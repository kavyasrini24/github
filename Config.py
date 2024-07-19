# src/config.py

from xml.etree import ElementTree as ET

def load_xml_files(*file_paths):
    xml_files = {}
    for file_path in file_paths:
        xml_files[file_path] = ET.parse(file_path).getroot()
    return xml_files
