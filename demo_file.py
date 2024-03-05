def complex_function(x, y):
    quadrant = ""
    xy_state = ""

    if x > 0:
        quadrant = "Quadrant I" if y > 0 else "Quadrant IV"
        xy_state = "X and Y are positive" if y > 0 else "X is positive but Y is not"
    elif x < 0:
        quadrant = "Quadrant II" if y > 0 else "Quadrant III"
        xy_state = "X is negative but Y is positive" if y > 0 else "Both X and Y are negative"
    else:
        quadrant = "Origin"
        xy_state = "Both X and Y are zero"

    print(quadrant)
    print(xy_state)