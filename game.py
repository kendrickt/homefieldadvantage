class Game(object):
    def __init__(self, year, week, team, ishome, pts, ptsallowed):
        self.year = year
        self.week = week
        self.team = team
        self.ishome = ishome
        self.pts = pts
        self.ptsallowed = ptsallowed

    def __repr__(self):
        return '%d,%s,%d,%d' % (self.year, self.team, self.ishome, self.week)
