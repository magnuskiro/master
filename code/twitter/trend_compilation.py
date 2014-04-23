
from os import listdir
from os.path import isfile
from sqlalchemy import join

__author__ = 'kiro'


trend_base = "/home/kiro/ntnu/master/code/twitter/trend-data/"


def filename_separation(folder):
    """
    Run trend file compilation with all wanted files in the folder.
    @param folder: the folder containing tweet files.
    """
    files = [f for f in listdir(folder) if isfile(join(folder, f))]
    trend_files = []
    files.sort().reverse()
    for filename in files:
        # disregard special files.
        if filename[0] == "_":
            continue
        # skipping the metadata files.
        if ".meta" in filename:
            continue
        # don't aggregate the trend files, the trend files contains already sorted tweets
        if "trend" in filename:
            trend_files.append(filename)
            continue
        # append filename to list.


if __name__ == "__main__":
    filename_separation(trend_base)
