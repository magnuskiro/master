# coding=utf-8
import codecs
import re


def clean_word(text):
    """
    Clean input string of unwanted stuff and return it.
    @param text: contaminated string containing the word.
    @return: the clean word.
    """
    # words must have two or more characters.
    if len(text) <= 1:
        return None

    replacement = ""
    # stripping unwanted characters.
    pattern = u"[!\"\%&\*+,-./:…;<=>?@~\r\n|\\[\\]}{)(→']"
    regex = re.compile(pattern, re.MULTILINE)
    text = regex.sub(replacement, text)

    # pre and post spaces
    text.strip()

    return text


def write_array_entries_to_file(array, filename):
    """
    writes all entries in an array to file, if the entry is not in the file already.
    @param array: all the items to write.
    @param filename: the name of the output file
    @return: null
    """
    # TODO this can be done quite elegantly in some oneliner way.
    output = codecs.open(filename, "rw", "utf-8")
    content = output.readlines()
    for item in array:
        if not item in content:
            output.write(item + "\n")
    output.close()
    return


def read_file(file_name):
    """
    Reads a file and returns all lines as array.
    @param file_name: the location and name of the file.
    @return: array of lines from file.
    """
    input_file = codecs.open(file_name, 'r', "utf-8")
    lines = input_file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip().lower()
    input_file.close()
    return lines


def file_to_lower(filename, output):
    """
    Changes all entries to lower case.
    @param filename: the file to convert
    @param output: the new file that is created.
    """
    out = codecs.open(output, "a", "utf-8")
    for line in open(filename).readlines():
        out.write(str(line[:-1]).lower().strip('[\u2013\u2026+()!\"\#$%&\'\()*+,-./:;<=>?@[]^_`{|}~]\r\n') + "\n")
    out.close()


