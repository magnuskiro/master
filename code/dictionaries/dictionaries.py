# helpers to read and update dictionaries.
from helpers import read_file

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


def classify_word(word):
    with open("unclassified_words.txt", "a") as unclassified_words:
        unclassified_words.write(word+'\n')


def get_positve_dict():
    lines = read_file(base + 'LoughranMcDonald_Positive.csv')
    words = {}
    for l in lines:
        words[l] = 1
    return words


def get_negative_dict():
    lines = read_file(base + 'LoughranMcDonald_Negative.csv')
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


#print get_positve_dict()
#print get_negative_dict()
#print get_Litigious_dict()
#rint get_ModalStrong_dict()
#print get_ModalWeak_dict()
#print get_Uncertainty_dict()
#print get_Emoticons_dict()
