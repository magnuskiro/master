# helpers to read and update dictionaries.
import codecs
from dictionary_utils import get_lines_from_file, write_array_entries_to_file, clean_text, \
    remove_duplicates_between_dictionaries, get_positive_negative_tweets_from_manually_labeled_tweets, \
    get_bigrams_from_text, file_to_lower

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
    lines = get_lines_from_file(dict)
    words = {}
    for l in lines:
        words[l] = 1
    return words


def get_negative_dict(dict=base + 'negative.csv'):
    lines = get_lines_from_file(dict)
    words = {}
    for l in lines:
        words[l] = -1
    return words


def get_Litigious_dict():
    lines = get_lines_from_file('LoughranMcDonald_Litigious.csv')
    return lines


def get_ModalStrong_dict():
    lines = get_lines_from_file('LoughranMcDonald_ModalStrong.csv')
    return lines


def get_ModalWeak_dict():
    lines = get_lines_from_file('LoughranMcDonald_ModalWeak.csv')
    return lines


def get_Uncertainty_dict():
    lines = get_lines_from_file('LoughranMcDonald_Uncertainty.csv')
    return lines


def get_Emoticons_dict():
    lines = get_lines_from_file('emoticon_polarity.tsv')
    emoticons = {}
    for l in lines:
        split = l.split('\t')
        #print split[0]
        #print split[1]
        emoticons[split[0]] = split[1]
    return emoticons


def compile_and_write_dictionary_from_array(array, output_name):
    """
    Takes an array of word to store, removed duplicates and, the unique and clean words are written to the output file.
    @param array: The array of words to store.
    @param output_name: the file to store processed entries
    @return:
    """
    words = []
    # for all lines in file. (one word per line)
    for w in array:
        # clear out noise and garbage words.
        w = clean_text(w)
        if w:
            #print w
            # if we don't have the word already, store it
            if w not in str(words):
                #print w
                words.append(w+"\n")

    # Write all words to file.
    write_array_entries_to_file(words, output_name)

    return


def compile_monogram_dictionaries():
    """
    Compiles dictionaries of words from the manually labeled tweets.
    @return:
    """
    classification_base = "/home/kiro/ntnu/master/code/classification/"

    # compile dictionaries
    compile_and_write_dictionary_from_array(get_lines_from_file(classification_base + "auto-positive.txt"),
                                            "compiled-positive.txt")
    compile_and_write_dictionary_from_array(get_lines_from_file(classification_base + "auto-negative.txt"),
                                            "compiled-negative.txt")

    # remove duplicates
    remove_duplicates_between_dictionaries("compiled-positive.txt", "compiled-negative.txt")

    return


def compile_bigram_dictionaries(tweet_file):
    """
    reads labeled tweets and creates bigram dictionaries for positive and negative words.
    @param tweet_file: the file containing manually labeled tweets.
    @return:
    """
    classification_base = "/home/kiro/ntnu/master/code/classification/"

    # get labeled tweets
    # tweets[0] are the positive ones, tweets[1] are the negative ones.
    tweets = get_positive_negative_tweets_from_manually_labeled_tweets(classification_base + tweet_file)

    positive_bigrams = []
    negative_bigrams = []

    # positive
    for text in tweets[0]:
        bigrams_list = get_bigrams_from_text(text)
        positive_bigrams = positive_bigrams + bigrams_list
    # negative
    for text in tweets[1]:
        bigrams_list = get_bigrams_from_text(text)
        negative_bigrams = negative_bigrams + bigrams_list

    #print positive_bigrams
    #print negative_bigrams

    # removing duplicates for each dictionary and writing to file.
    compile_and_write_dictionary_from_array(positive_bigrams, "bigram-compiled-positive.txt")
    compile_and_write_dictionary_from_array(negative_bigrams, "bigram-compiled-negative.txt")

    # remove duplicates
    remove_duplicates_between_dictionaries("bigram-compiled-positive.txt", "bigram-compiled-negative.txt")
    return


def compile_dictionaries():
    """
    helper to run monogram and bigram dictionary compilations in one go.
    """
    compile_monogram_dictionaries()
    #compile_bigram_dictionaries("tweets_classified_manually")


if __name__ == "__main__":
    compile_dictionaries()
    #file_to_lower("LoughranMcDonald_Negative.csv", "LoughranMcDonald_Negative.txt")
    #file_to_lower("LoughranMcDonald_Positive.csv", "LoughranMcDonald_Positive.txt")