#!/usr/bin/env python
# encoding: UTF-8

from logicmin.tt import TT
from logicmin.sol import Sol
from timeit import default_timer as timer

def main():
	t = TT(3,3);

	t.addRow("000","1-1")
	t.addRow("001","100")
	t.addRow("010","111")
	t.addRow("011","011")
	t.addRow("100","111")
	t.addRow("101","10-")
	t.addRow("110","111")
	t.addRow("111","011")

	start = timer()
	sols = t.Solve()
	end = timer()

	Sol.printN(sols, info=True)

	print "Solved in %f s." % (end-start)
	

if __name__ == "__main__":
    main()
