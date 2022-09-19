from src import square, rectangle, triangle, circle


def test_perimeter_of_rectangle():
    assert rectangle.Rectangle(4, 5).perimeter == 18


def test_perimeter_of_triangle():
    assert triangle.Triangle(3, 4, 5).perimeter == 12


def test_perimeter_of_square():
    assert square.Square(5).perimeter == 20


def test_perimeter_of_circle():
    assert circle.Circle(5).perimeter == 31.42

