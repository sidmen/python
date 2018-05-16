from logger import *


def square(x):
    """Return the square of x.

    >>> square(2)
    4
    >>> square(-2)
    4
    """

    return x * x * x


if __name__ == '__main__':
    import doctest
    doctest.testmod()

try:
    print(square(-2))
    logger.info("doctest completed")
except Error as e:
    logger.error("expression not correct")
    logger.debug("check THIS expression")
