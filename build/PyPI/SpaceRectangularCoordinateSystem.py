from typing import Union, List, Dict, Tuple, Set



class Point:
    def __init__(self, X: Union[int, float], Y: Union[int, float], Z: Union[int, float]) -> None:
        self.auth(X, Y, Z)

    def auth(self, X: Union[int, float], Y: Union[int, float], Z: Union[int, float]) -> None:
        if (type(X) != int and type(X) != float) or (type(Y) != int and type(Y) != float) or (type(Z) != int and type(Z) != float): raise TypeError("unsupported operand type(s) for creating a point object: '%s', '%s', '%s'" % (type(X).__name__, type(Y).__name__, type(Z).__name__))
        self.X, self.Y, self.Z = X, Y, Z

    def getCoords(self) -> Tuple[Union[int, float], Union[int, float], Union[int, float]]:
        return (self.X, self.Y, self.Z)

    def moveto(self, X: Union[int, float], Y: Union[int, float], Z: Union[int, float]) -> Tuple[Union[int, float], Union[int, float], Union[int, float]]:
        originalCoord = self.getCoords()
        self.auth(X, Y, Z)
        return (X-originalCoord[0], Y-originalCoord[1], Z-originalCoord[2])

    def shift(self, X: Union[int, float], Y: Union[int, float], Z: Union[int, float]) -> Tuple[Union[int, float], Union[int, float], Union[int, float]]:
        X = X + self.X
        Y = Y + self.Y
        Z = Z + self.Z
        self.auth(X, Y, Z)
        return (X, Y, Z)

    def __str__(self) -> str:
        return "a point at (%s, %s, %s)" % self.getCoords()

    def __sub__(self, other) -> Union[int, float]:
        if type(other) != Point:
            raise TypeError("unsupported operand type(s) for -: 'Point' and '%s'" % type(other).__name__)
        return ((self.X-other.X)**2 + (self.Y-other.Y)**2 + (self.Z-other.Z)**2)**0.5

    def __eq__(self, other) -> bool:
        if type(other) != Point:
            raise TypeError("unsupported operand type(s) for ==: 'Point' and '%s'" % type(other).__name__)
        return True if (self.getCoords() == other.getCoords()) else False


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.auth(start, end)

    def auth(self, start: Point, end: Point) -> None:
        if (type(start) != Point) or (type(end) != Point): raise TypeError("unsupported operand type(s) for creating a line object: '%s' and '%s'" % (type(start).__name__, type(end).__name__))
        if start == end: raise Exception("It is not a line.")
        self.startPoint, self.endPoint = start, end

    def getCoords(self) -> Tuple[Tuple[Union[int, float], Union[int, float], Union[int, float]], Tuple[Union[int, float], Union[int, float], Union[int, float]]]:
        return (self.startPoint.getCoords(), self.endPoint.getCoords())

    def getLength(self, axis: Union[str, None] = None) -> Union[int, float]:
        if not axis:
            return ((self.startPoint.X-self.endPoint.X)**2 + (self.startPoint.Y-self.endPoint.Y)**2 + (self.startPoint.Z-self.endPoint.Z)**2)**0.5
        if axis == "X":
            return self.endPoint.X-self.startPoint.X
        if axis == "Y":
            return self.endPoint.Y-self.startPoint.Y
        if axis == "Z":
            return self.endPoint.Z-self.startPoint.Z
        raise Exception("You can only get the length of the line, X, Y or Z.")

    def __str__(self) -> str:
        return "a line starting at %s, ending at %s" % self.getCoords()


