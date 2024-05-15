#!/usr/bin/env python3
"""Here's some documentation"""


class Poisson:
    """And more? Wow I never would have guessed"""

    def __init__(self, data=None, lambtha=1.0):
        """Woah! More documentation!!"""
        self.lambtha = float(lambtha)

        if data == None:
            if lambtha < 1:
                raise ValueError("lambtha must be a positive value")
        else:
            if type(data) != list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                self.lambtha = sum(data) / len(data)
