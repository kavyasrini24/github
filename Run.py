from src.module import get_keywords_from_file, find_differences
from src.interpreter import append_differences_to_files
from src.parser import write_properties_not_in_env

# Define the XML files to be parsed
xml_files = ["cbc-service-cbc-osb-dev01.xml", "cbc-service-cbc-osb-common.xml", "cbc-osb-dev01.xml"]

file_1_keywords = get_keywords_from_file('application.properties')
file_2_keywords = get_keywords_from_file('environment.properties')

file_1_difference, file_2_difference = find_differences(file_1_keywords, file_2_keywords)

append_differences_to_files(file_2_difference, 'environment.properties', 'environment_op.properties', xml_files)
write_properties_not_in_env(file_2_difference, 'properties-not-in-env.txt')
