def mortal_fibonacci_rabbits(n, m):
    # List to store rabbit pairs of each age (0 to m-1 months)
    rabbits = [0] * m
    rabbits[0] = 1  # Start with 1 newborn pair

    for month in range(1, n):
        # Newborns are produced by rabbits that are not newborn (age 1 to m-1)
        new_borns = sum(rabbits[1:])

        # Shift ages: oldest rabbits die, all others age by one month
        rabbits = [new_borns] + rabbits[:-1]

    # Total rabbit pairs is the sum of all age groups
    return sum(rabbits)