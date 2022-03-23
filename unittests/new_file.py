def add(x, y):
    """Add function"""
    return x + y


def divide(x, y):
    """Divide function"""
    if y == 0:
        raise ValueError('cannot divide number by zero')
    return x / y

