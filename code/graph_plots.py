__author__ = 'kiro'

import matplotlib.pyplot as plt


def plot_avgerage_threshold_accuracy():
    """
    Plot the threshold and average accuracy for all observations for that threshold value.
    """

    data = [
        # [threshold, accuracy]
        [-0.1, 0.6316],
        [-0.2, 0.6161],
        [-0.3, 0.6059],
        [-0.4, 0.5988],
        [-0.5, 0.5888],
        [-0.6, 0.5711],
        [-0.7, 0.5423],
        [-0.8, 0.5083],
        [-0.9, 0.4881],
        [0.0, 0.6479],
        [0.1, 0.6516],
        [0.2, 0.6511],
        [0.3, 0.6430],
        [0.4, 0.6305],
        [0.5, 0.6122],
        [0.6, 0.5934],
        [0.7, 0.5712],
        [0.8, 0.5457],
        [0.9, 0.5307]
    ]

    x = [e[0] for e in data]
    y = [e[1] for e in data]
    plt.xlabel('Threshold')
    plt.ylabel('Accuracy')
    plt.plot(x, y, 'o')
    plt.show()


def plot_dictionary_accyracy():
    y = [0.4203,
         0.5075,
         0.5827,
         0.8847,
         0.9829,
         0.9819,
         0.4313,
         0.4644,
         0.4313,
         0.3736,
         0.6278,
         0.6015,
         0.5370,
         0.6183,
         0.6352,
         0.6388,
         0.9729,
         0.9714]

    x = [e for e in range(1, 19)]
    plt.axis([0, 19, .3, 1.0])
    plt.xlabel('id')
    plt.ylabel('Accuracy')
    plt.plot(x, y, 'o')
    plt.show()


if __name__ == "__main__":
    #plot_avgerage_threshold_accuracy()
    plot_dictionary_accyracy()