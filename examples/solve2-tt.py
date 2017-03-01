#!/usr/bin/env python
# encoding: UTF-8

from logicmin.tt import TT

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


	sols = t.solve()

	sols.printN(info=True)

	

if __name__ == "__main__":
    main()
