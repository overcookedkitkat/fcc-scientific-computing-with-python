class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        pattern = ""
        if self.height >= 50 or self.width >= 50:
            return "Too big for picture."
        for _ in range(self.height):
            for _ in range(self.width):
                pattern += "*"
            pattern += '\n'
        return pattern

    def get_amount_inside(self,shape):
        return self.get_area() // shape.get_area()

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)
    
    def set_side(self,side):
        self.width = side
        self.height = side

    def set_width(self,width):
        self.set_height(width)

    def set_height(self,height):
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"
