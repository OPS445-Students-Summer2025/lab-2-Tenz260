#!/usr/bin/env python3
# Author: Tenzin Wangyel
# Author ID: 134207232
# Date Created: 2025/06/03

import sys

if len(sys.argv) > 1:
   timer = int(sys.argv[1])
else:
   timer = 3 

while timer != 0:
    print (timer)
    timer = timer - 1
print("blast off!")
