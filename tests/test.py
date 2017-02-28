import os
import sys

sys.path.insert(0, os.path.abspath('..'))

from logicmin.tt import TT
from logicmin.sol import Sol

def bcd7seg():
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
	sols = t.Solve()
	Sol.printN(sols, xnames=['b3','b2','b1','b0'], ynames=['a','b','c','d','e','f','g'])


def fulladder():
	t = TT(3,2);
	# ci a b  |  s co
	t.addRow("000","00")
	t.addRow("001","10")
	t.addRow("010","10")
	t.addRow("011","01")
	t.addRow("100","10")
	t.addRow("101","01")
	t.addRow("110","01")
	t.addRow("111","11")
	sols = t.Solve()
	Sol.printN(sols, xnames=['Ci','a','b'], ynames=['s','Co'], info=True)
	print "In VHDL:"
	Sol.printN(sols, xnames=['Ci','a','b'], ynames=['s','Co'], syntax='VHDL')


def main():
	fulladder()
	bcd7seg()

if __name__ == "__main__":
    main()


