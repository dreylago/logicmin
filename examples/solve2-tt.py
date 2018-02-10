#!/usr/bin/env python
# encoding: UTF-8

import logicmin

t = logicmin.TT(3,3);
t.addRow("000","1-1")
t.addRow("001","100")
t.addRow("010","111")
t.addRow("011","011")
t.addRow("100","111")
t.addRow("101","10-")
t.addRow("110","111")
t.addRow("111","011")
sols = t.solve()

print sols.printN(info=True)

    