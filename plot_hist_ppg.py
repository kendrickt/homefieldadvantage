from matplotlib import pyplot as plt
import numpy as np


if __name__ == "__main__":
    f = file('data/homeppg.dat', 'r')
    ppgs = []
    for line in f:
        ppgs.append(float(line))
    f.close()
    average = np.mean(ppgs)

    f = file('data/totalppg.dat', 'r')
    totalppgs = []
    for line in f:
        totalppgs.append(float(line))
    f.close()
    totalppg_avg = np.mean(totalppgs)

    f, (ax1, ax2) = plt.subplots(2, sharex=True)
    histtot = ax1.hist(totalppgs, bins=12, color='gray')
    ax1.plot([totalppg_avg, totalppg_avg], [0, 700], lw=3, color='g')
    ax1.text(
        totalppg_avg+1, 620, "total mean=%1.3f" % totalppg_avg, size='large')
    ax1.text(-3, 520, "all games", rotation=90, size='large')
    ax1.set_yticks([])

    hist = ax2.hist(ppgs, bins=12, color='gray')
    ax2.plot([average, average], [0, 350], lw=3, color='b')
    ax2.text(average+1, 300, "home mean=%1.3f" % average, size='large')
    ax2.text(-3, 270, "home games", rotation=90, size='large')

    plt.yticks([])
    plt.xlabel('points per game', size='large')

    plt.show()
