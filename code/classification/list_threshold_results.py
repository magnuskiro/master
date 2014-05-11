
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt

__author__ = 'kiro'

classification_base = "/home/kiro/ntnu/master/code/classification/"


def plot_data(threshold, acc_array):
    """
    Plots the accuracy of a dataset, given the threshold value.
    @param threshold: list of threshold values. -0.9 -> 0.9, step 0.1
    @param acc_array: list of lists containing the classification correctness.
    """

    # each element in acc_array is a list of the classification accuracy for each dataset with the given threshold
    # acc_array = [[0.5, 0.7, 0.9], [0.5, 0.7, 0.9]]
    # acc_array = [[set1, set2, set3], [set1, set2, set3]]

    # for the number of datasets
        # find all threshold accuracies for a dataset.
            # plot that accuracy graph for the dataset

    # for the number of datasets.
    for i in range(1, len(acc_array[0])+1):
        # get all accuracies observations for the same threshold for a dataset.
        y = [e[i-1] for e in acc_array]
        plt.subplot(6, 3, i)
        #plt.title(i)
        plt.grid(True)
        plt.axis([-1.0, 1.0, 0, 1.0])
        plt.plot(threshold, y, 'o')

    plt.xlabel('Threshold')
    plt.ylabel('Accuracy')
    plt.show()


def get_results_from_file(filename):
    """
    Reads accuracy results from file and returns them.
    @param filename: the name of the file to get accuracies from.
    @return: list of accuracies.
    """
    results = []
    #for all lines in the given filename
    for line in open(filename).readlines():
        # if we have a line containing results
        if "{F" in line:
            # store all accuracy observations of this threshold.
            results.append(float(line.split(" ")[-2]))
    return results


def print_threshold(files):
    """

    @param files: list of filenames containing trend data.
    """
    # list of threshold values. -0.9 -> 0.9, step 0.1
    thresholds = []

    # each element in acc_array is a list of the classification accuracy for each dataset with the given threshold
    # acc_array = [[0.5, 0.7, 0.9], [0.5, 0.7, 0.9]]
    # acc_array = [[set1, set2, set3], [set1, set2, set3]]
    classification_accuracies = []

    # for all filenames
    for filename in files:
        # get threshold value from name
        if filename[0] == "-":
            name = filename[0:4]
        else:
            name = filename[0:3]
        #print name
        # store the threshold value for this file.
        thresholds.append(float(name))

        classification_accuracies.append(get_results_from_file(filename))
        #print " ".join(results)

    #print classification_accuracies
    #print thresholds
    plot_data(thresholds, classification_accuracies)


def filename_separation(trend_folder):
    """
    Get list of wanted filenames from the trend data folder.
    @param trend_folder: the directory to look for files.
    """
    files = [f for f in listdir(trend_folder) if isfile(join(trend_folder, f))]
    threshold_files = []
    files.sort()
    for filename in files:
        if ".py" in filename:
            continue
        if not ".txt" in filename:
            continue
        # if it's a file we want append it to list of files.
        if "threshold" in filename:
            threshold_files.append(filename)
            continue
    return threshold_files


def average_accuracy_for_threshold(directory):
    """
    Find the average accuracy for all thresholds and print each one.
    @param directory: the directory to find threshold variation results in.
    """
    threshold_files = filename_separation(directory)

    for filename in threshold_files:
        results = get_results_from_file(filename)
        if filename[0] == "-":
            print filename[0:4], "avg:", sum(results) / len(results)
        else:
            print filename[0:3], "avg:", sum(results) / len(results)


if __name__ == "__main__":
    average_accuracy_for_threshold(classification_base)
    print_threshold(filename_separation(classification_base))
