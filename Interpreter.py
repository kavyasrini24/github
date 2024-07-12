import xml.etree.ElementTree as ET
from src.config import append_additional_values

def append_differences_to_files(file_2_difference, env_file_path, env_file_op_path, xml_files):
    with open(env_file_path, 'a') as env_file, open(env_file_op_path, 'w') as env_file_op:
        for val in file_2_difference:
            commonxml = ET.parse("cbc-osb-common.xml")
            namefinderinxml = commonxml.find(f".//*[name='{val}']")
            env_file.writelines(f"{namefinderinxml.find('name').text}={namefinderinxml.find('value').text}\n")
            env_file_op.writelines(f"{namefinderinxml.find('name').text}={namefinderinxml.find('value').text}\n")
            append_additional_values(env_file, env_file_op, namefinderinxml, xml_files)
