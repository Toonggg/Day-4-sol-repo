from mpi4py	import MPI	
import numpy as np 

comm = MPI.COMM_WORLD 
rank = comm.Get_rank()  
#print(type(rank)) rank is an int class, so casting to int is difficult 
size = comm.Get_size() 

ranksum = 0 

if rank != 0: 
    comm.send(rank, dest = 0 ) 
else: 
    for nz_rank in range(1, size): 
        ranksum += comm.recv(source = nz_rank) 
    print(ranksum) 
   