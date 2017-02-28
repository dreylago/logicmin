from expr2l import Expr2L
from cube import *

class Expr2VHDL(Expr2L):

	def __str__( self ):
		out = ''
		i = 0
		for c in self.Cubes:
			op = ''
			if i > 0:
				op = [' or ',') and ('][not self.SOP]

			out = out + op + c.vhdl(self.var_names,sum=not self.SOP)
			i = i + 1
	
		if out == '':
			out = ["'0'","'1'"][not self.SOP]
		if not self.SOP and out != '0':
			out = '(' + out + ')'
		return out


