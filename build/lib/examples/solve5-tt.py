#!/usr/bin/env python
# encoding: UTF-8

import logicmin
from timeit import default_timer as timer

t = logicmin.TT(5,8);

t.add("00000","--11-111")
t.add("00001","10011011")
t.add("00010","10110111")
t.add("00011","00001000")
t.add("00100","11011001")
t.add("00101","00010100")
t.add("00110","1-11-11-")
t.add("00111","1-10-11-")
t.add("01000","1-11-11-")
t.add("01001","11011011")
t.add("01010","11111101")
t.add("01011","11011011")
t.add("01100","10111111")
t.add("01101","10110110")
t.add("01110","10111010")
t.add("01111","011111-1")
t.add("10000","--11-111")
t.add("10001","10011010")
t.add("10010","10110110")
t.add("10011","00001001")
t.add("10100","11011011")
t.add("10101","00010100")
t.add("10110","1-11----")
t.add("10111","1-10----")
t.add("11000","1-11-11-")
t.add("11001","11011011")
t.add("11010","11111111")
t.add("11011","11011011")
t.add("11100","10111110")
t.add("11101","10110111")
t.add("11110","10111011")
t.add("11111","01111101")

start = timer()
sols = t.solve()
end = timer()
print(sols.printN())

print("Solved in %f s." % (end-start))


