#!/usr/bin/env python
# encoding: UTF-8

from logicmin.tt import TT

def main():
	t = TT(4,7);
	# b3 b2 b1 b0  | a b c d e f g 
	t.addRow("0000","1111110") 
	t.addRow("0001","0110000") 
	t.addRow("0010","1101101") 
	t.addRow("0011","1111001") 
	t.addRow("0100","0110011") 
	t.addRow("0101","1011011") 
	t.addRow("0110","0011111") 
	t.addRow("0111","1110000") 
	t.addRow("1000","1111111") 
	t.addRow("1001","1110011") 
	t.addRow("1010","-------") 
	t.addRow("1011","-------") 
	t.addRow("1100","-------") 
	t.addRow("1101","-------") 
	t.addRow("1110","-------") 
	t.addRow("1111","-------") 
	sols = t.solve()
	sols.printN( xnames=['b3','b2','b1','b0'], ynames=['a','b','c','d','e','f','g'])


if __name__ == "__main__":
    main()
