'''
Data Classes

>>> Coordinate = namedtuple('Coordinate', 'lat lon')
>>> issubclass(Coordinate, tuple)
True
>>> moscow = Coordinate(55.76, 37.62)
>>> moscow
Coordinate(lat=55.76, lon=37.62)
>>> loc = Coordinate(55.76, 37.62)
>>> moscow == loc
True

>>> import typing
>>> Coordinate = typing.NamedTuple('Coordinate',[('lat', float),('lon',float)])
>>> issubclass(Coordinate, tuple)
True
>>> typing.get_type_hints(Coordinate)
{'lat': <class 'float'>, 'lon': <class 'float'>}
'''

from collections import namedtuple
from typing import NamedTuple
from dataclasses import dataclass, field


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




class Coordinate2(NamedTuple):
    """
    >>> moscow = Coordinate2(55.76, 37.62)
    >>> moscow
    55.8°N, 37.6°E
    """
    lat: float
    lon: float

    def __repr__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


@dataclass(frozen=True)
class Coordinate3:
    """
    >>> moscow = Coordinate3(55.76, 37.62)
    >>> moscow
    55.8°N, 37.6°E
    """
    lat: float
    lon: float

    def __repr__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'

def run1():
    City = namedtuple('City', 'name country population coordinates')
    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    print(f"{tokyo}, {tokyo.population}, {tokyo.coordinates}, {tokyo[1]}")
    print(tokyo._fields)
    print(tokyo._asdict())

@dataclass
class ClubMember:
    name: str
    guests: list[str] = field(default_factory=list)

def run2():
    cm = ClubMember('Howdy',['a','b','c'])
    print(cm)


if __name__ == '__main__':
    #import doctest
    #doctest.testmod()

    run2()
