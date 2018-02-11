#!/usr/bin/env python
# encoding: UTF-8

import logicmin

t = logicmin.TT(4,6);

t.add("0000","--11-1")
t.add("0001","100110")
t.add("0010","101101")
t.add("0011","000010")
t.add("0100","110110")
t.add("0101","000101")
t.add("0110","1-11-1")
t.add("0111","1-10-1")
t.add("1000","1-11-1")
t.add("1001","110110")
t.add("1010","111111")
t.add("1011","110110")
t.add("1100","101111")
t.add("1101","101101")
t.add("1110","101110")
t.add("1111","011111")

sols = t.solve()
print(sols.printN())


