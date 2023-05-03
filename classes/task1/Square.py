from Shape import Shape
class Square(Shape):

    def area(self, *args):
        try:
            return str(float(args[0]) * float(args[0]))
        except:
            return "error_in_input"