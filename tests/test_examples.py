import os
import sys


sys.path.insert(0, os.path.abspath('..'))

def testFile(path):
    print("Testing %s" %(path))
    execfile(path)
    print("***")

testFile("../examples/full-adder.py")
testFile("../examples/bcd7seg.py")
testFile("../examples/solve1-tt.py")
testFile("../examples/solve2-tt.py")
testFile("../examples/solve3-tt.py")
testFile("../examples/solve4-tt.py")
testFile("../examples/solve5-tt.py")
testFile("../examples/solve6-tt.py")
testFile("../examples/counter.py")


