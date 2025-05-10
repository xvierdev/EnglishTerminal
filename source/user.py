class User:
    def __init__(self, nick, points):
        self.nick = nick
        self.points = points

    def add_points(self, poinst):
        self.points += poinst

    def get_points(self):
        return self.points
    
    def get_nick(self):
        return self.nick

