from tt import *

class FSM:
	# list of states
	states = []
	# number of states
	N = 0
	# nimber of bits
	N_BITS = 0
	# state flow table
	t = {}
	# VI_MAX_VARS: number of input variables
	# VO_MAX_VARS: number of output variables
	VI_MAX_VARS=0
	VO_MAX_VARS=0

	assignment_cubes = {}

	# states (list of str): name of the states
	# N_BITS: number of bits of state codes
	# VI_MAX_VARS: number of input variables
	# VO_MAX_VARS: number of output variables
	
	def __init__(self, states, N_BITS, VI_MAX_VARS, VO_MAX_VARS):
		self.states = states
		self.N = len(states)
		self.N_BITS = N_BITS
		self.VI_MAX_VARS=VI_MAX_VARS
		self.VO_MAX_VARS=VO_MAX_VARS

	# adds a row in state table
	# vi: input variables
	# ss: current state
	# nss: next state
	# vo: output variables
	
	def Add(self, vi, ss, nss, vo):
		cubes = CubeExpandLHS(vi, self.VI_MAX_VARS)
		for ci in cubes:
			co = CombToCube(vo,self.VO_MAX_VARS);
			if not ss in self.t:
				self.t[ss] = {}
			self.t[ss][ci] = {'co':co,'nss':nss}

	def Assign(self):
		for ss,h in self.t.iteritems():
			for ci,data in h.iteritems():
				data['sc'] = self.assignment_cubes[ss].Copy()
				data['nsc'] = self.assignment_cubes[data['nss']].Copy()
			
	
	# Assign binary codes to states
	def AssignCodes(self,assignment_codes):
		for ss,code in assignment_codes.iteritems():
#			print "ss=",ss," code=",code
			self.assignment_cubes[ss]=num_to_cube(code,self.N_BITS)

	
	def AssignOneCode(self,symbol,code):
		cube = num_to_cube(code,self.N_BITS)
		self.assignment_cubes[symbol] = cube
			
			
	def AssignmentVector(self,state,vector):
		l = len(vector)
		for i in range(l):
			ss = state[i]
			code = vector[i]
			self.assignment_cubes[ss]=num_to_cube(code,self.N_BITS)
	
	
	def SolveD(self):
		x_max_vars = self.VI_MAX_VARS + self.N_BITS
		y_max_vars = self.VO_MAX_VARS + self.N_BITS # ff-d
#		print "x_max_vars=",x_max_vars,"y_max_vars=",y_max_vars
		tt = TT(x_max_vars,y_max_vars)
		for ss,h in self.t.iteritems():
			for ci, data in h.iteritems():
				xc = ci.Concat(data['sc'])
				yc = data['nsc'].Concat(data['co']) 
#				print "ss=",ss,"xc=",xc,"yc=",yc
				tt.AddRow(xc,yc)
				
		tt.Solve()
		return tt;
	
	def JKCube(self,sc,nsc):
		comb = "";
#		print "JKCube nsc.max_vars",nsc.MAX_VARS
		for i in range(nsc.MAX_VARS):
			if (sc.BitValue(i) == 0 and nsc.BitValue(i) == 0):
				comb = "0-" + comb 	
			elif (sc.BitValue(i) == 0 and nsc.BitValue(i) == 1):
				comb = "1-" + comb 	
			elif (sc.BitValue(i) == 1 and nsc.BitValue(i) == 0):
				comb = "-1" + comb 	
			elif (sc.BitValue(i) == 1 and nsc.BitValue(i) == 1):
				comb = "-0" + comb
			else:
				comb = "--" + comb
#		print "sc",sc,"nsc",nsc,"comb",comb
		return CombToCube(comb,nsc.MAX_VARS*2)

	
	def SolveJK(self):
		x_max_vars = self.VI_MAX_VARS + self.N_BITS
		y_max_vars = self.VO_MAX_VARS + 2 * self.N_BITS # ff-jk
		tt = TT(x_max_vars,y_max_vars)
		for ss,h in self.t.iteritems():
			for ci, data in h.iteritems():
				xc = ci.Concat(data['sc'])
				JKCube = self.JKCube(data['sc'],data['nsc'])
				yc = JKCube.Concat(data['co']) 
#				print "ss=",ss,"xc=",xc,"yc=",yc
				tt.AddRow(xc,yc)
		tt.Solve()
		return tt;

	def StrAssign(self):
		o = ""
		for ss in self.states:
			cube = self.assignment_cubes[ss]
			o = o + '[' + ss + ':'  + str(cube.Value()) + ']'
		return o
	
	def SolveMode(self,mode='D'):
		if mode=='D':
			return self.SolveD()
		if mode=='JK':
			return self.SolveJK()
		return None
		
		
				
