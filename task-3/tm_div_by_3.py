class TuringMachine:
    def __init__(self):
        # Define states: q0 (remainder 0), q1 (remainder 1), q2 (remainder 2)
        self.states = {'q0', 'q1', 'q2'}
        self.accept_state = 'q0'  # Accept when remainder is 0
        self.initial_state = 'q0'  # Start with remainder 0
        
        # Define the transition function
        # Format: (current_state, read_symbol): (next_state, write_symbol, move_direction)
        self.transitions = {
            # When in state q0 (remainder 0)
            ('q0', '0'): ('q0', '0', 'R'),  # Reading 0: remain in q0, move right
            ('q0', '1'): ('q1', '1', 'R'),  # Reading 1: go to q1, move right
            
            # When in state q1 (remainder 1)
            ('q1', '0'): ('q2', '0', 'R'),  # Reading 0: go to q2, move right
            ('q1', '1'): ('q0', '1', 'R'),  # Reading 1: go to q0, move right
            
            # When in state q2 (remainder 2)
            ('q2', '0'): ('q1', '0', 'R'),  # Reading 0: go to q1, move right
            ('q2', '1'): ('q2', '1', 'R'),  # Reading 1: remain in q2, move right
        }
    
    def run(self, input_string):
        # Initialize the tape with input and blank symbol at the end
        tape = list(input_string) + ['_']
        
        # Initialize head position and current state
        head_pos = 0
        current_state = self.initial_state
        
        # Run the machine until it halts
        while head_pos < len(tape) - 1:  # Continue until we reach the blank symbol
            # Get current symbol
            current_symbol = tape[head_pos]
            
            # Check if transition exists
            if (current_state, current_symbol) in self.transitions:
                # Get next state, symbol to write, and direction to move
                next_state, write_symbol, move_direction = self.transitions[(current_state, current_symbol)]
                
                # Write symbol
                tape[head_pos] = write_symbol
                
                # Move head
                if move_direction == 'R':
                    head_pos += 1
                elif move_direction == 'L':
                    head_pos -= 1
                
                # Update state
                current_state = next_state
            else:
                # No transition defined, halt
                break
        
        # Check if in accept state
        return current_state == self.accept_state

# Test the Turing Machine
if __name__ == "__main__":
    tm = TuringMachine()
    
    test_cases = [
        "0",      # 0 in decimal, divisible by 3
        "11",     # 3 in decimal, divisible by 3
        "110",    # 6 in decimal, divisible by 3
        "1001",   # 9 in decimal, divisible by 3
        "1",      # 1 in decimal, not divisible by 3
        "10",     # 2 in decimal, not divisible by 3
        "100",    # 4 in decimal, not divisible by 3
        "101",    # 5 in decimal, not divisible by 3
    ]
    
    print("Testing Turing Machine for binary numbers divisible by 3:")
    for test in test_cases:
        result = tm.run(test)
        decimal_value = int(test, 2)
        print(f"Binary: {test}, Decimal: {decimal_value}, Divisible by 3: {result}")