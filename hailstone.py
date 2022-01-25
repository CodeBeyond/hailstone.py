def hailstone(integer):
    """Integer is the initial number of a hailstone sequence and returns steps it takes to reach 1."""
    counter = 1
    while (int(integer)) > 0:
        if integer > 1:
            if integer % 2 == 0:
                counter += hailstone(integer / 2)
            else:
                counter += hailstone((integer * 3) + 1)
        return counter