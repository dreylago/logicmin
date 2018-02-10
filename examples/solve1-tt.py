#!/usr/bin/env python
# encoding: UTF-8

import logicmin

t = logicmin.TT(3,3);
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
print sols.printN(xnames=['a','b','c'], ynames=['x','y','z'])


