import sys
from make_dat_files import read_game_file as rgf


def check_teams(teams):
    team_to_games = {}
    for team in teams:
        team_to_games[team] = []

    games = rgf('games/games_combined.csv')
    for game in games:
        if game.team in teams:
            team_to_games[game.team].append(game)

    for team in team_to_games:
        games = team_to_games[team]
        home_pts, home_games = 0, 0.0
        away_pts, away_games = 0, 0.0
        for game in games:
            if game.ishome:
                home_pts += game.pts - game.ptsallowed
                home_games += 1.0
            else:
                away_pts += game.pts - game.ptsallowed
                away_games += 1.0

        print home_pts, away_pts
        print team, (home_pts/home_games)/(away_pts/away_games)


def get_teams_sorted_by_HFA():
    games = rgf('games/games_combined.csv')
    teams_to_games = {}
    for game in games:
        if game.team in teams_to_games.keys():
            teams_to_games[game.team].append(game)
        else:
            teams_to_games[game.team] = []

    teams_to_stats = []
    for team in teams_to_games:
        games = teams_to_games[team]
        home_pts, home_wins, home_games = 0, 0, 0.0
        away_pts, away_wins, away_games = 0, 0, 0.0
        for game in games:
            if game.ishome:
                home_pts += game.pts - game.ptsallowed
                home_games += 1.0
                if game.pts > game.ptsallowed:
                    home_wins += 1
            else:
                away_pts += game.pts - game.ptsallowed
                away_games += 1.0
                if game.pts > game.ptsallowed:
                    away_wins += 1
        if (away_wins/away_games) > 0.300:
            teams_to_stats.append((team,
                                   (home_pts/home_games) - (away_pts/away_games),
                                   (home_wins/home_games) - (away_wins/away_games)
                                   )
                                  )

    # sort them
    teams_to_stats.sort(key=lambda x: x[1])
    for x in teams_to_stats:
        print x


if __name__ == '__main__':
    try:
        func = sys.argv[1]
    except:
        func = None

    if func == 'get':
        check_teams(sys.argv[2:])
    elif func == 'bleacherreport':
        teams = ['SEA', 'CHI', 'MIN', 'DEN', 'KC']
        check_teams(teams)
    else:
        get_teams_sorted_by_HFA()
