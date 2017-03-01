#!/usr/bin/env python
# encoding: UTF-8

from logicmin.tt import TT

def main():
	t = TT(3,3);
	# a b c  |  x y z
	t.addRow("000","101")
	t.addRow("001","010")
	t.addRow("010","100")
	t.addRow("011","100")
	t.addRow("100","100")
	t.addRow("101","010")
	t.addRow("110","001")
	t.addRow("111","011")
	sols = t.solve()
	sols.printN(xnames=['a','b','c'], ynames=['x','y','z'])

if __name__ == "__main__":
    main()
