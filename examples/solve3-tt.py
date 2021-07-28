#!/usr/bin/env python
# encoding: UTF-8

import logicmin

t = logicmin.TT(4, 3)
t.add("0000", "--1")
t.add("0001", "100")
t.add("0010", "101")
t.add("0011", "000")
t.add("0100", "110")
t.add("0101", "000")
t.add("0110", "1-1")
t.add("0111", "0-1")
t.add("1000", "1-1")
t.add("1001", "110")
t.add("1010", "111")
t.add("1011", "110")
t.add("1100", "101")
t.add("1101", "001")
t.add("1110", "101")
t.add("1111", "011")

sols = t.solve()

print(sols.printN())
