from src import rectangle, triangle, square, circle


def test_area_rectangle():
    assert rectangle.Rectangle(4, 5).area == 20


def test_area_triangle():
    assert triangle.Triangle(3, 4, 5).area == 6


def test_area_square():
    assert square.Square(5).area == 25


def test_area_circle():
    assert circle.Circle(5).area == 157.08