# helpers to read and update dictionaries.
import codecs
from dictionary_utils import get_lines_from_file, write_array_entries_to_file, clean_text, \
    remove_duplicates_between_dictionaries, get_positive_negative_tweets_from_manually_labeled_tweets, \
    get_bigrams_from_text, file_to_lower, get_trigrams_from_text

classification_base = "/home/kiro/ntnu/master/code/classification/"
dictionary_base = "/home/kiro/ntnu/master/code/dictionaries/"


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
            if w not in words:
                #print w
                words.append(w)

    #print words
    # Write all words to file.
    write_array_entries_to_file(words, output_name)
    return


def save_dictionaries(positive_dict, negative_dict, filename):
    """
    Takes two lists of words, creates dictionaries without duplicates, and removed words that are in both dictionaries.
    @param positive_dict: list of positive words.
    @param negative_dict: list of negative words.
    @param filename: name base for output file.
    """
    # removing duplicates for each dictionary and writing to file.
    compile_and_write_dictionary_from_array(positive_dict, filename + "-positive.txt")
    compile_and_write_dictionary_from_array(negative_dict, filename + "-negative.txt")

    # remove duplicates between files.
    remove_duplicates_between_dictionaries(filename + "-positive.txt", filename + "-negative.txt")


def compile_monogram_dictionaries(tweets, filename):
    """
    Takes labeled tweets and create monogram dictionaries for positive and negative words.
    @param tweets: list of tweets that are labeled.
    @param filename: name base for output file.
    @return:
    """
    positive_dict = []
    negative_dict = []

    # positive
    for text in tweets[0]:
        positive_dict.extend(text.split(" "))
    # negative
    for text in tweets[1]:
        negative_dict.extend(text.split(" "))

    filename += "-monogram"
    save_dictionaries(positive_dict, negative_dict, filename)
    return


def compile_bigram_dictionaries(tweets, filename):
    """
    Takes labeled tweets and creates bigram dictionaries for positive and negative words.
    @param tweets: list of tweets that are labeled.
    @param filename: name base for output file.
    @return:
    """
    positive_dict = []
    negative_dict = []

    # positive
    for text in tweets[0]:
        bigrams_list = get_bigrams_from_text(text)
        positive_dict = positive_dict + bigrams_list
    # negative
    for text in tweets[1]:
        bigrams_list = get_bigrams_from_text(text)
        negative_dict = negative_dict + bigrams_list

    filename += "-bigram"
    save_dictionaries(positive_dict, negative_dict, filename)
    return


def compile_trigram_dictionaries(tweets, filename):
    """
    Creating dictionaries of trigrams.
    @param tweets: list of tweets that are labeled.
    @param filename: name base for output file.
    """
    positive_dict = []
    negative_dict = []

    # positive
    for text in tweets[0]:
        trigrams_list = get_trigrams_from_text(text)
        positive_dict = positive_dict + trigrams_list
    # negative
    for text in tweets[1]:
        trigrams_list = get_trigrams_from_text(text)
        negative_dict = negative_dict + trigrams_list

    filename += "-trigram"
    save_dictionaries(positive_dict, negative_dict, filename)
    return


def run_dictionary_compilation():
    """
    helper to run dictionary compilations in one go.
    """
    # manually classified tweet files. and name of dataset.
    data_files = [
        # [name/description, name of file containing tweets]
        ["kiro", "tweets_classified_manually"],
        ["obama", "obama_tweets_classified_manually"]
    ]

    for item in data_files:
        # get labeled tweets
        # tweets[0] are the positive ones, tweets[1] are the negative ones.
        tweets = get_positive_negative_tweets_from_manually_labeled_tweets(classification_base + item[1])

        compile_monogram_dictionaries(tweets, item[0])
        compile_bigram_dictionaries(tweets, item[0])
        compile_trigram_dictionaries(tweets, item[0])


if __name__ == "__main__":
    run_dictionary_compilation()

    # Run one dictionary compilation to get the duplicate words.
    #compile_trigram_dictionaries(
    #    get_positive_negative_tweets_from_manually_labeled_tweets(classification_base + "tweets_classified_manually"),
    #    "kiro")

    #file_to_lower("LoughranMcDonald_Negative.csv", "LoughranMcDonald_Negative.txt")
    #file_to_lower("LoughranMcDonald_Positive.csv", "LoughranMcDonald_Positive.txt")