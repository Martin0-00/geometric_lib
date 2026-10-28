import unittest
import circle
import square
import rectangle
import triangle

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        res = circle.area(5)
        self.assertEqual(res, 78.53981633974483)

    def test_perimeter(self):
        res = circle.perimeter(5)
        self.assertEqual(res, 31.41592653589793)

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        res = square.area(5)
        self.assertEqual(res, 25)

    def test_perimeter(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)

class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        res = rectangle.area(3, 5)
        self.assertEqual(res, 15)

    def test_perimeter(self):
        res = rectangle.perimeter(3, 5)
        self.assertEqual(res, 16)

class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        res = triangle.area(3, 4)
        self.assertEqual(res, 6.0)

    def test_perimeter(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)

if __name__ == '__main__':
    unittest.main()