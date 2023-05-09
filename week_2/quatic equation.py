import math

def solve_cubic(a, b, c, d):
    if a == 0:
        # This is not a cubic equation!\n",
        return None
    # Normalize the equation so that the coefficient of x^3 is 1
    b /= a
    c /= a
    d /= a

    # Calculate the coefficients of the depressed cubic equation
    p = (3 * c - b**2) / 3
    q = (2 * b**3 - 9 * b * c + 27 * d) / 27

    # Calculate the discriminant\n",
    discriminant = q**2 / 4 + p**3 / 27

    if discriminant > 0:

        # There are three real roots\n",
        u = (-q / 2 + math.sqrt(discriminant))**(1/3)
        v = (-q / 2 - math.sqrt(discriminant))**(1/3)
        return [u + v - b / 3]
    elif discriminant == 0:

       # There is one real root\n",
        if q < 0:
            u = -(-q / 2)**(1/3)
        else:
            u = (q / 2)**(1/3)
        return [2 * u - b / 3, -u - b / 3]

    else:
        # There are three distinct real roots
        phi = math.acos(-q / 2 / math.sqrt(-p**3 / 27)) / 3
        r1 = 2 * math.sqrt(-p / 3) * math.cos(phi)
        r2 = 2 * math.sqrt(-p / 3) * math.cos(phi + 2 * math.pi / 3)
        r3 = 2 * math.sqrt(-p / 3) * math.cos(phi - 2 * math.pi / 3)
        return [r1 - b / 3, r2 - b / 3, r3 - b / 3]
