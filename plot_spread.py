from matplotlib import pyplot as plt
import numpy as np


def get_data(filename):
    f = file(filename, 'r')
    data = []
    for line in f:
        data.append(float(line))
    f.close()
    return data


def make_boxplot():
    data = get_data('data/spread.dat')

    ax = plt.subplot(111)
    plt.boxplot(data, vert=False, widths=0.8)
    plt.yticks([])
    plt.xlabel("spread")
    ax.xaxis.label.set_fontsize(20)
    plt.show()


if __name__ == "__main__":
    f = file("data/spread.dat", 'r')
    winrating = []
    for line in f:
        winrating.append(float(line))
    print len(winrating)

    average = np.mean(winrating)

    fig = plt.figure(figsize=(6, 4))
    boxplot_axes = fig.add_axes([0.1, 0.7, 0.7, 0.15])
    histplot_axes = fig.add_axes([0.1, 0.1, 0.7, 0.6])
    histplot_axes.xaxis.label.set_fontsize(13)
    histplot_axes.yaxis.label.set_fontsize(13)
    for item in (histplot_axes.get_xticklabels() +
                 histplot_axes.get_yticklabels()):
        item.set_fontsize(13)

    boxplot = boxplot_axes.boxplot(winrating, notch=True, vert=False)
    boxplot_axes.plot([average, average], [0, 30], lw=3, color='g')
    boxplot_axes.plot([0, 0], [0, 30], lw=3, color='b')

    hist = histplot_axes.hist(winrating, bins=12, color='gray')
    histplot_axes.plot([average, average], [0, 500], lw=3, color='g')
    histplot_axes.plot([0, 0], [0, 500], lw=3, color='b')

    boxplot_axes.set_xticklabels([])
    boxplot_axes.set_yticks([])
    histplot_axes.set_yticks([])

    plt.xlabel('at home point spread', size='large')

    plt.show()
