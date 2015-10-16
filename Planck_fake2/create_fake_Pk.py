import numpy as np
import mass_function_library as MFL
import sys,os


def factor(k):
    A = 0.2  #choose its value either above 1 or below 1
    array = np.ones(len(k),dtype=np.float64)
    indexes = np.where((k>0.1) & (k<0.2))[0]
    
    B = (A-1.0)/0.05**2
    array[indexes] = A-B*(k[indexes]-0.15)**2;  del indexes

    return array
        

################################## INPUT #####################################
f_in  = '../CAMB_TABLES/ics_matterpow_99.dat'
f_out = 'fake_Pk2.dat'
##############################################################################

# read the input P(k) file
k_in, Pk_in = np.loadtxt(f_in,unpack=True)

# multiply P(k) by the corresponding factor
Pk_out = Pk_in*factor(k_in)

np.savetxt(f_out,np.transpose([k_in,Pk_out]))
sys.exit()

