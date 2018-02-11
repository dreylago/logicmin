#!/usr/bin/env python
# encoding: UTF-8

import logicmin

t = logicmin.TT(3,3);
# a b c  |  x y z
t.add("000","101")
t.add("001","010")
t.add("010","100")
t.add("011","100")
t.add("100","100")
t.add("101","010")
t.add("110","001")
t.add("111","011")
sols = t.solve()
print(sols.printN(xnames=['a','b','c'], ynames=['x','y','z']))


