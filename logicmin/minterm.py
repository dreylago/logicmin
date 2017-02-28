import random;

def list_init( MAX_VARS ):
    p = 2 ** MAX_VARS;
    r = [];
    for i in range(p):
        r.append(False);

    return r;


def list_random( MAX_VARS ):
    p = 2 ** MAX_VARS;
    r = [];
    for i in range(p):
        r.append(random.randint(0,1)==1);

    return r;

def list_get( MAX_VARS, i ):
    p = 2 ** MAX_VARS;
    qx = i;
    rx = 0
    r = [];
    while qx > 0:
        q = qx / 2;
        rx = qx % 2;
        qx = q;
        r.append(rx==1);

    return r;


def list_inc( q ):

    c = True;
    r = [];
    for j in range(len(q)):
        r.append(False);
        nextc = q[j] and c;
        r[j] = (q[j] and (not c) ) or ((not q[j]) and c);
        c = nextc;

    return r;


def min_list( q ):

    r = [];
    for j in range(len(q)):
        if q[j]:
            r.append(j);

    return r;

        
            
        
    
