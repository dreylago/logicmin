#!/usr/bin/env python
# encoding: UTF-8

from logicmin.tt import TT
from logicmin.sol import Sol
from timeit import default_timer as timer

def main():
	t = TT(4,3);

	t.addRow("0000","--1")
	t.addRow("0001","100")
	t.addRow("0010","101")
	t.addRow("0011","000")
	t.addRow("0100","110")
	t.addRow("0101","000")
	t.addRow("0110","1-1")
	t.addRow("0111","0-1")
	t.addRow("1000","1-1")
	t.addRow("1001","110")
	t.addRow("1010","111")
	t.addRow("1011","110")
	t.addRow("1100","101")
	t.addRow("1101","001")
	t.addRow("1110","101")
	t.addRow("1111","011")

	start = timer()
	sols = t.Solve()
	end = timer()

	Sol.printN(sols)

	print "Solved in %f s." % (end-start)

if __name__ == "__main__":
    main()
