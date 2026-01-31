import math


class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def set_width(self, value):
        self.width = value

    def set_height(self, value):
        self.height = value

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ["*" * self.width] * self.height

        return "\n".join(picture) + "\n"

    def get_amount_inside(self, other: "Rectangle"):
        return round(self.width / other.width) * round(self.height / other.height)

    def __str__(self):
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)

    def set_width(self, value):
        self.set_side(value)

    def set_height(self, value):
        self.set_side(value)

    def set_side(self, value):
        self.height = self.width = value

    def __str__(self):
        return f"{self.__class__.__name__}(side={self.height})"


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

print(Rectangle(15, 10).get_amount_inside(Square(5)))
