import numpy as np
from math import sqrt


def get_data(filename):
    f = file(filename, 'r')
    data = []
    for line in f:
        data.append(float(line))
    f.close()
    return data, np.mean(data), len(data)


def get_std(dat1, dat2):
    mean1 = np.mean(dat1)
    mean2 = np.mean(dat2)
    summed = (sum((x - mean1)**2 for x in dat1) +
              sum((x - mean2)**2 for x in dat2))
    return summed / (len(dat1) + len(dat2) - 2.0)


if __name__ == "__main__":
    home, home_mean, home_n = get_data('data/homeppg.dat')
    away, away_mean, away_n = get_data('data/awayppg.dat')
    std = get_std(home, away)
    print (home_mean - away_mean) / sqrt(std * (1.0/home_n + 1.0/away_n))

    spread = []
    for i in xrange(len(home)):
        spread.append(home[i] - away[i])
    spread_mean = np.mean(spread)
    spread_std = np.std(spread)
    f = file('data/spread.dat', 'w')
    for val in spread:
        f.write(str(val) + '\n')
    f.close()
    print spread_mean / sqrt(spread_std / (len(spread)-1.0))
