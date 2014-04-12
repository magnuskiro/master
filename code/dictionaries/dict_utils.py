
import codecs


def read_file(file_name):
    """
    Reads a file and returns all lines as array.
    @param file_name: the location and name of the file.
    @return: array of lines from file.
    """
    input_file = open(file_name, 'r')
    lines = input_file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
        lines[i] = lines[i].lower()
    return lines


def file_to_lower(filename, output):
    """
    Changes all entries to lower case.
    @param filename: the file to convert
    @param output: the new file that is created.
    """
    out = codecs.open(output, "a", "utf-8")
    for line in open(filename).readlines():
        out.write(str(line[:-1]).lower().strip('[\u2013\u2026+()!\"\#$%&\'\()*+,-./:;<=>?@[]^_`{|}~]\r\n')+"\n")


