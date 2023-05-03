from Square import Square
from Rectangle import Rectangle
from Circle import Circle
from Cube import Cube
from Cuboid import Cuboid
from Pentagon import Pentagon

square = Square()
rectangle = Rectangle()
circle = Circle()
cube = Cube()
cuboid = Cuboid()
pentagon = Pentagon()


def writeInFile(data):
    f = open("/Users/apple/Documents/Projects-Test/pythonProject/pythonProject/classes/task1/result_E22MTCG0005.txt", "a")
    f.write(data+"\n")
    f.close()

with open("/Users/apple/Documents/Projects-Test/pythonProject/pythonProject/classes/task1/input.txt") as file:
    while line := file.readline():
        extracted_line = line.rstrip()
        print(extracted_line.split())
        splitted_line = extracted_line.split()
        if splitted_line[0] == "Circle":
            result = circle.area(splitted_line[1])
            data = "Circle "+splitted_line[1]+" "+ result
            writeInFile(data)
        elif splitted_line[0] == "Cube":
            result = cube.area(splitted_line[1])
            data = "Cube " + splitted_line[1] + " " + result
            writeInFile(data)
        elif splitted_line[0] == "Square":
            result = square.area(splitted_line[1])
            data = "Square " + splitted_line[1] + " " + result
            writeInFile(data)
        elif splitted_line[0] == "Rectangle":
            result = rectangle.area(splitted_line[1], splitted_line[2])
            data = "Rectangle " + splitted_line[1] +" "+ splitted_line[2]+ " " + result
            writeInFile(data)
        elif splitted_line[0] == "Pentagon":
            result = pentagon.area(splitted_line[1])
            data = "Pentagon " + splitted_line[1] + " " + result
            writeInFile(data)
        elif splitted_line[0] == "Cuboid":
            result = cuboid.area(splitted_line[1], splitted_line[2], splitted_line[3])
            data = "Cuboid " + splitted_line[1]+" "+ splitted_line[2]+" "+ splitted_line[3] + " " + result
            writeInFile(data)
