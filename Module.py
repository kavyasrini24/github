def get_keywords_from_file(file_path):
    keywords = []
    with open(file_path, 'r') as file:
        line = file.readline().rstrip()
        while line:
            if line and line[0] != "#" and '=' in line and line.split("=")[1][0] == "$":
                keywords.append(line.split("=")[1][2:-1])
            line = file.readline().rstrip()
    return sorted(keywords)

def find_differences(file_1_keywords, file_2_keywords):
    file_1_difference = set(file_2_keywords).difference(file_1_keywords)
    file_2_difference = set(file_1_keywords).difference(file_2_keywords)
    return file_1_difference, file_2_difference
