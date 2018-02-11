import os
import sys
from past.builtins import execfile

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path + '/..')

def testFile(path):
    print("Testing %s" %(path))
    execfile(path)
    print("***")

examples_dir = dir_path + '/../examples'
testFile(examples_dir+"/full-adder.py")
testFile(examples_dir+"/bcd7seg.py")
testFile(examples_dir+"/solve1-tt.py")
testFile(examples_dir+"/solve2-tt.py")
testFile(examples_dir+"/solve3-tt.py")
testFile(examples_dir+"/solve4-tt.py")
testFile(examples_dir+"/solve5-tt.py")
testFile(examples_dir+"/solve6-tt.py")
testFile(examples_dir+"/counter.py")
assert True


