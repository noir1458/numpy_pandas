"""
@brief      generate a list of sparse matrix with sparsity 0.2
"""

import numpy as np
from scipy import sparse
import time

N = 21407
M = 2013
ell = 100
p = 0.2

def generate_chr_mat():
    # Build a random number generator
    rng = np.random.default_rng(int(time.time()))
    # Randomly determine the total number of True values
    Ntrue = rng.binomial(n=N*M, p=p, size=1)[0]  # 90016776
    print(Ntrue)
    
    # Randomly determine true position
    position_ids = rng.choice(a=N*M, size=Ntrue, replace=False)
    positions = np.unravel_index(position_ids, shape=(N,M))
    # print(positions)
    
    # Build a compressed sparse row matrix with the constructor:
    # csr_matrix((data, (row_ind, col_ind)), [shape=(M, N)])
    result = sparse.csr_matrix((np.ones(shape = Ntrue), positions), shape=(N,M), dtype=np.int8)

    # transform sparse matrix into numpy matrix
    chr_mat = result.todense()
    
    np.savetxt("chr_mat.csv", chr_mat, fmt="%.1u", delimiter=",")
    
    return None

def generate_hash_coefs():
    hash_coefs = np.random.randint(M, N, size=(ell,2), dtype=np.int32)
    np.savetxt("hash_coefs.csv", hash_coefs, fmt="%u", delimiter=",")
    
    return None

def main():
    generate_chr_mat()
    generate_hash_coefs()
    return None

if "__main__" == __name__:
    main()