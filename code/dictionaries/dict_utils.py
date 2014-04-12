# coding=utf-8
import codecs
import re
from nltk import bigrams


def get_bigrams_from_text(text):
    """
    creates bigrams based on the input text and returns them
    @param text: the text to create bigrams from.
    @return: list of bigrams
    """
    text = clean_text(text)

    bigrams_list = []
    # for all bigram tuples
    for tup in bigrams(text.split(' ')):
        # find the tuple texts
        # (u'text1', u'text2')
        m_obj = re.search(r'\(u\'(.+)\', u\'(.+)\'\)', str(tup))
        if m_obj:
            # combine tuple parts to bigram
            bigram = m_obj.group(1) + " " + m_obj.group(2)
            # if bigram don't exist
            if bigram not in bigrams_list:
                # add it to list.
                bigrams_list.append(bigram)
    return bigrams_list


def get_positive_negative_tweets_from_manually_labeled_tweets(filename):
    """
    From manually labeled tweets get positive and negative tweets.
    @param filename: file with manually labeled tweets
    @return: return an array with two lists, positive and negative tweets.
    """
    pos = []
    neg = []

    # labeled tweet file format:
    # polarity,id,text
    # -1,578123, content, content content , content
    # 1,17823017,word, word word word, word
    # 0,76125391, word, word word word, word

    # for all manually labeled tweets
    for line in get_lines_from_file(filename):
        params = line.split(",")
        # if tweet is labeled negative
        if params[0] == '-1':
            neg.append(''.join(params[2:]))
        # if tweet is labeled positive
        elif params[0] == '1':
            pos.append(''.join(params[2:]))
    return pos, neg


def remove_duplicates_between_dictionaries(primary_dictionary_name, secondary_dictionary_name):
    """
    Takes two dictionaries and removes duplicates from both.
    Words that are in both dictionaries are neither positive nor negative.
    @param primary_dictionary_name:
    @param secondary_dictionary_name:
    @return:
    """
    primary_dictionary = get_lines_from_file(primary_dictionary_name)
    secondary_dictionary = get_lines_from_file(secondary_dictionary_name)

    # remove duplicates from both lists.
    for w in primary_dictionary:
        #print w
        if w in secondary_dictionary:
            #print "----------DUPLICATE"
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


def get_lines_from_file(filename):
    """
    Reads a file and returns all lines as array.
    @param filename: the location and name of the file.
    @return: array of lines from file.
    """
    input_file = codecs.open(filename, 'r', "utf-8")
    lines = input_file.readlines()
    for i in range(len(lines)):
        # removed .rstrip() don't think we need this here. to much regex fixing elsewhere.
        lines[i] = lines[i].lower()
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


def clean_text(text):
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