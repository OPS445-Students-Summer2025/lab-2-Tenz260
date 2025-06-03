#!/usr/bin/env python3

import sys

# this is to check if 2 arguments are provided
if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " name age")
    sys.exit()

name = sys.argv[1]
age = sys.argv[2]

# outputting message
print("Hi " + name + ", you are " + age + " years old.")
