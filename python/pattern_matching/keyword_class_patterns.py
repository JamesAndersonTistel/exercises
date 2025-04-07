"""
"""

import typing


class City(typing.NamedTuple):
    continent: str
    name: str
    country: str


cities = [
    City('Asia', 'Tokyo', 'JP'),
    City('Asia', 'Delhi', 'IN'),
    City('North America', 'Mexico City', 'MX'),
    City('North America', 'New York', 'US'),
    City('South America', 'São Paulo', 'BR'),
]


def match_asian_cities():
    '''
    >>> match_asian_cities()
    [City(continent='Asia', name='Tokyo', country='JP'), City(continent='Asia', name='Delhi', country='IN')]
    '''
    results = []

    for city in cities:
        match city:
            case City(continent='Asia'):
                results.append(city)
    
    return results


def run1():
    print()

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    
