from Shape import Shape
class Cube(Shape):

    def area(self, *args):
        try:
            return str(6 * (float(args[0])**2))
        except:
            return "error_in_input"