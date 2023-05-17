#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!

# Checks that the program outputs "0" for an input of "1 * 0"
assert run("1 * 0").output == "0"

# Checks that the program exits successfully for input "5 * 0"
assert run("5 * 0").output == "0" 

print("All tests passed!")



