
# command line for turingmachine

import turingmachine as turing
import sys

mac = turing.machine()

program = "148;2;169;2"

while True:
    inp = input("> ")
    if "run" == inp:
        mac.program(program,sys.stdout)
        sys.stdout.write("\n")
    elif "exit" == inp:
        exit()
    else:
        program = inp
