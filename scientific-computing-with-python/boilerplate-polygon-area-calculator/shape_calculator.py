class Rectangle:

    # When a Rectangle object is created, it should be initialized with width and height attributes.
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    # Additionally, if an instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10)
    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    # set the width based on the passed argument
    def set_width(self, width):
        self.width = width

    # set the height based on the passed argument
    def set_height(self, height):
        self.height = height

    # Returns area (width * height)
    def get_area(self):
        return (self.width * self.height)

    # Returns perimeter (2 * width + 2 * height)
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    # Returns diagonal ((width ** 2 + height ** 2) ** .5)
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    # Returns a string that represents the shape using lines of "*".
    def get_picture(self):

        # Initialize variable with empty string
        picture = ""
        # If the width or height is larger than 50, this should return the string: "Too big for picture.".
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        # The number of lines should be equal to the height and the number of "*" in each line should be equal to the width.
        # There should be a new line (\n) at the end of each line.
        for i in range(self.height):
            picture += "*" * self.width + "\n"
        return picture

    # Takes another shape (square or rectangle) as an argument. 
    # Returns the number of times the passed in shape could fit inside the shape (with no rotations).
    def get_amount_inside(self, shape):
        return (self.width * self.height) // (shape.width * shape.height)


# The Square class should be a subclass of Rectangle.
class Square(Rectangle):
    
    # When a Square object is created, a single side length is passed in.
    # The __init__ method should store the side length in both the width and height attributes from the Rectangle class.
    def __init__(self, side) -> None:
        self.width = side
        self.height = side

    # If an instance of a Square is represented as a string, it should look like: Square(side=9)
    def __str__(self) -> str:
        return f"Square(side={self.width})"

    # The Square class should be able to access the Rectangle class methods but should also contain a set_side method.
    def set_side(self, side):
        self.width = side
        self.height = side
