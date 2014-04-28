
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt

__author__ = 'kiro'


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

        results = []
        #for all lines in the given filename
        for line in open(filename).readlines():
            # if we have a line containing results
            if "{F" in line:
                # store all accuracy observations of this threshold.
                results.append(line.split(" ")[-2])
        classification_accuracies.append(results)
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
    print_threshold(threshold_files)


if __name__ == "__main__":
    folder = "/home/kiro/ntnu/master/code/classification/"
    filename_separation(folder)