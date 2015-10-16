import numpy as np
import readsnap


snapshot_fname = 'ics'
fout = 'CAMB.txt'

#read particle positions in #Mpc/h                                        
pos=readsnap.read_block(snapshot_fname,"POS ",parttype=1)/1e3

print np.min(pos[:,0]),np.max(pos[:,0])
print np.min(pos[:,1]),np.max(pos[:,1])
print np.min(pos[:,2]),np.max(pos[:,2])

f=open(fout,'w')
for i in xrange(len(pos)):
    f.write(str(pos[i,0])+' '+str(pos[i,1])+' '+str(pos[i,2])+'\n')
f.close()
