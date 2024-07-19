# run.py

from src.config import load_xml_files
from src.interpreter import append_differences_to_files
from src.module import get_keywords_from_file, find_differences
from src.parser import write_properties_not_in_env

# Load keywords from files
file_1_keywords = get_keywords_from_file('application.properties')
file_2_keywords = get_keywords_from_file('environment.properties')

# Find differences between the two sets of keywords
file_1_difference, file_2_difference = find_differences(file_1_keywords, file_2_keywords)

# Load XML files
xml_files = load_xml_files('cbc-osb-common.xml', 'cbc-service-cbc-osb-dev01.xml', 'cbc-service-cbc-osb-common.xml', 'cbc-osb-dev01.xml', 'new-file.xml')

# Append differences to files
append_differences_to_files(file_2_difference, 'environment.properties', 'environment_op.properties', xml_files)

# Write properties not in environment
write_properties_not_in_env(file_2_difference, 'properties-not-in-env.txt')
