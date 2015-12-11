from matplotlib import pyplot as plt


def get_data(filename):
    f = file(filename, 'r')
    data = []
    for line in f:
        data.append(float(line))
    f.close()
    return data


def make_boxplot():
    home = get_data('data/homeppg.dat')
    away = get_data('data/awayppg.dat')
    total = get_data('data/totalppg.dat')

    ax = plt.subplot(111)
    plt.boxplot([home, away, total], vert=False, widths=0.8)
    plt.yticks([])
    plt.text(-3, 3.3, "all games", rotation=90, size='large')
    plt.text(-3, 2.3, "away games", rotation=90, size='large')
    plt.text(-3, 1.3, "home games", rotation=90, size='large')
    plt.xlabel("points per game")
    plt.xlim(-1, 70)
    ax.xaxis.label.set_fontsize(20)
    plt.show()


if __name__ == "__main__":
    make_boxplot()
