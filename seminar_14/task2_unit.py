from test1_doc import chek
import unittest

class TestTriangle(unittest.TestCase):

    def test_triangle_versatile(self):
        self.assertEqual(chek(5,2,4), 'Треугольник является разносторонним.')

    def test_triangle_equilateral(self):
        self.assertEqual(chek(2,2,2), 'Треугольник является равносторонним.')

    def test_triangle_isosceles(self):
        self.assertEqual(chek(2,2,1), 'Треугольник является равнобедренным.')

    def test_value_1(self):
        self.assertRaises(ValueError, chek, -5, 3, 6)

    def test_value_2(self):
        self.assertRaises(ValueError, chek, 5, -3, 6)

    def test_value_3(self):
        self.assertRaises(ValueError, chek, 5, 3, -6)

    def test_value_4(self):
        self.assertRaises(ValueError, chek, 5, 3, 9)

if __name__ == '__main__':
    unittest.main(verbosity=2)
