# Logic minimization solution 
# 
from logicmin.expr2l import Expr2L
from logicmin.expr2vhdl import Expr2VHDL
from logicmin.expr2verilog import Expr2Verilog
from logicmin.cube import *

class SOP:

	def __init__(self, X_MAX_VARS, cubes):
		self.cubes = cubes
		self.X_MAX_VARS = X_MAX_VARS

	def expr(self, xnames=None, syntax=None):
		if (xnames is None):
			xnames = []
			for j in range(self.X_MAX_VARS-1,-1,-1):
				xnames.append("x%d"%j)
		SOP = None
		if syntax is None:
			SOP = Expr2L(self.cubes, xnames)
		elif syntax=='VHDL':
			SOP = Expr2VHDL(self.cubes, xnames)
		elif syntax=='Verilog':
			SOP = Expr2Verilog(self.cubes, xnames)
		else:
			SOP = Expr2L(self.cubes, xnames)
		return SOP

	def cost(self, gc=1, tc=1):
		return cubes_cost(self.cubes, gc, tc)
	