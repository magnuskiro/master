# helpers to read and update dictionaries.
import codecs
from dict_utils import read_file, file_to_lower, write_array_entries_to_file, clean_word

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


def compile_dictionary_from_file(filename, output_name):
    """
    Reads a file and stores unique and clean words to output file.
    @param filename: the file to gets entries from
    @param output_name: the file to store processed entries
    @return: nothing
    """
    lines = read_file(filename)
    words = []
    for w in lines:
        # clear out noise and garbage words.
        w = clean_word(w)
        if w:
            #print w
            # if we don't have the word already store it
            if w not in words:
                #print w
                words.append(w)

    # Write all words to file.
    write_array_entries_to_file(words, output_name)

    return


# Test code
def to_lower():
    file_to_lower("negative.txt-old", "negative.txt")
    file_to_lower("positive.txt-old", "positive.txt")
    file_to_lower("LoughranMcDonald_Negative.csv", "negative.txt")
    file_to_lower("LoughranMcDonald_Positive.csv", "positive.txt")


def compile_auto_generated_dictionaries():
    """
    Compiles dictionaries from word of the manually labeled tweets.
    @return:
    """
    classification_base = "/home/kiro/ntnu/master/code/classification/"
    compile_dictionary_from_file(classification_base+"auto-positive.txt", "compiled-positive.txt")
    compile_dictionary_from_file(classification_base+"auto-negative.txt", "compiled-negative.txt")
    return

if __name__ == "__main__":
    compile_auto_generated_dictionaries()
    exit()