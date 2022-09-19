import sys
from reduction import *
reduction = Reduction()
text = open('finalinput.txt').read()
reduction_ratio = 0.4
newfile=open("finaloutput.txt","w+")
reduced_text = reduction.reduce(text, reduction_ratio)
sys.stdout = newfile
print reduced_text

