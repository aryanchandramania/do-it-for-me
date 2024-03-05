def complex_function(x, y):
    if x > 0:
        if y > 0:
            print("Quadrant I")
            print("X and Y are positive")
        else:
            print("Quadrant IV")
            print("X is positive but Y is not")
    elif x < 0:
        if y > 0:
            print("Quadrant II")
            print("X is negative but Y is positive")
        else:
            print("Quadrant III")
            print("Both X and Y are negative")
    else:
        print("Origin")
        print("Both X and Y are zero")