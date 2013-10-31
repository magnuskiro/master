# helpers to read and update dictionaries.

from helpers import read_file


def get_positve_dict():
    lines = read_file('LoughranMcDonald_Positive.csv')
    words = {}
    for l in lines:
        words[l] = 1
    return words


def get_negative_dict():
    lines = read_file('LoughranMcDonald_Negative.csv')
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