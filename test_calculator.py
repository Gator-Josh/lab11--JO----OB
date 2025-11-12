# https://github.com/Gator-Josh/lab11--JO----OB
# Partner 1: Joshua Oliver
# Partner 2: Owen Brooks

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        assert add(1, 17) == 18
        assert add(-1, 67) == 66
        assert add(-5, -10) == -15

    def test_subtract(self): # 3 assertions
        assert subtract(5, 4) == 1
        assert subtract(1, 15) == -14
        assert subtract(-5, -10) == 5
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        assert(mul(3, 5)) == 15
        assert(mul(4, 0)) == 0
        assert(mul(3, -4)) == -12
    #     fill in code

    def test_divide(self): # 3 assertions
        assert(div(2, 10)) == 5
        assert(div(10, -2)) == -0.2
        assert(div(10, 5)) == 0.2
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self): # 3 assertions
        assert logarithm(2, 8) == 3
        assert logarithm(3, 27) == 3
        assert logarithm(4, 64) == 3

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-4, 5)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
    #     fill in code
        assert(hypotenuse(3, 4)) == 5
        assert(hypotenuse(3, -4)) == 5
        self.assertAlmostEqual(hypotenuse(2, 4) , 4.4721359549995793928, 9, "Not Equal")

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-20)
        assert(square_root(9) == 3)

        self.assertAlmostEqual(square_root(20), 4.4721359549995793928, 9, "Not Equal")
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()