from xml.etree import ElementTree as ET

def append_additional_values(env_file, env_file_op, namefinderinxml, xml_files):
    splitting = namefinderinxml.find('value').text.split("${")
    if len(splitting) > 1:
        for index, splitter in enumerate(splitting):
            if index > 0:
                element_found = False
                for xml_name in ['cbc-service-cbc-osb-dev01.xml', 'cbc-service-cbc-osb-common.xml', 'cbc-osb-dev01.xml', 'new-file.xml']:
                    devxml = xml_files.get(xml_name)
                    if devxml is None:
                        print(f"Warning: {xml_name} not found in xml_files")
                        continue

                    namefinderindevxml = devxml.find(f".//*[name='{splitting[index][:-1]}']")
                    if namefinderindevxml:
                        env_file.write(f"{namefinderindevxml.find('name').text}={namefinderindevxml.find('value').text}\n")
                        env_file_op.write(f"{namefinderindevxml.find('name').text}={namefinderindevxml.find('value').text}\n")
                        element_found = True
                        break

                if not element_found:
                    print(f"Warning: No element with name '{splitting[index][:-1]}' found in any XML files")

def append_differences_to_files(file_2_difference, env_file_path, env_file_op_path, xml_files):
    with open(env_file_path, 'a') as env_file, open(env_file_op_path, 'w') as env_file_op:
        for val in file_2_difference:
            element_found = False
            for xml_name in ['cbc-osb-common.xml', 'new-file.xml']:
                commonxml = xml_files.get(xml_name)
                if commonxml is None:
                    print(f"Warning: {xml_name} not found in xml_files")
                    continue

                namefinderinxml = commonxml.find(f".//*[name='{val}']")
                if namefinderinxml:
                    env_file.write(f"{namefinderinxml.find('name').text}={namefinderinxml.find('value').text}\n")
                    env_file_op.write(f"{namefinderinxml.find('name').text}={namefinderinxml.find('value').text}\n")
                    append_additional_values(env_file, env_file_op, namefinderinxml, xml_files)
                    element_found = True
                    break

            if not element_found:
                print(f"Warning: No element with name '{val}' found in any XML files")
