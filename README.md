# LogicMin: Logic Minimization in Python

Minimize logic functions

## Usage

### Full-adder

```python
import logicmin

# full-adder
# truth table 3 inputs, 2 outputs

t = logicmin.TT(3,2);

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
# solution for analysis and print
sols = t.solve()

# print solution mapped to var names (xnames=inputs, ynames=outputs)
# add debug information
print sols.printN(xnames=['Ci','a','b'], ynames=['s','Co'], info=True)

# get expression in VHDL syntax
print "\nIn VHDL:\n"
# print solution in VHDL

print sols.printN(xnames=['Ci','a','b'], ynames=['s','Co'], syntax='VHDL')
```

### Binary counter with hold

For finite state machines, use the FSM object. 

```python
import logicmin

# state machine
# state names: e0, e1, e2, e3
# input: x
# output: y

# sequences
# x=0 => hold
# x=1 => binary up count
# y = 1 in states: e1 and e3

# state labels
states = ['e0','e1','e2','e3']

# initializes finite state machine
# state labels: e0, e1, e2, e3
# 2 bits for state codes
# 1 input variable
# 1 output variable
m = logicmin.FSM(states,2,1,1)

# transition table
m.add('0','e0','e0','0')
m.add('1','e0','e1','0')
m.add('0','e1','e1','1')
m.add('1','e1','e2','1')
m.add('0','e2','e2','0')
m.add('1','e2','e3','0')
m.add('0','e3','e3','1')
m.add('1','e3','e0','1')

# assign code to states
codes = {'e0':0,'e1':1,'e2':2,'e3':3}
m.assignCodes(codes)

# solve with D flip-flops
sols = m.solveD()

# print solution with input and output names. 
# in format <inputs,states,flip-flop,outputs>

print sols.printN(xnames=['X','Q1','Q0'], ynames=['D1','D0','Y'])
```

The advantages of FSM objects are 

	1. use symbolic  names for the states 
	2. Decouple code assignment from table initialization.

## Other examples

Look into examples/ directory.

## Install

 	1. git clone or download sources
	2. Install with pip 

```bash
cd /path/to/logicmin
pip install .
````
