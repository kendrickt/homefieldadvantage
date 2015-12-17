from make_dat_files import get_data
from matplotlib import pyplot as plt
import sys


def plot_data(years, stat, win_type):
    data = get_data('data/%s_top_%s.dat' % (years, stat))
    plt.figure(1)
    min_x, max_x = sys.maxint, 0
    min_y, max_y = sys.maxint, 0

    for datum in data:
        name, value, passes_filter, home_wins, total_wins = datum
        if win_type == 'home':
            wins = home_wins
        elif win_type == 'total':
            wins = total_wins
        else:
            print "Warning: invalid win_type. Defaulted to 'home'."
            wins = home_wins

        if passes_filter:
            color = 'k'
        else:
            color = 'r'
        plt.text(wins, value, name, size='large', color=color)
        min_x, max_x = min(min_x, wins), max(max_x, wins)
        min_y, max_y = min(min_y, value), max(max_y, value)

    plt.xlim(min_x - max_x/10.0, max_x + max_x/10.0)
    plt.ylim(min_y - max_y/10.0, max_y + max_y/10.0)

    # X and Y labels
    plt.ylabel(stat, size='large')
    plt.xlabel('# of %s wins' % win_type, size='large')

    plt.show()


def plot_data_comparison(years_x, stat_x, years_y, stat_y):
    data_x = get_data('data/%s_top_%s.dat' % (years_x, stat_x))
    data_y = get_data('data/%s_top_%s.dat' % (years_y, stat_y))
    plt.figure(1)
    min_x, max_x = sys.maxint, 0
    min_y, max_y = sys.maxint, 0

    data = {}

    # Links a team with their stat_x.
    for datum in data_x:
        name, value = datum[0], datum[1]
        data[name] = [value]

    # Links a team with their stat_y.    for datum in data_y:
    for datum in data_y:
        name, value = datum[0], datum[1]
        data[name].append(value)

    # Plot
    for team in data:
        x_val, y_val = data[team]
        plt.text(x_val, y_val, team, size='large')

        min_x, max_x = min(min_x, x_val), max(max_x, x_val)
        min_y, max_y = min(min_y, y_val), max(max_y, y_val)

    plt.xlim(min_x - max_x/10.0, max_x + max_x/10.0)
    plt.ylim(min_y - max_y/10.0, max_y + max_y/10.0)

    # X and Y labels
    plt.ylabel(stat_y, size='large')
    plt.xlabel(stat_x, size='large')

    plt.show()


if __name__ == '__main__':
    func = sys.argv[1]
    if func == 'plot':
        years, stat, win_type = sys.argv[2:]
        plot_data(years, stat, win_type)
    elif func == 'compare':
        years_x, stat_x, years_y, stat_y = sys.argv[2:]
        plot_data_comparison(years_x, stat_x, years_y, stat_y)
    else:
        print 'Invalid func: %s' % func
