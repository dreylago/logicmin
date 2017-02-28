from cube import *

    
####################################################################

def get_maxterms( MAX_VARS, minterms, dc ):
    used = set(minterms) | set(dc)
    n = 2**MAX_VARS
    maxterms = set(range(n)) - used
    return sorted(maxterms)


##MINIMIZATION#############################################################
# McCLUSKEY
# WAKERLY


def prime_implicants( MAX_VARS, minterms, dc=None ):
    if (dc is None):
        dc = [];
    lminterms = minterms + dc
    NumCubes = [len(lminterms)]
    # print "NumCubes[0] = ", NumCubes[0]
    Cubes = [[]]
    Covered = [[]]
    for j in range(NumCubes[0]):
        Cubes[0].append(minterm_to_cube(MAX_VARS,lminterms[j]))
        Covered[0].append(False)

    comparisons = 0
    for m in range(MAX_VARS):
        # print "m=",m
        NumCubes.append(0)
        Cubes.append([])
        Covered.append([])
        for j in range(NumCubes[m]):
            # print " j=", j
            for k in range(j+1,NumCubes[m]):
                # print "    k=", k," combinable(",Cubes[m][j], ",", Cubes[m][k],")?"
                comparisons = comparisons + 1
                if combinable(Cubes[m][j], Cubes[m][k]):
                    # print "          they are combinable!"
                    Covered[m][j] = True
                    Covered[m][k] = True
                    tmpCube = combine(Cubes[m][j], Cubes[m][k])
                    found = False
                    p = 0
                    while p < NumCubes[m+1] and not found:
                        if equalcubes(Cubes[m+1][p],tmpCube):
                            found = True
                        p = p + 1
                                
                    if not found:
                        # print "          append " , tmpCube
                        NumCubes[m+1] = NumCubes[m+1] + 1
                        Cubes[m+1].append(tmpCube)
                        Covered[m+1].append(False)

    OutCubes = []
    for m in range(MAX_VARS+1):
        for j in range(NumCubes[m]):
            if not Covered[m][j]:
                OutCubes.append(Cubes[m][j])

    return (OutCubes,comparisons)
                

