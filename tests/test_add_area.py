import pytest

from src import rectangle, triangle, square, circle

rectangle = rectangle.Rectangle(4, 6)
triangle = triangle.Triangle(3, 4, 5)
square = square.Square(5)
circle = circle.Circle(5)

def test_add_area_rt():
    assert rectangle.add_area(triangle), 26

def test_add_area_sc():
    assert square.add_area(circle), 182.08

def test_add_area_rr():
    assert rectangle.add_area(rectangle), 40

def test_add_area_exeption():
    with pytest.raises(ValueError):
        circle.add_area(1)



