class Figure:

    def __init__(self):
        self.area = None
        self.name = ["square", "triangle", "rectangle", "circle"]

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Убедитесь, что это геометрическая фигура")
        return self.area + figure.area



