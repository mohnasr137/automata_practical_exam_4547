# DFA for Binary Strings Containing "101"

This project implements a Deterministic Finite Automaton (DFA) that accepts all binary strings where the substring "101" appears at least once.

## Overview

A Deterministic Finite Automaton (DFA) is a mathematical model used in theoretical computer science for recognizing patterns within input strings. This implementation specifically recognizes binary strings (consisting of only 0s and 1s) that contain the substring "101" at least once.

## DFA Design

The DFA has 4 states:
- q0: Initial state
- q1: Seen "1"
- q2: Seen "10"
- q3: Seen "101" (accepting state)

Once the DFA reaches the accepting state (q3), it remains there regardless of further input.

### State Transition Table

| State | Input 0 | Input 1 | Accepting? |
|-------|---------|---------|------------|
| q0    | q0      | q1      | No         |
| q1    | q2      | q1      | No         |
| q2    | q0      | q3      | No         |
| q3    | q3      | q3      | Yes        |

## Files

- `dfa_101.py`: Main implementation of the DFA
- `test_dfa_101.py`: Unit tests for the DFA
- `requirements.txt` : Project dependencies
- `README.md` : This documentation file

### How to Run the Code

Running the Main Program:
```bash
python dfa_101.py
```
Running the Unit Tests:
```bash
python test_dfa_101.py