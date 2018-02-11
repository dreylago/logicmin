from logicmin.sol import Sol

# minimization solution to multiple outputs

class MultiSol:

	def __init__(self ):
		self.sols = []

	def add(self, sol):
		self.sols.append(sol)

	def ynamesGen(self):
		ynames = []
		for j in range(len(self.sols)-1,-1,-1):
			ynames.append("y%d"%(j))
		return ynames

	def printInfo(self, ynames=None):
		Y_MAX_VARS = len(self.sols)
		if (ynames is None):
			ynames = self.ynamesGen()

		o = ''
		sep = ""
		for j in range(Y_MAX_VARS):
				o += sep + self.sols[j].printInfo(ynames[Y_MAX_VARS-j-1])
				sep = "\n"
		return o
	
	def printN(self, xnames=None, ynames=None, syntax=None, info=False):
		Y_MAX_VARS = len(self.sols)
		if (ynames is None):
			ynames = self.ynamesGen()

		o = ''
		sep = ""
		for j in range(Y_MAX_VARS):
			o += sep + self.sols[j].printSol(ynames[Y_MAX_VARS-j-1],xnames,syntax)
			sep = "\n"
		
		if info:
			o += sep + self.printInfo(ynames) 
			sep = "\n"
		return o

	def __str__(self):
		return self.printN()

	def __len__(self):
		return len(self.sols)

	def __getitem__(self,j):
		return self.sols[j]