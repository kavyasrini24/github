import xml.etree.ElementTree as ET

def append_additional_values(env_file, env_file_op, namefinderinxml, xml_files):
    splitting = namefinderinxml.find('value').text.split("${")
    
    if len(splitting) > 1:
        for index, splitter in enumerate(splitting):
            if index > 0:
                for xml_file in xml_files:
                    parsed_xml = ET.parse(xml_file)
                    namefinder = parsed_xml.find(f".//*[name='{splitting[index][:-1]}']")
                    if namefinder:
                        env_file.writelines(f"{namefinder.find('name').text}={namefinder.find('value').text}\n")
                        env_file_op.writelines(f"{namefinder.find('name').text}={namefinder.find('value').text}\n")
