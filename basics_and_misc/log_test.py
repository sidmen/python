from logger import *

# file_handler.setLevel(logging.ERROR)


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        # logger.exception('Tried to divide by zero' + str(x) + "/" + str(y))
        logger.error('Tried to divide by zero {} / {}'.format(x, y))
    else:
        return result


num_1 = 10
num_2 = 0

div_result = divide(num_1, num_2)
print(div_result)
