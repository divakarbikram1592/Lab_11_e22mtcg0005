from Shape import Shape

import math

class Circle(Shape):

    def area(self, *args):
        try:
            return str(math.pi * (float(args[0])**2))
        except:
            return "error_in_input"