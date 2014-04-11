
def read_file(file_name):
    input_file = open(file_name, 'r')
    lines = input_file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
        lines[i] = lines[i].lower()
    return lines



