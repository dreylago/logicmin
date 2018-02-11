# Logic minimization solution 
from logicmin.cube import *
from logicmin.sop import SOP

class Sol(SOP):

	def __init__(self, X_MAX_VARS, m, cubes, comps, minimal, iterations):
		SOP.__init__(self,X_MAX_VARS,cubes)
		self.m = m
		self.comps = comps
		self.minimal = minimal
		self.iterations = iterations

	def printSol(self, yname='y', xnames=None, syntax=None):
		s = self.expr(xnames, syntax)
		return "%s <= %s" % (yname, s)

	def __str__(self):
		return self.printSol()

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
		o = "%s: ------------------------\n" % (fname)
		#print 'minterms: ', self.m;
		#print "Cubes: %s" % (s)	
		o += "Cost minimal: %.1f. Canonical: %.1f (%.1f%%)\n" % (
			min_cost,canonical_cost,r
		)
		o += "Comps: %d. Iterations: %d. Minimal: %s" % (self.comps, self.iterations, self.minimal)
		return o
	

	