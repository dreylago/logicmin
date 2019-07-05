from __future__ import print_function

from fsm import *

class StateAssign:
    def __init__(fsm):
        self.fsm=fsm

    def Run():
        i=0
        done=0
        hist = []
        for k in range(1000):
            hist.append(0)

        while not done:
            done = fsm.NextAssign()
            fsm.Solve()
            solcost = fsm.SolCost(1,0)
            hist[solcost] = hist[solcost] + 1; 
            if solcost < mincost:
                mincost = solcost
                print("i",i,"cost",solcost)
                fsm.PrintSol()
            i = i + 1      
#        
        print("total solutions=",i-1)

        for k in range(1000):
            if hist[k]>0:
                print(k,"=",hist[k])


