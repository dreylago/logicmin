#!/usr/bin/env python
# encoding: UTF-8

import logicmin
from timeit import default_timer as timer

t = logicmin.TT(5,8);

t.addRow("00000","--11-111")
t.addRow("00001","10011011")
t.addRow("00010","10110111")
t.addRow("00011","00001000")
t.addRow("00100","11011001")
t.addRow("00101","00010100")
t.addRow("00110","1-11-11-")
t.addRow("00111","1-10-11-")
t.addRow("01000","1-11-11-")
t.addRow("01001","11011011")
t.addRow("01010","11111101")
t.addRow("01011","11011011")
t.addRow("01100","10111111")
t.addRow("01101","10110110")
t.addRow("01110","10111010")
t.addRow("01111","011111-1")
t.addRow("10000","--11-111")
t.addRow("10001","10011010")
t.addRow("10010","10110110")
t.addRow("10011","00001001")
t.addRow("10100","11011011")
t.addRow("10101","00010100")
t.addRow("10110","1-11----")
t.addRow("10111","1-10----")
t.addRow("11000","1-11-11-")
t.addRow("11001","11011011")
t.addRow("11010","11111111")
t.addRow("11011","11011011")
t.addRow("11100","10111110")
t.addRow("11101","10110111")
t.addRow("11110","10111011")
t.addRow("11111","01111101")

start = timer()
sols = t.solve()
end = timer()
print sols.printN()

print "Solved in %f s." % (end-start)


