### Task

Design a Turing Machine that recognizes the language L = {binary numbers divisible by 3}

### Description

This project implements a Turing Machine that determines whether a binary number is divisible by 3. The machine works by tracking the remainder of the number modulo 3 as it processes each bit from left to right.

The Turing Machine has three states:
- q0: remainder 0 (accepting state)
- q1: remainder 1
- q2: remainder 2

### Implementation Details

The Turing Machine uses the following transition rules:
- From state q0 (remainder 0):
  - Reading 0: Stay in q0 (0 × 2 + 0 = 0 mod 3)
  - Reading 1: Go to q1 (0 × 2 + 1 = 1 mod 3)
- From state q1 (remainder 1):
  - Reading 0: Go to q2 (1 × 2 + 0 = 2 mod 3)
  - Reading 1: Go to q0 (1 × 2 + 1 = 3 mod 3 = 0)
- From state q2 (remainder 2):
  - Reading 0: Go to q1 (2 × 2 + 0 = 4 mod 3 = 1)
  - Reading 1: Stay in q2 (2 × 2 + 1 = 5 mod 3 = 2)
The machine accepts if it ends in state q0, meaning the number is divisible by 3.

### Files

- `tm_div_by_3.py`: Contains the Turing Machine implementation
- `test_tm_div_by_3.py`: Contains unit tests for the Turing Machine
- `requirements.txt` : Project dependencies
- `README.md` : This documentation file

### How to Run the Code

Running the Main Program:
```bash
python tm_div_by_3.py
```

Run the unit tests:
```bash
python test_tm_div_by_3.py
```
