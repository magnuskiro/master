# coding=utf-8
import codecs
import os
import re
from nltk import bigrams, ngrams


def get_trigrams_from_text(text):
    """
    Creates trigrams form text and returns them.
    @param text: the text to create trigrams from.
    @return: list of trigrams
    """
    # if we have no words to work with, return empty list.
    text = clean_text(text)
    if not text:
        return []

    trigrams_list = []
    # for all tuples representing ngrams
    for tup in ngrams(text.split(' '), 3):
        # find the tuple texts
        # (u'text1', u'text2', u'text3')
        m_obj = re.search(r'\(u\'(.+)\', u\'(.+)\', u\'(.+)\'\)', str(tup).decode())
        if m_obj:
            # combine tuple parts to trigram
            word = m_obj.group(1) + " " + m_obj.group(2) + " " + m_obj.group(3)
            # if word don't exist
            if word not in trigrams_list:
                # add it to list.
                trigrams_list.append(word)
    return trigrams_list


def get_bigrams_from_text(text):
    """
    creates bigrams based on the input text and returns them
    @param text: the text to create bigrams from.
    @return: list of bigrams
    """
    # if we have no words to work with, return empty list.
    text = clean_text(text)
    if not text:
        return []

    bigrams_list = []
    # for all bigram tuples
    for tup in bigrams(text.split(' ')):
        # find the tuple texts
        # (u'text1', u'text2')
        m_obj = re.search(r'\(u\'(.+)\', u\'(.+)\'\)', str(tup).decode())
        if m_obj:
            # combine tuple parts to bigram
            word = m_obj.group(1) + " " + m_obj.group(2)
            # if bigram don't exist
            if word not in bigrams_list:
                # add it to list.
                bigrams_list.append(word)
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

    duplicate_words = []

    # for all words in the primary dictionary.
    for pw in primary_dictionary:
        #print w
        # for all words in the secondary dictionary.
        for sw in secondary_dictionary:
            # if primary word equals secondary word
            if pw == sw:
                # remove word from both dictionaries.
                primary_dictionary.remove(pw)
                secondary_dictionary.remove(sw)
                duplicate_words.append(pw)
                # as we don't have duplicates within a list we skip to the next pw.
                break

    # rewrite the updated lists to file
    write_array_entries_to_file(primary_dictionary, primary_dictionary_name)
    write_array_entries_to_file(secondary_dictionary, secondary_dictionary_name)
    write_array_entries_to_file(duplicate_words, "duplicate-words")
    return


def write_array_entries_to_file(array, filename):
    """
    writes all entries in an array to file, if the entry is not in the file already.
    @param array: all the items to write.
    @param filename: the name of the output file
    @return: null
    """
    output = codecs.open(filename, "w", "utf-8")
    output.writelines([item.strip("\n") + "\n" for item in array])
    output.close()
    return


def get_lines_from_file(filename):
    """
    Reads a file and returns all lines as array.
    @param filename: the location and name of the file.
    @return: array of lines from file.
    """
    # if the file don't exist return empty array.
    if not os.path.isfile(filename):
        return []

    input_file = codecs.open(filename, 'r', "utf-8")
    lines = input_file.readlines()
    for i in range(len(lines)):
        # removed .rstrip() don't think we need this here. to much regex fixing elsewhere.
        lines[i] = lines[i].lower().strip("\n")
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
        out.write(
            str(line[:-1]).decode().lower().strip('[\u2013\u2026+()!\"\#$%&\'\()*+,-./:;<=>?@[]^_`{|}~\r\n]') + "\n")
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