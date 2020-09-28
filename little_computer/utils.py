"""Various Utility functions and classes."""


def clamp(x, max, min, error=True):
    """Ensure a value is within bounds."""
    if min <= x <= max:
        return x
    else:
        if error:
            raise OverflowError("Value "+str(x)+" is not in bounds "+str(min)+" <= x <= "+str(max))
        else:
            if x > max:
                return max
            else:
                return min
