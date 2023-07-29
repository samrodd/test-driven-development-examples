# Step 1: write test case to define the expected behavior of the factiorial function using unittest framework from Python
import unittest

# Step 3 write code 
# Define the factorial function
def factorial(n):
    # base case of n = 0 or n = 1 return 1
    if n == 0 or n == 1:
        return 1
    # additional cases where n > 1
    else:
        return n * factorial(n - 1)

# Step 2: define the test class and cases 
# Define the test class
class TestFactorial(unittest.TestCase):
    # Define test method within test class
    def test_factorial_0(self):
        # Define an assertion that calling factorial with argument 0 equals the expected result of 1. 
        # If the result matches the expected value, the test passes, otherwise it fails
        self.assertEqual(factorial(0), 1)

    def test_factorial_1(self):
        self.assertEqual(factorial(1), 1)
    
    def test_factorial_5(self):
        self.assertEqual(factorial(5), 120)
    
    def test_factorial_10(self):
        self.assertEqual(factorial(10), 3628800)

if __name__ == '__main__':
    unittest.main()
