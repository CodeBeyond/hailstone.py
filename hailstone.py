def hailstone(integer):
    """Integer is the initial number of a hailstone sequence and returns steps it takes to reach 1."""
    counter = 0
    while integer != 1:
        if integer % 2 == 0:
            integer //= 2
        else:
            integer = 3 * integer + 1
        counter += 1
    return counter

