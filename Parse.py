def write_properties_not_in_env(file_2_difference, output_file_path):
    with open(output_file_path, mode='wt', encoding='utf-8') as f2d:
        f2d.write('\n'.join(str(line) for line in file_2_difference))
