"""
asfsp caller

Author: Xiaodong Liu
"""

import argparse

parser = argparse.ArgumentParser(description='Process 1d or 2dSFS.')
parser.add_argument('--input','-I', required=True,metavar="FILE",
                    help="Input file for raw SFS of the same format as realSFS")
parser.add_argument('--dim', '-D', required=True,type=str,
                    help="Dimensions for the SFS, e.g., 11 for 1dSFS, 11, 11 for 2dSFS.")
parser.add_argument('--calc', '-C',type=str,
                    help="Calculate required popgen statistics including: Hudson's Fst(fst), dXY(dxy), pi(pi), Watterson's theta(theta)")
parser.add_argument('--oper','-O',type=str,
                    help="Some basic operations on SFS including: marginalize(margin1 or margin2), print(print), plot(plot)")

# convert the argument into dict
args = vars(parser.parse_args()) 
infile = args['input']
args['dim'] = [s.strip() for s in args["dim"].split(",")]
dims = args['dim']
if (args.get('calc')):
    stat = args['calc'].lower()

if (args.get('oper')):
    operation = args['oper'].lower()

### import library ###
import numpy as np
import sys
import os
sys.path.insert(1,os.path.dirname(os.path.abspath(__file__))+'/sfs')
from main import sfs

# parse input and create sfs object
with open (infile, 'r') as f:
    content = [line.strip() for line in f][0]
    data = [float(item) for item in content.split()]

raw_array = np.array(data)
dims_int = list([int(s) for s in dims])
s1 = sfs(raw_array, dims_int)

# caculate the required statistics here
if (args.get('calc')):
    if 'theta' in stat:
        if s1.ndim == 2:
            sys.exit("2dSFS detected! Please marginalize it first")
        s1.theta_w()
    elif 'dxy' in stat:
        s1.pairwiseDiv()
    elif 'pi' in stat:
        if s1.ndim == 2:
            sys.exit("2dSFS detected! Please marginalize it first")
        s1.pairwiseDiv()
    elif 'fst' in stat:
        s1.hudson_fst()
    else:
        sys.exit("Typo or unsupported population genetic statistics!")

# perform required operations on the sfs
if (args.get('oper')):
    if 'plot' in operation:
        s1.plotSfs()
    elif 'print' in operation:
        s1.printSfs()
    elif 'margin1' in operation:
        s1.marginalize(pop=1)
        print(s1.array)
    elif 'margin2' in operation:
        s1.marginalize(pop=2)
        print(s1.array)
    else:   
        sys.exit("Typo or unsupported operations!")
