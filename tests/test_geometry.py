import math
import unittest

import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    """Проверяет корректность вычисления площади и периметра круга."""

    def test_area_for_various_radii(self):
        cases = [
            (2, math.pi * 4),            # положительное число
            (1, math.pi),                # граничный случай единицы
            (0, 0),                      # нулевой радиус
            (12.5, math.pi * 156.25),    # дробное и крупное значение
        ]
        for radius, expected in cases:
            with self.subTest(radius=radius):
                self.assertAlmostEqual(circle.area(radius), expected, places=6)

    def test_perimeter_for_various_radii(self):
        cases = [
            (3, 6 * math.pi),            # положительное число
            (1, 2 * math.pi),            # граничный случай единицы
            (0, 0),                      # нулевой радиус
            (20.2, 40.4 * math.pi),      # дробное и крупное значение
        ]
        for radius, expected in cases:
            with self.subTest(radius=radius):
                self.assertAlmostEqual(circle.perimeter(radius), expected, places=6)


class SquareTestCase(unittest.TestCase):
    """Проверяет корректность вычисления площади и периметра квадрата."""

    def test_area_supports_boundary_and_large(self):
        cases = [
            (5, 25),          # обычное положительное
            (1, 1),           # граничный случай
            (0, 0),           # нулевая длина
            (15.5, 240.25),   # дробное и крупное значение
        ]
        for side, expected in cases:
            with self.subTest(side=side):
                self.assertEqual(square.area(side), expected)

    def test_perimeter_supports_boundary_and_large(self):
        cases = [
            (4, 16),          # обычное положительное
            (1, 4),           # граничный случай
            (0, 0),           # нулевая длина
            (22.75, 91.0),    # дробное и крупное значение
        ]
        for side, expected in cases:
            with self.subTest(side=side):
                self.assertEqual(square.perimeter(side), expected)


class RectangleTestCase(unittest.TestCase):
    """Проверяет корректность вычисления площади и периметра прямоугольника."""

    def test_area_mixes_zero_fraction_and_large(self):
        cases = [
            ((3, 7), 21),             # положительные стороны
            ((1, 9), 9),              # граничный случай единицы
            ((0, 4.5), 0),            # нулевая сторона
            ((12.5, 8.4), 105.0),     # дробные значения
        ]
        for (a, b), expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(rectangle.area(a, b), expected)

    def test_perimeter_mixes_zero_fraction_and_large(self):
        cases = [
            ((3, 7), 20),             # положительные стороны
            ((1, 6), 14),             # граничный случай единицы
            ((0, 10), 20),            # нулевая сторона
            ((15.5, 9.25), 49.5),     # дробные значения
        ]
        for (a, b), expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(rectangle.perimeter(a, b), expected)


class TriangleTestCase(unittest.TestCase):
    """Проверяет корректность вычисления площади и периметра треугольника."""

    def test_area_covers_zero_unit_and_fraction(self):
        cases = [
            ((6, 4), 12),          # обычные положительные значения
            ((1, 1), 0.5),         # граничные единицы
            ((0, 9), 0),           # нулевое основание
            ((7.2, 5.5), 19.8),    # дробные значения
        ]
        for (base, height), expected in cases:
            with self.subTest(base=base, height=height):
                self.assertEqual(triangle.area(base, height), expected)

    def test_perimeter_covers_zero_unit_and_fraction(self):
        cases = [
            ((3, 4, 5), 12),             # классические положительные стороны
            ((1, 1, 1), 3),              # граничный случай
            ((0, 0, 0), 0),              # нулевые стороны
            ((2.5, 3.75, 4.25), 10.5),   # дробные стороны
        ]
        for (a, b, c), expected in cases:
            with self.subTest(a=a, b=b, c=c):
                self.assertEqual(triangle.perimeter(a, b, c), expected)


if __name__ == "__main__":
    unittest.main()
