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
