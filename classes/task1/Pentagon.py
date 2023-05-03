import math

from Shape import Shape
class Pentagon(Shape):

    def area(self, *args):
        try:
            return str((math.sqrt(5*(5+2*math.sqrt(5))) * float(args[0])**2)/4)
        except:
            return "error_in_input"