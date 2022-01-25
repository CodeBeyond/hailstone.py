def hailstone(integer):
    """Integer is the initial number of a hailstone sequence and returns steps it takes to reach 1."""
    counter = 1
    while (int(integer)) != 1:
        if integer % 2 == 0:
            counter += (integer / 2)
        else:
            counter += ((integer * 3) + 1)
        return counter

    answer = hailstone(10)
    print(answer)
