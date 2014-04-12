# coding=utf-8
import codecs
import re


def remove_duplicates_from_dictionaries(primary_dictionary_name, secondary_dictionary_name):
    """
    Takes two dictionaries and removes duplicates from both.
    Words that are in both dictionaries are neither positive nor negative.
    @param primary_dictionary_name:
    @param secondary_dictionary_name:
    @return:
    """
    primary_dictionary = read_file(primary_dictionary_name)
    secondary_dictionary = read_file(secondary_dictionary_name)

    # remove duplicates from both lists.
    for w in primary_dictionary:
        if w in secondary_dictionary:
            primary_dictionary.remove(w)
            secondary_dictionary.remove(w)

    # rewrite the updated lists to file
    write_array_entries_to_file(primary_dictionary, primary_dictionary_name)
    write_array_entries_to_file(secondary_dictionary, secondary_dictionary_name)
    return


def write_array_entries_to_file(array, filename):
    """
    writes all entries in an array to file, if the entry is not in the file already.
    @param array: all the items to write.
    @param filename: the name of the output file
    @return: null
    """
    output = codecs.open(filename, "w", "utf-8")
    output.writelines(array)
    output.close()
    return


def read_file(filename):
    """
    Reads a file and returns all lines as array.
    @param filename: the location and name of the file.
    @return: array of lines from file.
    """
    input_file = codecs.open(filename, 'r', "utf-8")
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
        out.write(str(line[:-1]).lower().strip('[\u2013\u2026+()!\"\#$%&\'\()*+,-./:;<=>?@[]^_`{|}~\r\n]') + "\n")
    out.close()


def clean_word(text):
    """
    Clean input string of unwanted stuff and return it.
    @param text: contaminated string containing the word.
    @return: the clean word.
    """
    # words must have two or more characters.
    # skip all sanitation if it to short.
    if len(text) <= 1:
        return None

    replacement = ""

    # pre and post spaces
    text.strip()

    # remove plurals 's
    pattern = u"'s"
    regex = re.compile(pattern, re.MULTILINE)
    text = regex.sub(replacement, text)

    # don't want retweet
    pattern = u"^rt"
    regex = re.compile(pattern, re.MULTILINE)
    text = regex.sub(replacement, text)

    # don't want to start with http, it's a link removal gone wrong.
    pattern = u"http[s]*[^ ]*"
    regex = re.compile(pattern, re.MULTILINE)
    text = regex.sub(replacement, text)

    # don't want money.
    pattern = u"\$\d+"
    regex = re.compile(pattern, re.MULTILINE)
    text = regex.sub(replacement, text)

    # stripping unwanted characters.
    pattern = u"[!\"\%&\*+,-_./:…;<=>?@~\r\n|\\[\\]}{)(→'“”’]"
    regex = re.compile(pattern, re.MULTILINE)
    text = regex.sub(replacement, text)

    # don't want to start with digit, that's not a word.
    pattern = u"^\d+"
    regex = re.compile(pattern, re.MULTILINE)
    text = regex.sub(replacement, text)

    # words must have two or more characters.
    # recheck if we removed something that made the word to short.
    if len(text) <= 1:
        return None

    return text