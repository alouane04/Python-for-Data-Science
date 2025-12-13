from typing import Any


def callLimit(limit: int):
    """ Decorator factory that sets a limit on how many
    times a function can be called."""
    count = 0

    def callLimiter(function):

        def limit_function(*args: Any, **kwds: Any):
            # We need to modify 'count' which lives in the 'callLimit' scope.
            nonlocal count

            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter
