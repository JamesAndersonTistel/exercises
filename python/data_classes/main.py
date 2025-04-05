'''
Data Classes

>>> Coordinate = namedtuple('Coordinate', 'lat long')
>>> issubclass(Coordinate, tuple)
True
>>> moscow = Coordinate(55.76, 37.62)
>>> moscow
Coordinate(lat=55.76, long=37.62)
>>> loc = Coordinate(55.76, 37.62)
>>> moscow == loc
True
'''

from collections import namedtuple

class Coordinate:
    """
    >>> moscow = Coordinate(55.76, 37.62)
    >>> loc = Coordinate(55.76, 37.62)
    >>> loc == moscow
    False
    >>> # compared object ids!
    """

    def __init__(self, lat: float, long: float):
        self._lat = lat
        self._long = long


if __name__ == '__main__':
    import doctest
    doctest.testmod()
