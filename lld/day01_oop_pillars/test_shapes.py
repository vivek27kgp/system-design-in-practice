import math

import pytest

from lld.day01_oop_pillars.shapes import Circle, Rectangle, Shape, Triangle, total_area


def test_shape_is_abstract():
    with pytest.raises(TypeError):
        Shape()  # type: ignore[abstract]


@pytest.mark.parametrize(
    ("shape", "area", "perimeter"),
    [
        (Circle(1), math.pi, 2 * math.pi),
        (Rectangle(3, 4), 12, 14),
        (Triangle(3, 4, 5), 6, 12),
    ],
)
def test_each_shape_computes_its_own_area_and_perimeter(shape, area, perimeter):
    assert shape.area() == pytest.approx(area)
    assert shape.perimeter() == pytest.approx(perimeter)


def test_total_area_works_for_any_mix_of_shapes():
    assert total_area([Rectangle(1, 1), Rectangle(2, 3)]) == pytest.approx(7)
    assert total_area([]) == 0


def test_describe_is_inherited_by_every_shape():
    assert Rectangle(3, 4).describe() == "Rectangle: area=12.00, perimeter=14.00"


@pytest.mark.parametrize(
    "make_invalid",
    [lambda: Circle(0), lambda: Rectangle(-1, 2), lambda: Triangle(1, 2, 3)],
)
def test_invalid_shapes_are_rejected(make_invalid):
    with pytest.raises(ValueError):
        make_invalid()


def test_shapes_are_value_objects():
    assert Circle(2) == Circle(2)
    assert len({Circle(2), Circle(2), Circle(3)}) == 2  # hashable → usable in sets
    with pytest.raises(AttributeError):
        Circle(2).radius = 5  # frozen → immutable
