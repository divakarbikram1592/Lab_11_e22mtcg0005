from Shape import Shape
class Cuboid(Shape):

    def area(self, *args):
        try:
            return str(2*(float(args[0])*float(args[1])+float(args[1])*float(args[2])+float(args[2])*float(args[0])))
        except:
            return "error_in_input"