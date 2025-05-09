class User:
    def __init__(self, nick, name, points):
        self.nick = nick
        self.name = name
        self.points = points

    def add_points(self, poinst):
        self.points = poinst

    def get_points(self):
        return self.points
    
    def get_name(self):
        return self.name

