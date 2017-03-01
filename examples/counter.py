from logicmin.fsm import FSM


def main():
	# state machine
	# x=0 => hold
	# x=1 => binary up count
	# y = 1 in e1 and e3
	states = ['e0','e1','e2','e3']
	m = FSM(states,2,1,1)
	m.add('0','e0','e0','0')
	m.add('1','e0','e1','0')
	m.add('0','e1','e1','1')
	m.add('1','e1','e2','1')
	m.add('0','e2','e2','0')
	m.add('1','e2','e3','0')
	m.add('0','e3','e3','1')
	m.add('1','e3','e0','1')
	codes = {'e0':0,'e1':1,'e2':2,'e3':3}
	m.assignCodes(codes)
	m.assign()
	sols = m.solveD()
	sols.printN(xnames=['X','Q1','Q0'], ynames=['D1','D0','Y'])


if __name__ == "__main__":
    main()


