# helpers to read and update dictionaries.
import codecs
from dict_utils import read_file, file_to_lower

base = "/home/kiro/ntnu/master/code/dictionaries/"


# method to check if a word exists in any dictionary or not.
def find_word(word):
    word = word.lower()
    if word in get_positve_dict(): return True
    if word in get_negative_dict(): return True
    if word in get_Litigious_dict(): return True
    if word in get_ModalStrong_dict(): return True
    if word in get_ModalWeak_dict(): return True
    if word in get_Uncertainty_dict(): return True
    classify_word(word)
    return False


# Save unpolarized words for classification.
def classify_word(word):
    """
    @param word:
    """
    with codecs.open(base + "unclassified_words.txt", "a", "utf-8") as unclassified_words:
        unclassified_words.write(word + '\n')


def get_positve_dict(dict=base + 'positive.csv'):
    lines = read_file(dict)
    words = {}
    for l in lines:
        words[l] = 1
    return words


def get_negative_dict(dict=base + 'negative.csv'):
    lines = read_file(dict)
    words = {}
    for l in lines:
        words[l] = -1
    return words


def get_Litigious_dict():
    lines = read_file('LoughranMcDonald_Litigious.csv')
    return lines


def get_ModalStrong_dict():
    lines = read_file('LoughranMcDonald_ModalStrong.csv')
    return lines


def get_ModalWeak_dict():
    lines = read_file('LoughranMcDonald_ModalWeak.csv')
    return lines


def get_Uncertainty_dict():
    lines = read_file('LoughranMcDonald_Uncertainty.csv')
    return lines


def get_Emoticons_dict():
    lines = read_file('emoticon_polarity.tsv')
    emoticons = {}
    for l in lines:
        split = l.split('\t')
        #print split[0]
        #print split[1]
        emoticons[split[0]] = split[1]
    return emoticons


def clean_dcictionary(dctionary):
    return


# Test code
def to_lower():
    file_to_lower("negative.txt-old", "negative.txt")
    file_to_lower("positive.txt-old", "positive.txt")
    file_to_lower("LoughranMcDonald_Negative.csv", "negative.txt")
    file_to_lower("LoughranMcDonald_Positive.csv", "positive.txt")


if __name__ == "__main__":
    exit()