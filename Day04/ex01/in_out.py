def square(x: int | float) -> int | float:
    """Returns the square of the argument."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Returns the argument raised to the power of itself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """ Returns a closure that applies the function to x repeatedly."""
    count = x

    def inner() -> float:
        # We need to modify 'count' which lives in the 'outer' scope.
        # 'nonlocal' allows us to write to that variable.
        nonlocal count

        # Apply the function to the current value of count
        count = function(count)

        return count

    return inner
