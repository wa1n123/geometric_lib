import math
import unittest

import circle
import rectangle
import square
import triangle


class CircleTests(unittest.TestCase):
    """Проверяет вычисления площади и длины окружности."""

    def test_area_varied_radii(self):
        cases = [
            (1, math.pi),
            (2.5, math.pi * 6.25),
            (0, 0),
            (7, math.pi * 49),
        ]
        for radius, expected in cases:
            with self.subTest(radius=radius):
                self.assertAlmostEqual(circle.area(radius), expected, places=6)

    def test_perimeter_varied_radii(self):
        cases = [
            (1, 2 * math.pi),
            (3, 6 * math.pi),
            (0, 0),
            (5.5, 11 * math.pi),
        ]
        for radius, expected in cases:
            with self.subTest(radius=radius):
                self.assertAlmostEqual(circle.perimeter(radius), expected, places=6)


class SquareTests(unittest.TestCase):
    """Проверяет вычисления площади и периметра квадрата."""

    def test_area_multiple_lengths(self):
        cases = [
            (2, 4),
            (0, 0),
            (9.5, 90.25),
        ]
        for side, expected in cases:
            with self.subTest(side=side):
                self.assertEqual(square.area(side), expected)

    def test_perimeter_multiple_lengths(self):
        cases = [
            (2, 8),
            (0, 0),
            (6.25, 25.0),
        ]
        for side, expected in cases:
            with self.subTest(side=side):
                self.assertEqual(square.perimeter(side), expected)


class RectangleTests(unittest.TestCase):
    """Проверяет вычисления площади и периметра прямоугольника."""

    def test_area_pairs(self):
        cases = [
            ((3, 4), 12),
            ((5.5, 2), 11.0),
            ((0, 10), 0),
        ]
        for (a, b), expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(rectangle.area(a, b), expected)

    def test_perimeter_pairs(self):
        cases = [
            ((3, 4), 14),
            ((7, 1.5), 17.0),
            ((0, 5), 10),
        ]
        for (a, b), expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(rectangle.perimeter(a, b), expected)


class TriangleTests(unittest.TestCase):
    """Проверяет вычисления площади и периметра треугольника."""

    def test_area_combinations(self):
        cases = [
            ((6, 4), 12),
            ((3.5, 8), 14.0),
            ((0, 9), 0),
        ]
        for (base, height), expected in cases:
            with self.subTest(base=base, height=height):
                self.assertEqual(triangle.area(base, height), expected)

    def test_perimeter_combinations(self):
        cases = [
            ((3, 4, 5), 12),
            ((10, 10, 10), 30),
            ((2.5, 3.5, 4.0), 10.0),
        ]
        for (a, b, c), expected in cases:
            with self.subTest(a=a, b=b, c=c):
                self.assertEqual(triangle.perimeter(a, b, c), expected)


if __name__ == "__main__":
    unittest.main()