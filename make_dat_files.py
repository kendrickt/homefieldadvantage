import sys
from game import Game


def read_game_file(f):
    games = []
    f.next()  # header
    for line in f:
        game = line_to_game(line)
        games.append(game)
    f.close()
    return games


def line_to_game(line):
    data = line.split(',')
    year, team, ishome, week, pts, ptsallowed = (
        int(data[0]), data[1], int(data[2]),
        int(data[3]), int(data[4]), int(data[5])
    )
    return Game(year, week, team, ishome, pts, ptsallowed)


def partition_games(games, partitioner):
    partitions = {}
    for game in games:
        key = partitioner(game)
        if key in partitions:
            partitions[key].append(game)
        else:
            partitions[key] = [game]
    return partitions


def write_stat(games, eq_class_func, get_stat, mask, filename):
    out = file(filename, 'w')
    if eq_class_func:
        partition = partition_games(games, eq_class_func)
        partition = partition.values()
    else:
        partition = games
    count = 0
    for part in partition:
        stat = get_stat(part, mask)
        if stat is not None:
            count += 1
            out.write('%1.3f\n' % stat)
    out.close()


def write_home_win_rating(games):
    write_stat(
        games,
        lambda x: (x.week, x.year),
        get_home_win_rating,
        lambda x: x.ishome,
        'data/home_win_rating.dat'
    )


def get_home_win_rating(games, mask):
    wins, num_of_games = 0.0, 0.0
    for game in games:
        if mask(game):
            if game.pts > game.ptsallowed:
                wins += 1.0
            num_of_games += 1.0
    if num_of_games > 0:
        return wins / num_of_games
    else:
        return None


def get_ppg(games, mask):
    if type(games) is list:
        pts, num_of_games = 0.0, 0.0
        for game in games:
            if mask(game):
                pts += game.pts
                num_of_games += 1.0
        if num_of_games > 0:
            return pts / num_of_games
        else:
            return None
    else:
        game = games
        if mask(game):
            pts = game.pts
            num_of_games = 1.0
            return pts / num_of_games
        else:
            return None


def write_home_ppg(games):
    write_stat(
        games,
        None,
        get_ppg,
        lambda x: x.ishome,
        'data/home_ppg.dat'
    )


def write_away_ppg(games):
    write_stat(
        games,
        None,
        get_ppg,
        lambda x: not int(x.ishome),
        'data/away_ppg.dat'
    )


def write_total_ppg(games):
    write_stat(
        games,
        None,
        get_ppg,
        lambda x: True,
        'data/total_ppg.dat'
    )


def write_spread(games):
    write_stat(
        games,
        lambda x: x,
        get_spread,
        lambda x: x.ishome,
        'data/home_spread.dat'
    )


def get_spread(games, mask):
    spread, num_of_games = 0, 0.0
    for game in games:
        if mask(game):
            spread += game.pts - game.ptsallowed
            num_of_games += 1.0
    if num_of_games:
        return spread / num_of_games
    else:
        return None


if __name__ == "__main__":
    f = file('games/games_combined.csv', 'r')
    games = read_game_file(f)

    func = sys.argv[1]
    function_dict = {
        'homeppg': write_home_ppg,
        'awayppg': write_away_ppg,
        'totalppg': write_total_ppg,
        'winrating': write_home_win_rating
    }

    if func in function_dict:
        function_dict[func](games)
    else:
        print "invalid function: %s" % func
        print "valid functions are: ", function_dict.keys()
