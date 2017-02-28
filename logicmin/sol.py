from texpr import *
from cube import *

# Logic minimization solution 
class Sol:

	def __init__(self, X_MAX_VARS, m, cubes, comps, minimal, iterations):
		self.m = m
		self.cubes = cubes
		self.comps = comps
		self.minimal = minimal
		self.iterations = iterations
		self.X_MAX_VARS = X_MAX_VARS

	def printSol(self, f='y', xnames=None, syntax=None):
		if (xnames is None):
			xnames = []
			for j in range(self.X_MAX_VARS-1,-1,-1):
				xnames.append("x%d"%j)
		SOP = None
		if syntax is None:
			SOP = Exp2L(self.cubes, xnames)
		elif syntax=='VHDL':
			SOP = Exp2VHDL(self.cubes, xnames)
		else:
			SOP = Exp2VHDL(self.cubes, xnames)
		print "%s <= %s" % (f, SOP)

	def printInfo(self, fname):
		mincubes = []
		for minterm in self.m:
			cube = minterm_to_cube(minterm,self.X_MAX_VARS)
			mincubes.append(cube)
		canonical_cost = cubes_cost(mincubes)
		min_cost = self.cost()
		r = 100.0 * (min_cost - canonical_cost) / canonical_cost
		s = ''
		s0 = ''
		for c in self.cubes:
			s += s0 + c.Str();
			s0 = ' '
		print '%s: ------------------------' % (fname)
		#print 'minterms: ', self.m;
		#print "Cubes: %s" % (s)	
		print "cost minimal: %.1f cost canonical %.1f (%.1f%%)" % (
			min_cost,canonical_cost,r
		)
		print 'comps:', self.comps, ', iterations:', self.iterations, ', minimal?:', self.minimal;

	@staticmethod
	def printN(sols, xnames=None, ynames=None, syntax=None, info=False):
		Y_MAX_VARS = len(sols)

		if (ynames is None):
			ynames = []
			for j in range(Y_MAX_VARS-1,-1,-1):
				ynames.append("y%d"%(j))

		for j in range(Y_MAX_VARS):
			sols[j].printSol(ynames[Y_MAX_VARS-j-1],xnames,syntax)
		
		if info:
			for j in range(Y_MAX_VARS):
				sols[j].printInfo(ynames[Y_MAX_VARS-j-1])

	def cost(self, gc=1, tc=1):
		return cubes_cost(self.cubes, gc, tc)
	