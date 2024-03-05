def complex_function(x, y):
    quadrant = ""
    sign_message = ""

    if x > 0:
        quadrant = "Quadrant I" if y > 0 else "Quadrant IV"
        sign_message = "X and Y are positive" if y > 0 else "X is positive but Y is not"
    elif x < 0:
        quadrant = "Quadrant II" if y > 0 else "Quadrant III"
        sign_message = "X is negative but Y is positive" if y > 0 else "Both X and Y are negative"
    else:
        quadrant = "Origin"
        sign_message = "Both X and Y are zero"

    print(quadrant)
    print(sign_message)