#!/usr/bin/env python
# encoding: UTF-8

from logicmin.tt import TT
from logicmin.sol import Sol
from timeit import default_timer as timer

def main():
	t = TT(4,6);

	t.addRow("0000","--11-1")
	t.addRow("0001","100110")
	t.addRow("0010","101101")
	t.addRow("0011","000010")
	t.addRow("0100","110110")
	t.addRow("0101","000101")
	t.addRow("0110","1-11-1")
	t.addRow("0111","1-10-1")
	t.addRow("1000","1-11-1")
	t.addRow("1001","110110")
	t.addRow("1010","111111")
	t.addRow("1011","110110")
	t.addRow("1100","101111")
	t.addRow("1101","101101")
	t.addRow("1110","101110")
	t.addRow("1111","011111")

	start = timer()
	sols = t.Solve()
	end = timer()

	Sol.printN(sols)

	print "Solved in %f s." % (end-start)

if __name__ == "__main__":
    main()
