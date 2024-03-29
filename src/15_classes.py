# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class Latlon:
    def __init__(self, lat=0, lon=0):
        self.latitude = lat
        self.longitude = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(Latlon):
    def __init__(self, name='unknown', lat=0, lon=0):
        super().__init__(lat, lon)
        self.name = name
        self.lat = lat
        self.lon = lon
       

    def __str__(self):
        return "<Waypoint '{}' {:f},{}>".format(self.name, self.lat, self.lon)
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name='unknown', difficulty=0, size=0, lat=0, lon=0):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return "<GeoCache '{}' {:f},{} {} {}>".format(self.name, self.difficulty, self.size, self.lat, self.lon)
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint('Catacombs', 41.70505, -121.51521)
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# TODO: finish this
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
# YOUR CODE HERE
geocache = Geocache('Newberry Views', 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
# TODO: finish this
print(geocache)
