from cube import *

class Exp2L:

    def __init__( self, Cubes, var_names, SOP=True, POS=False ):
        self.Cubes = Cubes
        self.SOP = SOP and not POS
        self.var_names = var_names
        
    def __str__( self ):
        out = ''
        i = 0
        for c in self.Cubes:
            op = ''
            if i > 0:
                op = [' + ',') ('][not self.SOP]
            out = out + op + c.varstr(self.var_names,sum=not self.SOP)
            i = i + 1
                
        if out == '':
            out = ['0','1'][not self.SOP]
        if not self.SOP and out != '0':
            out = '(' + out + ')'
        return out

	
    def expr_vec( self ):
        out = []
        for c in self.Cubes:
            out.append(c.Str())
        return out

    def invert( self ):
        self.SOP = not self.SOP
        for i in range(len(self.Cubes)):
            self.Cubes[i].invert()

    # pin count
    
    def pc( self ):
        return cubes_cost(self.Cubes)


  
  
class Exp2VHDL (Exp2L):
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


