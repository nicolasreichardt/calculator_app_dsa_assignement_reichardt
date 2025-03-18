import unittest  # Importing Python built-in unittest framework
import math 
from circle import Circle

# First we will run unit tests manually with assert and then with unittest framework

# Creating a circle object with radius 5
circle = Circle(5)

# Test perimeter method
expected_perimeter = 2 * math.pi * 5
# Using 1e-9 to avoid floaing point calculation errors
assert abs(circle.perimeter() - expected_perimeter) < 1e-9, "Perimeter test failed!"

# Test area method
expected_area = math.pi * 5 ** 2
# Using 1e-9 to avoid floaing point calculation errors
assert abs(circle.area() - expected_area) < 1e-9, "Area test failed!"

print("All tests passed!")



# Now we can do it with unittest (following the unittest conventions)

class TestCircle(unittest.TestCase):

    def test_perimeter(self):
        """Test if the perimeter method returns the correct value"""
        circle = Circle(5)
        expected_perimeter = 2 * math.pi * 5
         # Using assertAlmostEqual for the same reason as above (floating point calculations)
        self.assertAlmostEqual(circle.perimeter(), expected_perimeter)

    def test_area(self):
        """Test if the area method returns the correct value"""
        circle = Circle(5)
        expected_area = math.pi * 5 ** 2
         # Using assertAlmostEqual for the same reason as above (floating point calculations)
        self.assertAlmostEqual(circle.area(), expected_area)

if __name__ == '__main__':
    unittest.main()



# Both methods confirm that the methods work well!

