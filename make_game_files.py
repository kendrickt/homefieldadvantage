import sys
import nflgame


def combine_games(years):
    """
    Given a list of years, the .csv files associated with those years
    are concatenated into a combined game csv.
    """
    combined_games = file('games/games_combined.csv', 'w')
    print_header(combined_games)

    for year in years:
        try:
            f = file('games/games_' + year + '.csv', 'r')
        except IOError:
            print year,
            print 'does not have a file associated with it'
            break

        f.next()  # header
        for line in f:
            combined_games.write(year + ',' + line)
        f.close()
    combined_games.close()


def print_header(f):
    """
    Writes the common header to the file f.
    """
    f.write('team,ishome,week,pts,ptsallowed\n')


def get_games(years):
    """
    Given a list of N years, N .csv files will be written,
    each containing game data for the regular season of that year.
    """
    for year in years:
        f = file('games/games_' + year + '.csv', 'w')
        print_header(f)

        games = nflgame.games(int(year))
        for game in games:
            home_team = game.home
            home_score = str(game.score_home)
            away_team = game.away
            away_score = str(game.score_away)
            week = game.schedule['week']

            f.write(
                home_team + ',1,' + str(week) + ',' + home_score + ',' +
                away_score + '\n')
            f.write(
                away_team + ',0,' + str(week) + ',' + away_score + ',' +
                home_score + '\n')
        f.close()


if __name__ == "__main__":
    func = sys.argv[1]
    years = sys.argv[2:]
    if not len(years):
        years = ['2009', '2010', '2011', '2012', '2013', '2014', '2015']

    function_dict = {
        'get': get_games,
        'combine': combine_games
    }

    if func in function_dict:
        function_dict[func](years)
    else:
        print "invalid function: %s" % func
        print "valid functions are: ", function_dict.keys()
