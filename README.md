# LogicMin: Logic Minimization in Python

Minimize a logic function expressed as a truth table. 

## Usage

### Full-adder

```python
	# full-adder
	# truth table 3 inputs, 2 outputs
	t = TT(3,2);
	# add rows to the truth table (input, ouutput)
	# ci a b  |  s co
	t.addRow("000","00")
	t.addRow("001","10")
	t.addRow("010","10")
	t.addRow("011","01")
	t.addRow("100","10")
	t.addRow("101","01")
	t.addRow("110","01")
	t.addRow("111","11")
	# minimize functions and get
	# solution for analyze and print
	sols = t.solve()
	# print solution mapped to var names (xnames=inputs, ynames=outputs)
	# add debug information
	sols.printN(xnames=['Ci','a','b'], ynames=['s','Co'], info=True)
	print "\nIn VHDL:\n"
	# print solution in VHDL
	sols.printN(xnames=['Ci','a','b'], ynames=['s','Co'], syntax='VHDL')
```

Look into examples/ directory for other samples.


## Install

 	1. git clone or download sources
	2. Install with pip 

```bash
cd /path/to/logicmin
pip install .
````
