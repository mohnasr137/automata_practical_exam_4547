import unittest
from tm_div_by_3 import TuringMachine

class TestTuringMachineDivisibleBy3(unittest.TestCase):
    def setUp(self):
        """Set up a new Turing Machine instance for each test."""
        self.tm = TuringMachine()
    
    def test_empty_string(self):
        """Test with empty string (should be treated as 0, which is divisible by 3)."""
        self.assertTrue(self.tm.run(""))
    
    def test_zero(self):
        """Test with binary 0 (decimal 0, divisible by 3)."""
        self.assertTrue(self.tm.run("0"))
    
    def test_one(self):
        """Test with binary 1 (decimal 1, not divisible by 3)."""
        self.assertFalse(self.tm.run("1"))
    
    def test_divisible_by_three(self):
        """Test various binary numbers that are divisible by 3."""
        test_cases = [
            "11",     # 3 in decimal
            "110",    # 6 in decimal
            "1001",   # 9 in decimal
            "1100",   # 12 in decimal
            "1111",   # 15 in decimal
            "10010",  # 18 in decimal
        ]
        
        for test in test_cases:
            with self.subTest(binary=test, decimal=int(test, 2)):
                self.assertTrue(self.tm.run(test), 
                               f"Failed: Binary {test} (Decimal {int(test, 2)}) should be divisible by 3")
    
    def test_not_divisible_by_three(self):
        """Test various binary numbers that are not divisible by 3."""
        test_cases = [
            "1",      # 1 in decimal
            "10",     # 2 in decimal
            "100",    # 4 in decimal
            "101",    # 5 in decimal
            "111",    # 7 in decimal
            "1000",   # 8 in decimal
        ]
        
        for test in test_cases:
            with self.subTest(binary=test, decimal=int(test, 2)):
                self.assertFalse(self.tm.run(test), 
                                f"Failed: Binary {test} (Decimal {int(test, 2)}) should not be divisible by 3")
    
    def test_large_numbers(self):
        """Test with larger binary numbers."""
        # Divisible by 3
        self.assertTrue(self.tm.run("1001001001"))  # 585 in decimal (585 ÷ 3 = 195)
        self.assertFalse(self.tm.run("1010101010"))  # 682 in decimal (682 ÷ 3 = 227 with remainder 1)
        
        # Not divisible by 3
        self.assertFalse(self.tm.run("1010101011"))  # 683 in decimal (683 ÷ 3 = 227 with remainder 2)
        self.assertTrue(self.tm.run("1111111111"))  # 1023 in decimal (1023 ÷ 3 = 341)
    
    def test_mathematical_property(self):
        """Test the mathematical property that a number is divisible by 3 
        if and only if the sum of its digits is divisible by 3."""
        for i in range(100):
            binary = bin(i)[2:]  # Convert to binary and remove '0b' prefix
            decimal = i
            is_divisible = decimal % 3 == 0
            
            with self.subTest(decimal=decimal, binary=binary):
                self.assertEqual(self.tm.run(binary), is_divisible, 
                               f"Failed: Binary {binary} (Decimal {decimal}) divisibility test")

if __name__ == "__main__":
    unittest.main()