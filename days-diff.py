from datetime import date


def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    d1 = date(*date1)
    d2 = date(*date2)
    diff = abs((d1 - d2).days)
    return diff


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
