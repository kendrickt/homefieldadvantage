import sys
from compare_all_games import read_game_file as rgf

"""
This file grabs the five teams listed from bleacher reports 2011 list of
top 5 hardest home fields to play against. Then looks at how those teams'
performances differ when they play at home vs away.
"""
if __name__ == '__main__':
    f = file('games/games_combined.csv', 'r')
    teams = sys.argv[1:]
    if not len(teams):
        teams = ['SEA', 'CHI', 'MIN', 'DEN', 'KC']

    team_to_games = {}
    for team in teams:
        team_to_games[team] = []

    games = rgf(f)
    for game in games:
        if game.team in teams:
            team_to_games[game.team].append(game)

    for team in team_to_games:
        games = team_to_games[team]
        home_pts, home_games = 0, 0.0
        away_pts, away_games = 0, 0.0
        for game in games:
            if game.ishome:
                home_pts += game.pts
                home_games += 1.0
            else:
                away_pts += game.pts
                away_games += 1.0
        print team, (home_pts/home_games)/(away_pts/away_games)
