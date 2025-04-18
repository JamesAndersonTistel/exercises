# playing around with the book Fluent Python by Luciano Ramalho
"""
Utility functions for normalized Unicode string comparison.

Using Normal Form C, case sensitive:

    >>> s1 = 'café'
    >>> s2 = 'cafe\u0301'
    >>> s1 == s2
    False
    >>> nfc_equal(s1, s2)
    True
    >>> nfc_equal('A', 'a')
    False

Using Normal Form C with case folding:

    >>> s3 = 'Straße'
    >>> s4 = 'strasse'
    >>> s3 == s4
    False
    >>> nfc_equal(s3, s4)
    False
    >>> fold_equal(s3, s4)
    True
    >>> fold_equal(s1, s2)
    True
    >>> fold_equal('A', 'a')
    True

"""

from unicodedata import normalize, combining


def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)


def fold_equal(str1, str2):
    return (normalize('NFC', str1).casefold() ==
            normalize('NFC', str2).casefold())


def shave_marks(txt):
    """Remove all diacritic marks

    >>> s5 = 'São Paulo'
    >>> s6 = 'Sao Paulo'
    >>> shave_marks(s5) == s6
    True
    """
    norm_txt = normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt
                     if not combining(c))
    return normalize('NFC', shaved)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
