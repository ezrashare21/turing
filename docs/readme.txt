
--- TuringMachine Instruction Set ---

run programs with turingmachine.machine().program(the_program,sys.stdout)

MemSlot:
0000 - set address to argument provided. - 0adr;
0100 - add 1 to address. -  4;
1000 - subtract 1 from address. - 8;
1100 - set address to value in current slot. - C;

SelSlot:
0001 - set current cell to value - 1val;
0101 - +1 to current cell - 5;
1001 - -1 from current cell - 9;
1101 - set cell to the cell selected - D;

I/O:
0010 - output cell as ASCII - 2;
0110 - output cell as int - 6;
1010 - input cell as ASCII - A;
1110 - input cell as a int and convert to int - E;

Flow:
0011 - restart - 3;
0111 - jnz - 7;
1011 - label - Blid;
1111 - goto - Flid;
