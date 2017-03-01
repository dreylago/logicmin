import minterm, logic, random;
from multisol import MultiSol
from sol import Sol
from cube import *

# Truth table
# 
class TT:
	def __init__(self, X_MAX_VARS, Y_MAX_VARS):
		self.lst=[]
		self.X_MAX_VARS=X_MAX_VARS
		self.Y_MAX_VARS=Y_MAX_VARS
		self.mm = []  # list of list of minterms
		self.dc = []  # list of list of don't care

	def setCubeLst(lst):
		self.lst = lst

	def addCubes(self,xc,yc):
		self.lst.append((xc,yc))
	
	def addRow(self, xs, ys):
		xc = CombToCube(xs,self.X_MAX_VARS)
		yc = CombToCube(ys,self.Y_MAX_VARS)
		self.addCubes(xc,yc)	

	def solve(self):
		self.mm = []
		self.dc = []
		sols = MultiSol()
		for j in range(self.Y_MAX_VARS):
			self.mm.append([])
			self.dc.append([])

		for (x,y) in self.lst:
			for j in range(self.Y_MAX_VARS):
				bit = y.BitValue(j)
#				print "x=",x,"x.value=",x.Value(),"y=",y,"j=",j,"bit=",bit
				if  bit == 1:
					self.mm[j].append(x.Value())
				elif bit == -1:
					self.dc[j].append(x.Value())
		
		for j in range(self.Y_MAX_VARS):
			m = self.mm[j]
			dc = self.dc[j]
#				print "j=",j,"m=",m,"dc=",dc
			sols.add(self.Solve1(m,dc))
		return sols

	def Solve1(self, m, dc):
		[Cubes,comps] = logic.prime_implicants(self.X_MAX_VARS,m,dc)
		(Cubes, minimal, iterations) = logic.solve_PIT(Cubes,m)
		return Sol(self.X_MAX_VARS,m,Cubes,comps,minimal,iterations)

	
		


	
	

	
