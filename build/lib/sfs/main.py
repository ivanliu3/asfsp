"""
asfsp is a package for calculating common population genetic statistics
from site frequency spectrum (SFS) and operating SFS

Author: Xiaodong Liu  xiaodong.liu@bio.ku.dk
"""
from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
import copy
import sys

# read sfs file, in realSFS/ANGSD format 
#infile = sys.argv[1]
#with open (infile, 'r') as f:
#    content = [line.strip() for line in f][0]

#data = [float(item) for item in content.split()]

#raw_array = np.array(data)

class sfs:
    def __init__ (self,np_array,dimension):
        if isinstance(dimension, int) or len(dimension) == 1: # dimension given as integer OR given as list of 1 element
            self.ndim = 1
            # save as integer
            if isinstance(dimension,int):
                self.dimension = int(dimension)
            else:
                self.dimension = int(dimension[0])
            self.array = np_array
            print("sfs object is created!\nDimension: ",str(list([self.dimension])) )
        elif len(dimension) == 2: # dimension given as list of 2 element
            self.ndim =2
            self.dimension = dimension
            self.array = np.reshape(np_array,(-1,dimension[1]))
            print( "sfs object is created!\nDimension: ", str(self.dimension) )
        else:
            sys.exit("Given dimension was wrong!")

    def plotSfs(self):
        
        #plt.imshow(self.array, cmap='hot', interpolation='nearest')
        ax = sns.heatmap(self.array, linewidth=0.5)
        plt.show()

    def printSfs(self):
        # convert to pandas dataframe and then print
        print (pd.DataFrame(self.array))

    def mask_corner(self):
        sfs = self.array
        if self.ndim == 2:
            n = self.dimension
            sfs[0,0] = 0
            sfs[n[0]-1,n[1]-1] = 0
            self.array = sfs

        if self.ndim ==1 :
            n = self.dimension
            sfs[0] = 0
            sfs[n-1] = 0
            self.aray = sfs

        return self

    def theta_w(self):
        # calculate Watterson's estimator of theta
        if self.ndim != 1:
            sys.exit("Hault! Theta w is only for 1d-sfs")
        n = self.dimension
        obj_ori = copy.deepcopy(self)
        sfs_ori = obj_ori.array
        self.mask_corner()
        sfs_mask = self.array
        S = sum([1/s for s in range(n-1) if s!= 0])
        theta = (np.sum(sfs_mask)/S) / np.sum(sfs_ori)
        print ("Watterson's estimator of theta is: ", theta)
        return  theta

    def pairwiseDiv(self):
        # calculate pairwise nucleotide differences within a population (pi)
        # or between two populations (dxy)
        denom = np.sum(self.array)
        n = self.dimension
        if self.ndim == 1:
            #sys.exit("Only for 1d-sfs")
            S = np.array( [f * (n-1-f) for f in list(range(n))] )
            pihat = np.sum(np.inner( self.array, S) / ((n-1)*(n-2)/2))
        
        elif self.ndim == 2:
            self.mask_corner()
            sfs = self.array
            a1 = np.outer( np.array(range(n[0])), np.ones(n[1]) ) 
            a2 = np.outer( np.ones(n[0]), np.array(range(n[1])) )
            ones = np.outer( np.ones(n[0]), np.ones(n[1]).T )
            n1 = (n[0]-1) * ones
            n2 = (n[1]-1) * ones
            expect = a2* (n1-a1) + a1* (n2-a2)
            d = np.sum(sfs*expect)
            pihat = d/np.prod([x-1 for x in n])
            
        else:
            sys.exit("Hault! Not 1d or 2d SFS")

        print ("Pairwise neuclotide difference is: ", pihat/denom)
        return pihat/denom    

    def hudson_fst (self):
        # calculate Hudson's Fst, based on the R code of fstFrom2dRHELLER.R  by Rasmus Heller
        if self.ndim != 2:
            sys.exit("Hault! Only 2d SFS is supported")
        N1, N2 = self.dimension
        self.mask_corner()
        array = self.array / np.sum(self.array) # masked and normalized by sum
        aMat = np.empty((N1,N2))
        aMat[:] = np.NAN
        aMat_ss = copy.deepcopy(aMat) #aMat_ss = aMat
        baMat = copy.deepcopy(aMat)
        for a1 in range(N1):
            for a2 in range(N2):
                p1 = float(a1/ (N1-1))
                p2 = float(a2/ (N2-1))
                N = (p1-p2) ** 2
                D = p1*(1-p2)+p2*(1-p1)
                aMat[a1,a2] = N
                baMat[a1,a2] = D
                #sample size correction
                N_ss = N-((p1*(1-p1))/(N1-2))-((p2*(1-p2))/(N2-2))
                aMat_ss[a1,a2] = N_ss

        ## sample size corrected moment estimator
        ss = np.sum(array * aMat_ss) / np.sum(array * baMat)
        print ("Hudson's Fst is: ", ss)
        return ss



#s1 = sfs(raw_array,21)
#s1.plotSfs()
#print(s1.dimension)
#s1.printSfs()

#s1.pairwiseDiv() 
#s1.hudson_fst() 
#print(s1.theta_w())
