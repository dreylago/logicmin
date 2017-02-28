from binary import *

def cubes_cost( Cubes, gc=1, tc=1 ):
    cpc = 0
    for c in Cubes:
        cpc = cpc + c.cost(gc,tc)
    mypc = len(Cubes)
    if mypc > 1:
            return cpc + (mypc + 1) * tc + gc # add PCs of the or gate
    elif mypc == 1:
            return cpc  # no or gate
    else:
            return 0 # ??

def minterm_to_cube( MAX_VARS, minterm ):
	t = 0
	f = 0
	mask = 1;
#	print "minterm=",minterm
	for b in range(MAX_VARS):
		if minterm & mask > 0:
			t = t | mask
		else:
			f = f | mask
		mask = mask << 1
	return Cube( MAX_VARS, t, f )

def num_to_cube ( num, MAX_VARS ):
	return minterm_to_cube(MAX_VARS,num)


def equalcubes( C1, C2 ):
	return C1.t == C2.t and C1.f == C2.f



def oneone ( w, MAX_VARS ):
	return countones(w,MAX_VARS)==1

def combinable ( C1, C2 ):
	twordt = C1.t ^ C2.t
	twordf = C1.f ^ C2.f
	return (twordt == twordf) and oneone(twordt,C1.MAX_VARS)

def combine ( C1, C2 ):
	return Cube( C1.MAX_VARS, C1.t & C2.t, C1.f & C2.f )

def CubeExpandRHS( comb, MAX_VARS ):
	return CombToCube(comb,MAX_VARS)
	
def CombToCube( comb, MAX_VARS ):
	vs = list(comb)
	vs.reverse()
	t = 0
	f = 0
	pwr = 1;
	for i in range(MAX_VARS):
		c = vs[i];
		if c=='1':
			t = t + pwr 
		elif c=='0':
			f = f + pwr
		pwr = pwr * 2
	return Cube(MAX_VARS,t,f)


def CubeExpandLHS( comb, MAX_VARS ):
	vs = list(comb)
	vs.reverse()
	lvs = vs.__len__
	i = 0
	pos = []
	for c in vs:
		if (c=='-'):
			pos.append(i);
		i += 1
	
	cnt = len(pos)
	n = 2**cnt
#	print "n=",n," cnt=",cnt," pos=",pos
	cubes = []
	xs = list(vs)
	xb0 = str_to_binary(xs,MAX_VARS)
#	print " xs=",xs," xb0=",xb0
	for w in range(n):
		bb = binary(w,cnt)
		xb = list(xb0)
		for i in range(cnt):
			xb[pos[i]] = bb[i]
#		print " xb=",xb
		minterm = numeric(xb,MAX_VARS)
		cube = minterm_to_cube(MAX_VARS,minterm)
		cubes.append(cube)
	return cubes	

class Cube:
	def __init__(self, MAX_VARS, t=0, f=0):
		self.MAX_VARS = MAX_VARS
		self.t = t
		self.f = f


	def varstr( self, names = (), sum=False):
		out = ""
		lnames = list(names)
		lnames.reverse()
		t = self.t
		f = self.f
		for b in range(self.MAX_VARS):
			name = "X" + str(b)
			if len(lnames)>b:
				name = lnames[b]
			sep = ""
			if out:
				sep = [".","+"][sum==True]
			if t & 1:
				out = name + sep + out
			elif f & 1:
				out = name + "'" + sep + out
			t = t >> 1
			f = f >> 1
		if out == '':
			out = ['1','0'][sum==True]
		return out

	def vhdl( self, names = (), sum=False):
		out = ""
		lnames = list(names)
		lnames.reverse()
		t = self.t
		f = self.f
		for b in range(self.MAX_VARS):
			name = "X" + str(b)
			if len(lnames)>b:
				name = lnames[b]
			sep = ""
			if out:
				sep = [" and "," or "][sum==True]
			if t & 1:
				out = name + sep + out
			elif f & 1:
				out = " not(" + name + ")" + sep + out
			t = t >> 1
			f = f >> 1
		if out == '':
			out = ["'1'","'0'"][sum==True]
		return out

	def __str__( self ):
		return self.Str()


	def Str( self ):
		out = ""
		t = self.t
		f = self.f
		for b in range(self.MAX_VARS):
			if t & 1 and not (f & 1):
				out = "1" + out
			elif f & 1 and not( t & 1):
				out = "0" + out
			elif not (t & 1) and not (f & 1):
				out = "x" + out
			else:
				out = "?" + out
			t = t >> 1
			f = f >> 1
		return out



	def covers( self, minterm ):
		mask = self.t | self.f
		return (minterm & mask == self.t) and \
			   ((~minterm) & mask == self.f)

	def cover_set( self, minterms):
		return filter(self.covers, minterms)


	def cost( self ):
		return countones(self.t,self.MAX_VARS) + \
			   countones(self.f,self.MAX_VARS)

	def input_pin_cnt( self ):
		return countones(self.t,self.MAX_VARS) + \
			   countones(self.f,self.MAX_VARS)

	def pc( self,gc=1,tc=1 ):
		cnt = self.input_pin_cnt();
		if cnt > 1:
			return tc * (cnt + 1) + gc
		elif cnt == 1:
			return 0 # it is a wire
		else:
			return 0

	def cost( self, gc=1, tc=1 ):
		cnt = self.input_pin_cnt();
		if cnt > 1:
			return tc * (cnt + 1) + gc
		elif cnt == 1:
			return 0 # it is a wire
		else:
			return 0


	def invert( self ):
		self.t, self.f = self.f, self.t



	def Value( self ):
		mask = 1 << self.MAX_VARS
		diff = (self.t - (~self.f)) & (~mask)
		tt = diff == 0
		if (tt):
			return self.t
		else:
			return None

	# 0, 1, (dc=-1)
	def BitValue( self, bit ):
		mask = 1 << bit
		mt = mask & self.t
		mf = mask & self.f
		if (mt and not mf):
			return 1
		if (mf and not mt):
			return 0
		return -1
		
	def Expand(self):
		xor = (self.t ^ self.f)
		tt = ~xor
		if (tt==0):
			return [self]
		return None

	def Concat(self,y):
		c = Cube(self.MAX_VARS + y.MAX_VARS)
		c.t = self.t << y.MAX_VARS | y.t
		c.f = self.f << y.MAX_VARS | y.f
		return c

	def Copy(self):
		c = Cube(self.MAX_VARS,self.t,self.f)
		return c
		
