#!/usr/bin/env python
# encoding: UTF-8

import logicmin

t = logicmin.TT(3,3);
t.add("000","1-1")
t.add("001","100")
t.add("010","111")
t.add("011","011")
t.add("100","111")
t.add("101","10-")
t.add("110","111")
t.add("111","011")
sols = t.solve()

print(sols.printN(info=True))

    