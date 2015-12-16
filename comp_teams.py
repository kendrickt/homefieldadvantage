from make_dat_files import read_game_file
from collections import defaultdict
import sys


class Team(object):
    """
    An object which keeps track of a teams home stats, away stats, total stats,
    the ratio between home and away stats,
    and the differential between home and away stats.
    """
    def __init__(self, name, games):
        self.name = name
        self.home = get_stats(filter(lambda x: x.ishome, games))
        self.away = get_stats(filter(lambda x: not x.ishome, games))
        self.total = get_stats(games)
        self.ratio = get_stat_ratio(self.home, self.away)
        self.diff = get_stat_diff(self.home, self.away)

    def __repr__(self):
        return '%s  %s  %s' % (self.name, str(self.ratio), str(self.diff))


class Stats(object):
    """
    An object which contains the points per game, points allowed per game,
    and spread per game for a set of games
    """
    def __init__(self, ppg, papg, spg, winrating):
        self.ppg = ppg
        self.papg = papg
        self.spg = spg
        self.winrating = winrating

    def __repr__(self):
        return ('%1.3f,%1.3f,%1.3f,%1.3f' %
                (self.ppg, self.papg, self.spg, self.winrating))


def get_team_dict(filename):
    """
    Given a game file, creates a dictionary mapping a team's name to
    a list of the games they played.
    """
    games = read_game_file(filename)

    team_dict = defaultdict(list)
    for game in games:
        team_dict[game.team].append(game)
    return team_dict


def get_stats(games):
    """
    Given a list of games, returns points per game, points allowed per game,
    and spread per game
    """
    spread = 0.0
    pts = 0.0
    ptsallowed = 0.0
    wins = 0.0
    for game in games:
        pts += game.pts
        ptsallowed += game.ptsallowed
        spread += game.pts - game.ptsallowed
        if game.pts > game.ptsallowed:
            wins += 1.0
    return Stats(pts/len(games), ptsallowed/len(games),
                 spread/len(games), wins/len(games))


def get_stat_ratio(homestats, awaystats):
    """
    Returns the ratio of two sets of Stats as a Stats object.
    There are +delta's everywhere to avoid dividing by zero problems.
    I don't look at the ratio of home spread per game vs away spread per game
    because I can't think of a great way to avoid division by zero.
    """
    delta = 0.00001
    ppg_ratio = (homestats.ppg+delta) / (awaystats.ppg+delta)
    papg_ratio = (homestats.papg+delta) / (awaystats.papg+delta)
    spg_ratio = 0
    winrating_ratio = (homestats.winrating+delta) / (awaystats.winrating+delta)
    return Stats(ppg_ratio, papg_ratio, spg_ratio, winrating_ratio)


def get_stat_diff(homestats, awaystats):
    ppg_diff = homestats.ppg - awaystats.ppg
    papg_diff = homestats.papg - awaystats.papg
    spg_diff = homestats.spg - awaystats.spg
    winrating_diff = homestats.winrating - awaystats.winrating
    return Stats(ppg_diff, papg_diff, spg_diff, winrating_diff)


def examine_ppg(team_stats, n):
    team_stats_filtered = filter(
        lambda x: x.home.ppg > x.away.ppg, team_stats)
    team_stats_filtered.sort(key=lambda x: x.home.ppg, reverse=True)
    for team in team_stats_filtered[0:n]:
        print team.name, team.home.ppg, team.away.ppg


def examine_papg(team_stats, n):
    team_stats_filtered = filter(
        lambda x: x.home.papg < x.away.papg, team_stats)
    team_stats_filtered.sort(key=lambda x: x.home.papg)
    for team in team_stats_filtered[0:n]:
        print team.name, team.home.papg, team.away.papg


def examine_spg(team_stats, n):
    team_stats_filtered = filter(
        lambda x: x.home.spg > x.away.spg, team_stats)
    team_stats_filtered.sort(key=lambda x: x.home.spg, reverse=True)
    for team in team_stats_filtered[0:n]:
        print team.name, team.home.spg, team.away.spg


def examine_winrating(team_stats, n):
    team_stats_filtered = filter(
        lambda x: x.home.winrating > x.away.winrating, team_stats)
    team_stats_filtered.sort(key=lambda x: x.home.winrating, reverse=True)
    for team in team_stats_filtered[0:n]:
        print team.name, team.home.winrating, team.away.winrating


def examine_ppgratio(team_stats, n):
    team_stats_filtered = filter(
        lambda x: x.home.ppg > x.away.ppg, team_stats)
    team_stats_filtered.sort(key=lambda x: x.ratio.ppg, reverse=True)
    for team in team_stats_filtered[0:n]:
        print team.name, team.ratio.ppg


def examine_papgratio(team_stats, n):
    team_stats_filtered = filter(
        lambda x: x.home.papg < x.away.papg, team_stats)
    team_stats_filtered.sort(key=lambda x: x.ratio.papg)
    for team in team_stats_filtered[0:n]:
        print team.name, team.ratio.papg


def examine_winratingratio(team_stats, n):
    team_stats_filtered = filter(
        lambda x: x.home.winrating > x.away.winrating, team_stats)
    team_stats_filtered.sort(key=lambda x: x.ratio.winrating, reverse=True)
    for team in team_stats_filtered[0:n]:
        print team.name, team.ratio.winrating


def examine_ppgdiff(team_stats, n):
    team_stats_filtered = filter(
        lambda x: x.home.ppg > x.away.ppg, team_stats)
    team_stats_filtered.sort(key=lambda x: x.diff.ppg, reverse=True)
    for team in team_stats_filtered[0:n]:
        print team.name, team.diff.ppg


def examine_papgdiff(team_stats, n):
    team_stats_filtered = filter(
        lambda x: x.home.papg < x.away.papg, team_stats)
    team_stats_filtered.sort(key=lambda x: x.diff.papg)
    for team in team_stats_filtered[0:n]:
        print team.name, team.diff.papg


def examine_spgdiff(team_stats, n):
    team_stats_filtered = filter(
        lambda x: x.home.spg > x.away.spg, team_stats)
    team_stats_filtered.sort(key=lambda x: x.diff.spg, reverse=True)
    for team in team_stats_filtered[0:n]:
        print team.name, team.diff.spg


def examine_winratingdiff(team_stats, n):
    team_stats_filtered = filter(
        lambda x: x.home.winrating > x.away.winrating, team_stats)
    team_stats_filtered.sort(key=lambda x: x.diff.winrating, reverse=True)
    for team in team_stats_filtered[0:n]:
        print team.name, team.diff.winrating


if __name__ == '__main__':
    func, years, n = sys.argv[1], sys.argv[2], int(sys.argv[3])
    team_dict = get_team_dict('games/games_%s.csv' % years)
    team_stats = [Team(team, team_dict[team]) for team in team_dict]

    if func == 'ppg':
        examine_ppg(team_stats, n)
    elif func == 'papg':
        examine_papg(team_stats, n)
    elif func == 'spg':
        examine_spg(team_stats, n)
    elif func == 'winrating':
        examine_winrating(team_stats, n)
    elif func == 'ppgratio':
        examine_ppgratio(team_stats, n)
    elif func == 'papgratio':
        examine_papgratio(team_stats, n)
    elif func == 'winratingratio':
        examine_winratingratio(team_stats, n)
    elif func == 'ppgdiff':
        examine_ppgdiff(team_stats, n)
    elif func == 'papgdiff':
        examine_papgdiff(team_stats, n)
    elif func == 'spgdiff':
        examine_spgdiff(team_stats, n)
    elif func == 'winratingdiff':
        examine_winratingdiff(team_stats, n)
