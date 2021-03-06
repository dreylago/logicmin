#!/usr/bin/env python
# encoding: UTF-8

import logicmin
from timeit import default_timer as timer

t = logicmin.TT(6,8);

t.add("000000","--11-111")
t.add("000001","10011011")
t.add("000010","10110111")
t.add("000011","00001000")
t.add("000100","11011001")
t.add("000101","00010110")
t.add("000110","1-11-111")
t.add("000111","1-10-111")
t.add("001000","1-11-111")
t.add("001001","11011011")
t.add("001010","11111101")
t.add("001011","11011011")
t.add("001100","10101011")
t.add("001101","10110110")
t.add("001110","10111010")
t.add("001111","011111-1")
t.add("010000","--11-111")
t.add("010001","10011010")
t.add("010010","10110110")
t.add("010011","00001001")
t.add("010100","11011011")
t.add("010101","00010100")
t.add("010110","1-11----")
t.add("010111","1-10----")
t.add("011000","1-11-11-")
t.add("011001","11011011")
t.add("011010","11111111")
t.add("011011","11011011")
t.add("011100","10111110")
t.add("011101","10110111")
t.add("011110","10111011")
t.add("011111","01111101")
t.add("100000","--11-111")
t.add("100001","10011011")
t.add("100010","10110111")
t.add("100011","00001000")
t.add("100100","11011001")
t.add("100101","00010100")
t.add("100110","1-11-11-")
t.add("100111","1-10-11-")
t.add("101000","1-11-11-")
t.add("101001","11011011")
t.add("101010","11111101")
t.add("101011","11011011")
t.add("101100","10111111")
t.add("101101","10110110")
t.add("101110","10111010")
t.add("101111","011111-1")
t.add("110000","--11-111")
t.add("110001","10011010")
t.add("110010","10110110")
t.add("110011","00001001")
t.add("110100","11011011")
t.add("110101","00010100")
t.add("110110","1-11----")
t.add("110111","1-10----")
t.add("111000","1-11-11-")
t.add("111001","11011011")
t.add("111010","00111111")
t.add("111011","010---11")
t.add("111100","10111110")
t.add("111101","10110111")
t.add("111110","10111111")
t.add("111111","01111101")

start = timer()
sols = t.solve()
end = timer()

print(sols.printN())

print("Solved in %f s." % (end-start))



