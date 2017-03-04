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

### Binary counter with hold

For finite state machines, use the FSM object. 

```python
	# state machine
	# x=0 => hold
	# x=1 => binary up count
	# y = 1 in states: e1 and e3
	
	# Finite state machine with 
	# state labels
	states = ['e0','e1','e2','e3']
	# 2 bits for state codes
	# 1 input variable
	# 1 output variable
	m = FSM(states,2,1,1)
	# transition table
	m.add('0','e0','e0','0')
	m.add('1','e0','e1','0')
	m.add('0','e1','e1','1')
	m.add('1','e1','e2','1')
	m.add('0','e2','e2','0')
	m.add('1','e2','e3','0')
	m.add('0','e3','e3','1')
	m.add('1','e3','e0','1')
	# asign code to states
	codes = {'e0':0,'e1':1,'e2':2,'e3':3}
	m.assignCodes(codes)
	# solve with D flip-flops
	sols = m.solveD()
	# print solution with input and output names. 
	# in format <inputs,states,flip-flop,outputs>
	sols.printN(xnames=['X','Q1','Q0'], ynames=['D1','D0','Y'])
```

The advantages of the FSM object are (1) use symbolic 
names for the states (2) Decouple assignment of codes 
from table initialization.

## Other examples

Look into examples/ directory.

## Install

 	1. git clone or download sources
	2. Install with pip 

```bash
	cd /path/to/logicmin
	pip install .
````
