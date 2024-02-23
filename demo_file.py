def complex_function(x, y):
    if x > 0:
        if y > 0:
            print("Quadrant I")
        else:
            print("Quadrant IV")
    elif x < 0:
        if y > 0:
            print("Quadrant II")
        else:
            print("Quadrant III")
    else:
        print("Origin")

    # Duplicated code
    if x > 0:
        if y > 0:
            print("X and Y are positive")
        else:
            print("X is positive but Y is not")
    elif x < 0:
        if y > 0:
            print("X is negative but Y is positive")
        else:
            print("Both X and Y are negative")
    else:
        print("Both X and Y are zero")