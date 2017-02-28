#!/usr/bin/env python
# encoding: UTF-8

from logicmin.tt import TT
from logicmin.sol import Sol

def main():
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

	print "\nIn VHDL:\n"
	Sol.printN(sols, xnames=['Ci','a','b'], ynames=['s','Co'], syntax='VHDL')

if __name__ == "__main__":
    main()
