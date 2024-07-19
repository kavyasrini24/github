# src/interpreter.py

from .parser import append_additional_values

def append_differences_to_files(file_2_difference, env_file_path, env_file_op_path, xml_files):
    with open(env_file_path, 'a') as env_file, open(env_file_op_path, 'w') as env_file_op:
        for val in file_2_difference:
            commonxml = xml_files.get("cbc-osb-common.xml")
            if commonxml is None:
                raise FileNotFoundError("cbc-osb-common.xml not found in xml_files")

            namefinderinxml = commonxml.find(f".//*[name='{val}']")
            if namefinderinxml is None:
                print(f"Warning: No element with name '{val}' found in cbc-osb-common.xml")
                continue

            env_file.write(f"{namefinderinxml.find('name').text}={namefinderinxml.find('value').text}\n")
            env_file_op.write(f"{namefinderinxml.find('name').text}={namefinderinxml.find('value').text}\n")
            append_additional_values(env_file, env_file_op, namefinderinxml, xml_files)