def solve_PIT( Cubes, minterms ):
    # build prime implicant table (PIT)
    # as a sparse matrix
    minimal = True
    multiple = False
    rows = len(Cubes)
    cols = len(minterms)
    PIT = {}
    CFreq = [0] * cols
    Select = [0] * rows
    RemoveR = [0] * rows
    RemoveC = [0] * cols
    
    for r in range(rows):
        for c in range(cols):
            if Cubes[r].covers(minterms[c]):
                PIT[(r,c)] = 1
                # print "r=",r," c=",c

    # marked entries            
    Marked = PIT.keys()
    # print "Marked: ", Marked
        
    # initialization ...

    # prime costs
    Costs = [] * rows
    for r in range(rows):
        Costs.append(Cubes[r].cost()) 

    # columns covered by each row
    
    CCovered = []
    for r in range(rows):
        CCovered.append([])

    # rows covered by each column:
    RCovered = []
    for r in range(cols):
        RCovered.append([])

    import copy
    VMarked = copy.copy(Marked)
    done = False
    iter = 0
    _Selected = []
    _Removed = []
    
    while not done:
        iter = iter + 1
        # print "while: VMarked", VMarked
        # get covering
        
        CFreq = [0] * cols
        for r,c in VMarked:
            CFreq[c] = CFreq[c] + 1
            
        # print "get essencial rows"
        for r,c in VMarked:
            if CFreq[c] == 1:
                Select[r] = True

        # print "Essentials:"
        for r in range(rows):
            if Select[r] and not r in _Selected:
                # print Cubes[r].cover_set(minterms)
                _Selected.append(r)


        # print "count total covered terms"

        Covered = [False] * cols
        for r,c in Marked:
            if Select[r]:
                Covered[c] = True
        cnt = Covered.count(True)
        if Marked == []:
            cnt = cols
        assert cnt <= cols, "cnt ! <= cols"

        if cnt == cols:
            done = True
        else:
            # print "remove essencial rows"
            NMarked = []
            for r,c in VMarked:
                if not Select[r] and not Covered[c]:
                    NMarked.append((r,c))
            VMarked = NMarked


            for r in range(rows):
                CCovered[r] = []
                
            VRows = []
            for r,c in VMarked:
                CCovered[r].append(minterms[c])
                if not r in VRows:
                    VRows.append(r)

            VRows.sort()

            removed = 0

            for t1 in range(len(VRows)):
                for t2 in range(t1+1,len(VRows)):
                    r1 = VRows[t1]
                    r2 = VRows[t2]
                    s12 = set(CCovered[r1]) - set(CCovered[r2]) == set([])
                    s21 = set(CCovered[r2]) - set(CCovered[r1]) == set([])
                    eq = s12 and s21
                    cost12 = Costs[r1] >= Costs[r2]
                    cost21 = Costs[r2] >= Costs[r1]
                    removedf = False
                    if eq and cost12:
                        RemoveR[r1] = True
                        # print "equal rem(%s) (%s)" % (Cubes[r1].cover_set(minterms),
                        #                              Cubes[r2].cover_set(minterms))
                        removedf = True 
                    elif eq and cost21:
                        # print "equal (%s) rem(%s)" % (Cubes[r1].cover_set(minterms),
                        #                              Cubes[r2].cover_set(minterms))
                        RemoveR[r2] = True
                        # print "equal",r2
                        removedf = True 
                    elif s12 and cost12:
                        RemoveR[r1] = True
                        removedf = True 
                    elif s21 and cost21:
                        RemoveR[r2] = True
                        removedf = True 
                    if removedf:
                        removed = removed + 1

            if removed > 0:
                # print "remove ", removed, "dominated row(s)"
                NMarked = []
                for r,c in VMarked:
                    if not RemoveR[r]:
                        NMarked.append((r,c))
                    else:
                        if not r in _Removed:
                            _Removed.append(r)
                            # print "remove ", Cubes[r].cover_set(minterms)
                
                VMarked = NMarked
                # print 'VMarked=', VMarked

            else:
                # print "pick less costly by hand..."
                minimal = False
                
                Pick = []
                for c in range(cols):
                    Pick.append([0,c])

                # count covers
                for c in range(cols):
                    RCovered[c] = []

                VCols = []
                for r,c in VMarked:
                    RCovered[c].append(r)
                    if not c in VCols:
                        VCols.append(c)
                VCols.sort()
                
                for c in VCols:
                    Pick[c][0] = len(RCovered[c])

                Pick.sort()

                # print "Pick=",Pick

                # pick column with less Xs, but >= 2 

                cc = -1
                for c in range(cols):
                    if Pick[c][0] >= 2 and cc < 0:
                        cc = Pick[c][1]
      
                # print "selecting cc=",cc

                rr = -1
                for r in VRows:
                    if PIT.get((r,cc),0) > 0 and rr < 0:
                        rr = r

                # print "seleccing rr=", rr
                
                assert not Select[rr] and not RemoveR[rr], "what? (2)"
                Select[rr] = True



    OutCubes = []
    for r in range(rows):
        if Select[r]:
            OutCubes.append(Cubes[r])
            
    return (OutCubes,minimal,iter)


###### misc ##########

#Binary with fixed length, W.J. van der Laan, 2003/11/05
# Python Cookbook

def tobin(x, count=8):
        """
        Integer to binary
        Count is number of bits
        """
        return "".join(map(lambda y:str((x>>y)&1), range(count-1, -1, -1)))


    
def todec(s):
    count = len(s)
    return sum(map(lambda y: int(s[count-1-y])*(2**y), range(count-1, -1, -1)))
