import unittest
from dfa_101 import DFA

class TestDFA101(unittest.TestCase):
    def setUp(self):
        self.dfa = DFA()
    
    def test_accepting_strings(self):
        """Test strings that should be accepted by the DFA."""
        accepting_strings = [
            "101",      # Basic case
            "0101",     # With prefix
            "1010",     # With suffix
            "01010",    # In the middle
            "111101",   # After multiple 1s
            "00101011"  # With prefix and suffix
        ]
        
        for string in accepting_strings:
            self.assertTrue(self.dfa.process_string(string), 
                           f"'{string}' should be accepted")
    
    def test_rejecting_strings(self):
        """Test strings that should be rejected by the DFA."""
        rejecting_strings = [
            "",         # Empty string
            "0",        # Single 0
            "1",        # Single 1
            "010",      # Close but no 101
            "1001",     # No 101
            "00"        # No 101
        ]
        
        for string in rejecting_strings:
            self.assertFalse(self.dfa.process_string(string), 
                            f"'{string}' should be rejected")
    
    def test_invalid_input(self):
        """Test that the DFA raises an error for invalid input."""
        with self.assertRaises(ValueError):
            self.dfa.process_string("10a1")
    
    def test_basic_transition(self):
        """Test the basic state transition for accepting "101"."""
        dfa = self.dfa
        
        # Start in q0
        current = dfa.start_state
        
        # Process "1" -> should be in q1
        current = dfa.transition[current]['1']
        self.assertEqual(current, 'q1')
        
        # Process "0" -> should be in q2
        current = dfa.transition[current]['0']
        self.assertEqual(current, 'q2')
        
        # Process "1" -> should be in q3 (accepting)
        current = dfa.transition[current]['1']
        self.assertEqual(current, 'q3')
        self.assertIn(current, dfa.accept_states)


if __name__ == "__main__":
    unittest.main()