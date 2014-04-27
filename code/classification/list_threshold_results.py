
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt

__author__ = 'kiro'


def plot_data(threshold, acc_array):
    """
    Plots the accuracy of a dataset, given the threshold value.
    @param threshold:
    @param acc_array:
    """
    # threshold = [0.1, 0.2, ..]

    # each element in acc_array is a list of the classification accuracy for each dataset with the given threshold
    # acc_array = [[0.5, 0.7, 0.9], [0.5, 0.7, 0.9]]
    # acc_array = [[set1, set2, set3], [set1, set2, set3]]

    # for the number of datasets
        # take [x] of each array in acc_array
            # plot that accuracy graph.

    # for the number of datasets.
    for i in range(1, len(acc_array[0])+1):
        # get all accuracies for a dataset.
        y = [e[i-1] for e in acc_array]
        plt.subplot(6, 2, i)
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
    thresholds = []
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
        #for all lines in the fiven filename
        for line in open(filename).readlines():
            # if we have a line contining results
            if "{F" in line:
                # store all accuracy observations of this threshold.
                results.append(line.split(" ")[-2])
        classification_accuracies.append(results)
        #print " ".join(results)
    #print classification_accuracies
    #plot_data(thresholds, classification_accuracies)


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