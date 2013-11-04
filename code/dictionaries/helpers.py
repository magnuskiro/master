
def read_file(file_name):
    file = open(file_name, 'r')
    list = file.readlines()
    for i in range(len(list)):
        list[i] = list[i].rstrip()
        list[i] = list[i].lower()
    return list



