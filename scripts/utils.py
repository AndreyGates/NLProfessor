def text_to_string(file_name):
    with open(file_name, encoding = 'utf-8', mode = 'r') as file:
        data = file.read().replace('\n', '')

    return data