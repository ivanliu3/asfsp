#!/usr/bin/python

import numpy as np
import sys
sys.path.insert(1, '../sfs')
from main import sfs

infile = sys.argv[1]
with open (infile, 'r') as f:
    content = [line.strip() for line in f][0]

data = [float(item) for item in content.split()]
raw_array = np.array(data)
s1 = sfs(raw_array,[10,6])
s1.printSfs()
#s1.plotSfs()
s1.marginalize(pop=2)
print(s1.array)
