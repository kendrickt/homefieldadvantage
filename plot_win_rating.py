from matplotlib import pyplot as plt
import numpy as np


if __name__ == "__main__":
    f = file("data/win_rating.dat", 'r')
    winrating = []
    for line in f:
        winrating.append(float(line))

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
    boxplot_axes.plot([0.5, 0.5], [0, 30], lw=3, color='b')
    boxplot_axes.plot([average, average], [0, 30], lw=3, color='g')

    hist = histplot_axes.hist(winrating, bins=12, color='gray')
    histplot_axes.plot([0.5, 0.5], [0, 30], lw=3, color='b')
    histplot_axes.plot([average, average], [0, 30], lw=3, color='g')

    boxplot_axes.set_xticklabels([], size='large')
    boxplot_axes.set_yticks([])
    histplot_axes.set_yticks([])

    plt.xlabel('at home win-rating', size='large')

    plt.show()

""""
    boxplt.hist(winrating, bins=12, color='gray')
    boxplt.text(average-0.02, 28, "mean=%1.3f" % average, rotation=90)
    boxplt.xlabel('at home win-rating')
    boxplt.ylabel('count')
    boxplt.boxplot(winrating, vert=False, positions=[30])
    boxplt.show()
    """
