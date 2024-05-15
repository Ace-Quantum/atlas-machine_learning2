#!/usr/bin/env python3

class Poisson:
    def __init__(self, data=None, lambtha=1.):

        self.lambtha = float(lambtha)

        if data == None:
            if lambtha < 1:
                raise ValueError('lambtha must be a positive value')
        else:
            if type(data) != list:
                raise TypeError('data must be a list')
            elif len(data) < 2:
                raise ValueError('data must contain multiple values')
            else:
                self.lambtha = sum(data) / len(data)