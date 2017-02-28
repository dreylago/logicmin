from cube import *
from sop import SOP

# Logic minimization solution 

class Sol(SOP):

	def __init__(self, X_MAX_VARS, m, cubes, comps, minimal, iterations):
		SOP.__init__(self,X_MAX_VARS,cubes)
		self.m = m
		self.comps = comps
		self.minimal = minimal
		self.iterations = iterations

	def printSol(self, yname='y', xnames=None, syntax=None):
		s = self.expr(xnames, syntax)
		print "%s <= %s" % (yname, s)

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
		print "Cost minimal: %.1f. Canonical: %.1f (%.1f%%)" % (
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

	