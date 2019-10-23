"""
This module is a Python replacement for some of C/C++ limits.h constants.
It's useful for some algorithms where you need to find max or min element
or check if some value exceeds some limits
and you cannot get some existing value as the starting point (because it's unknown at the moment) or it's inconvenient.

P.S. For numbers you should probably use math.inf and -math.inf
"""

class __Maximum:
    """
    The Maximum which is bigger than everything and not equal to anything (including itself). Almost like +Infinity
    """
    def __eq__(self, x):
        return False

    def __ne__(self, x):
        return True

    def __gt__(self, x):
        return True

    def __ge__(self, x):
        return True


maximum = __Maximum()


class __Minimum:
    """
    The Minimum which is smaller than everything and not equal to anything (including itself). Almost like -Infinity
    """
    def __eq__(self, x):
        return False

    def __ne__(self, x):
        return True

    def __lt__(self, x):
        return True

    def __le__(self, x):
        return True


minimum = __Minimum()
