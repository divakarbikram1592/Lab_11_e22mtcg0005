from Shape import Shape
class Rectangle(Shape):

    def area(self, *args):
        try:
            return str(float(args[0]) * float(args[1]))
        except:
            return "error_in_input"