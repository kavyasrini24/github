# src/parser.py

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
