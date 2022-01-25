def hailstone(integer):
    counter = 1
    while (int(integer)) > 0:
        print(int(integer))
        if integer > 1:
            if integer % 2 == 0:
                counter += hailstone(integer / 2)
            else:
                counter += hailstone((integer * 3) + 1)
        return counter


print(hailstone(int(10)))
