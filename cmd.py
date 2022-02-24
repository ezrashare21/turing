
# cmd 0.2.0
# command line for turingmachine

import turingmachine as turing
import sys, os

mac = turing.machine()

program = "148;2;169;2;1a;2"

def chtoinst(foo):
    th = hex(ord(foo))
    th = th.replace("0x","")
    return "1{};2".format(th)

def asm():
  program = []
  while True:
    inp = input("=> ")
    inps = inp.split(" ")
    if inps[0] == "exit":
      return ";".join(program)
    elif inps[0] == "pchr":
      program.append("00;1{};2".format(inps[1]))
    else:
      print("error")

while True:
    inp = input("> ")
    if "run" == inp:
        mac.program(program,sys.stdout)
    elif "exit" == inp:
        exit()
    elif "printstr" == inp:
        print(";".join(list(map(chtoinst,list(input("string:"))))))
    elif "load" == inp:
        program = open(input("Program ID: ") + ".tg").read()
    elif "save" == inp:
      inp = input("Program ID: ") + ".tg"
      try: open(inp,"w").write(program)
      except: open(inp,"x").write(program)
    elif "remove" == inp:
      try:os.remove(input("Program ID: ") + ".tg")
      except:print("PROGRAM NOT FOUND")
    elif "asm" == inp:
      program = asm()
    elif "list" == inp: print(program)
    else: program = inp
