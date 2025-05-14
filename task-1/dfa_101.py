class DFA:
    def __init__(self):
        # Define states
        # q0: Initial state
        # q1: Seen "1"
        # q2: Seen "10"
        # q3: Seen "101" (accepting state)
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.alphabet = {'0', '1'}
        self.transition = {
            'q0': {'0': 'q0', '1': 'q1'},
            'q1': {'0': 'q2', '1': 'q1'},
            'q2': {'0': 'q0', '1': 'q3'},
            'q3': {'0': 'q3', '1': 'q3'}  # Once in accepting state, stay there
        }
        self.start_state = 'q0'
        self.accept_states = {'q3'}
    
    def process_string(self, input_string):
        """
        Process the input string and determine if it's accepted by the DFA.
        Args: input_string: A string of '0's and '1's
        Returns: bool: True if the string is accepted, False otherwise
        """
        current_state = self.start_state
        
        for symbol in input_string:
            if symbol not in self.alphabet:
                raise ValueError(f"Invalid symbol '{symbol}' in input string")
            
            current_state = self.transition[current_state][symbol]
        
        return current_state in self.accept_states


def main():
    dfa = DFA()
    
    # Print DFA information
    print("DFA that accepts binary strings containing the substring '101'")
    
    # Test cases
    test_cases = [
        "101",      # accept
        "0101",     # accept
        "1010",     # accept
        "01010",    # accept
        "111101",   # accept
        "00101011", # accept
        "",         # reject
        "0",        # reject
        "1",        # reject
        "010",      # reject
        "1001",     # reject
        "11",       # reject
        "00"        # reject
    ]
    
    print("Test Results:")
    print("-" * 50)
    print("String\t|\tAccepted?")
    print("-" * 50)
    
    for test in test_cases:
        result = dfa.process_string(test)
        print(f"'{test}'\t|\t{'Yes' if result else 'No'}")


if __name__ == "__main__":
    main()