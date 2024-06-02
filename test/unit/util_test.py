import unittest
import pytest

from app import util


@pytest.mark.unit
class TestUtil(unittest.TestCase):
    def test_convert_to_number_correct_param(self):
        self.assertEqual(4, util.convert_to_number("4"))
        self.assertEqual(0, util.convert_to_number("0"))
        self.assertEqual(0, util.convert_to_number("-0"))
        self.assertEqual(-1, util.convert_to_number("-1"))
        self.assertAlmostEqual(4.0, util.convert_to_number("4.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.convert_to_number("0.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.convert_to_number("-0.0"), delta=0.0000001)
        self.assertAlmostEqual(-1.0, util.convert_to_number("-1.0"), delta=0.0000001)
        self.assertAlmostEqual(1.5, util.convert_to_number("1.5"), delta=0.0000001) # Nuevo

    def test_convert_to_number_invalid_type(self):
        invalid_params = ["", "3.h", "s", None, object(), "abc123"]
        for param in invalid_params:
            with self.subTest(param=param):
                self.assertRaises(TypeError, util.convert_to_number, param)

if __name__ == "__main__":  
    unittest.main()
Archivo de pruebas para calc.py:

python
Copiar código
import pytest
import unittest

from app.calc import Calculator


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))
        self.assertEqual(6, self.calc.add(3, 3))
          
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        
    def test_add_method_fails_with_nan_parameter(self):
        invalid_params = ["2", None, object(), "abc123"]
        for param in invalid_params:
            with self.subTest(param=param):
                self.assertRaises(TypeError, self.calc.add, param, 2)
                self.assertRaises(TypeError, self.calc.add, 2, param)

    def test_divide_method_fails_by_zero(self):
        zero_divisors = [0, -0]
        for divisor in zero_divisors:
            with self.subTest(divisor=divisor):
                self.assertRaises(TypeError, self.calc.divide, 4, divisor)

    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
        self.assertRaises(TypeError, self.calc.multiply, "0", 0)
        self.assertRaises(TypeError, self.calc.multiply, 0, "0")

    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(1, self.calc.power(1, 0))
        self.assertEqual(1, self.calc.power(-1, 0))
        self.assertEqual(-27, self.calc.power(-3, 3))
        self.assertRaises(TypeError, self.calc.power, "0", 0)
        self.assertEqual(0.001, self.calc.power(10, -3))

    def test_substract_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.substract(10, 6))
        self.assertEqual(-2, self.calc.substract(256, 258))
        self.assertEqual(-1, self.calc.substract(-1, 0))
        self.assertEqual(0, self.calc.substract(0, 0))
        self.assertEqual(0, self.calc.substract(0, 0))
        self.assertRaises(TypeError, self.calc.substract, "0", 0)

if __name__ == "__feature_fix_coverage__":  
    unittest.main()