class Cube:
    def __init__(self, start: Point, end: Point) -> None:
        self.auth(start, end)

    def auth(self, start: Point, end: Point) -> None:
        if (type(start) != Point) or (type(end) != Point): raise TypeError("unsupported operand type(s) for creating a cube objetc: '%s' and '%s'" % (type(start).__name__, type(end).__name__))
        startX, startY, startZ = start.getCoords()
        endX, endY, endZ = end.getCoords()
        (startX, endX) = (endX, startX) if (startX > endX) else (startX, endX)
        (startY, endY) = (endY, startY) if (startY > endY) else (startY, endY)
        (startZ, endZ) = (endZ, startZ) if (startZ > endZ) else (startZ, endZ)
        for i in [(startX, endX), (startY, endY), (startZ, endZ)]:
            if i[0] == i[1]: raise Exception("It is not a cube.")
        self.startPoint, self.endPoint = Point(startX, startY, startZ), Point(endX, endY, endZ)

    def getCoords(self) -> Tuple[Tuple[Union[int, float], Union[int, float], Union[int, float]], Tuple[Union[int, float], Union[int, float], Union[int, float]]]:
        return (self.startPoint.getCoords(), self.endPoint.getCoords())

    def getSize(self) -> Tuple[Union[int, float], Union[int, float], Union[int, float]]:
        return (self.endPoint.X-self.startPoint.X, self.endPoint.Y-self.startPoint.Y, self.endPoint.Z-self.startPoint.Z)

    def getLength(self, axis) -> Union[int, float]:
        if axis == "X":
            return self.endPoint.X-self.startPoint.X
        if axis == "Y":
            return self.endPoint.Y-self.startPoint.Y
        if axis == "Z":
            return self.endPoint.Z-self.startPoint.Z
        raise Exception("You can only get the length of X, Y or Z.")

    def getVolume(self) -> Union[int, float]:
        return self.getLength(axis = "X") * self.getLength(axis = "Y") * self.getLength(axis = "Z")

    def __str__(self) -> str:
        return "a cube starting at %s, ending at %s" % self.getCoords()

    def  __contains__(cube, point: Point) -> bool:
        if type(point) != Point:
            raise TypeError("unsupported operand type(s) for in: '%s' and 'Cube'" % point.__class__.__name__)
        return True if ((cube.startPoint.X <= point.X <= cube.endPoint.X) and (cube.startPoint.Y <= point.Y <= cube.endPoint.Y) and (cube.startPoint.Z <= point.Z <= cube.endPoint.Z)) else False

    def __and__(cube1, cube2):
        if type(cube2) != Cube:
            raise TypeError("unsupported operand type(s) for &: 'Cube' and '%s'" % cube2.__class__.__name__)
        minimumBoundingCube = Cube(Point(min(cube1.startPoint.X, cube2.startPoint.X), min(cube1.startPoint.Y, cube2.startPoint.Y), min(cube1.startPoint.Z, cube2.startPoint.Z)), Point(max(cube1.endPoint.X, cube2.endPoint.X), max(cube1.endPoint.Y, cube2.endPoint.Y), max(cube1.endPoint.Z, cube2.endPoint.Z)))
        lengthX = cube1.getLength(axis = "X") + cube2.getLength(axis = "X") - minimumBoundingCube.getLength(axis = "X")
        lengthY = cube1.getLength(axis = "Y") + cube2.getLength(axis = "Y") - minimumBoundingCube.getLength(axis = "Y")
        lengthZ = cube1.getLength(axis = "Z") + cube2.getLength(axis = "Z") - minimumBoundingCube.getLength(axis = "Z")
        if lengthX <= 0 or lengthY <= 0 or lengthZ <= 0:
            return None
        coincideCube = Cube(Point(max(cube1.startPoint.X, cube2.startPoint.X), max(cube1.startPoint.Y, cube2.startPoint.Y), max(cube1.startPoint.Z, cube2.startPoint.Z)), Point(min(cube1.endPoint.X, cube2.endPoint.X), min(cube1.endPoint.Y, cube2.endPoint.Y), min(cube1.endPoint.Z, cube2.endPoint.Z)))
        return coincideCube



if __name__ == "__main__":
    cube = Cube(Point(1, 2, 3), Point(4, 5, 6)) # ?????????????????????
    print(cube) # ?????????????????????
    print(cube.getSize()) # ????????????????????????
    print(cube.getVolume()) # ?????????????????????

    point = Point(2, 3, 4) # ???????????????
    print(point) # ??????????????????
    print(point in cube) # ?????????????????????????????????????????????

    point2 = Point(2, 9, 4) # ??????????????????
    point2.shift(0, -3, 4) # ?????????
    print(point2) # ????????????????????????
    print(point2 in cube) # ?????????????????????????????????????????????

    print(Line(point, point2).getLength()) # ???????????????????????? (????????????????????????)
    print(point - point2) # ???????????????????????? (???????????????????????????)

    cube2 = Cube(Point(-10, 4.9, 3), Point(7, 8, 9)) # ????????????????????????
    print(cube & cube2) # ????????????????????????????????????

