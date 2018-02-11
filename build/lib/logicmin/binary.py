def countones( w, MAX_VARS ):
	ones = 0
	for b in range(MAX_VARS):
		if w & 1:
			ones = ones + 1
		w = w >> 1
	return ones

def binary( w, MAX_VARS ):
	b = []
	for x in range(MAX_VARS):
		b.append(w&1)
		w = w >> 1
	return b

def str_to_binary( sb, MAX_VARS ):
	b = []
	for k in range(MAX_VARS):
		bit = 1 if sb[k] == '1' else 0
		b.append(bit)
	return b

def numeric( b, MAX_VARS ):
	w = 0
	pwr = 1;
	for k in range(MAX_VARS):
		w = w + (b[k] & 1) * pwr
		pwr = pwr * 2
	return w

