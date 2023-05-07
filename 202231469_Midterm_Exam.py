import numpy as np 

NUMBER_OF_WORDS  = 21407            # total number of words
NUMBER_OF_SETS   = 2013             # total number of sets
NUMBER_OF_HASHES = 100              # total number of hash functions

# @brief    Jaccard similarity between X and Y
# @param    X: a set  
# @param    Y: a set
def _Jaccard_similarity(X, Y):
    # your code
    sim = np.empty(shape=(1,1))
    tmp = np.concatenate(X,Y)
    print(np.unique(tmp))
    return sim

# @brief    read a characteristic matrix from the file chr_math_path
# @param    chr_mat_path: the CSV file name storing a characteristic matrix
# @param    n: the number of rows
# @param    m: the number of columns
def build_characteristic_matrix(chr_mat_path, n, m):
    # your code
    C_mat = np.empty(shape=(n,m))
    C_mat_csv = np.loadtxt(chr_mat_path,delimiter=',',dtype= np.int32)
    C_mat = C_mat_csv
    return C_mat

# @brief    read a set of hash functions h_k(x) = a_k*x + b_k mod n
# @param    hash_coefs_path: the CSV file name storing (a_k,b_k) 
# @param    ell: the number of hash functions
def build_hash_functions(hash_coefs_path, ell):
    # your code
    H_mat = np.empty(shape=(ell,2))
    H_mat_csv = np.loadtxt(hash_coefs_path,delimiter=',',dtype=np.int32)
    return H_mat

# @brief    compute the support matrix using the set of hash functions
# @param    H_mat: ell x 2 matrix 
#           H_mat = [[a_1,b_1],
#                    [a_2,b_2],
#                     ...
#                    [a_ell,b_ell]]
# @param    n: the number of rows (0, 1, 2, ..., n-1)
# @param    ell: the number of hash functions
def compute_support_matrix(H_mat, n, ell):
    # your code
    M_mat = np.empty(shape=(n,ell),dtype=np.float64) # ell?? dtype ??
    n_array = np.arange(0,n-1).reshape((n-1,1))
    sp_matrix = H_mat[:,0]*n_array + H_mat[:,0]
    M_mat = sp_matrix
    return M_mat

# @brief    compute the signature matrix using C_mat and M_mat
# @param    C_mat: the characteristic matrix
# @param    M_mat: the support matrix
# @param    n: the number of rows in C_mat
# @param    m: the number of columns in C_mat & R_mat
# @param    ell: the number of rows in R_mat
def compute_signature_matrix(C_mat, M_mat, n, m, ell):
    # your code
    R_mat = np.empty(shape=(n,m))
    signature_matrix = np.full((n,m),np.Infinity)
    R_mat = signature_matrix
    for row_idx in range(C_mat.shape[0]):
        for col_idx in range(C_mat.shape[1]):
            if C_mat[row_idx,col_idx] == 0:
                continue
            elif C_mat[row_idx,col_idx] == 1:
                R_mat[row_idx,col_idx] = min(R_mat[row_idx,col_idx],M_mat[row_idx,col_idx])
    return R_mat

# @brief    compute the Jaccard similarity of two given sets: S_alpha and S_beta
# @param    R_mat: the signature matrix
# @param    ell: the number of rows in R_mat
# @param    alpha: the index of a set
# @param    beta: the index of a set
def compute_Jaccard_similarity(R_mat, ell, alpha, beta):
    assert (1 <= alpha) and (ell >= beta) 
    # your code
    S_alpha = np.empty(shape=(1,1))
    S_beta = np.empty(shape=(1,1))
    return _Jaccard_similarity(S_alpha, S_beta)


def main():
    # set the parameters
    n, m, ell = NUMBER_OF_WORDS, NUMBER_OF_SETS, NUMBER_OF_HASHES
    targets = input("Enter your alpha, beta:").split(",")
    alpha, beta = int(targets[0]), int(targets[1])

    # set the file names
    chr_mat_path = "./chr_mat.csv"    
    hash_coefs_path = "./hash_coefs.csv"
    
    """
    your code
    """
    C_mat = build_characteristic_matrix(chr_mat_path,n,m)
    H_mat = build_hash_functions(hash_coefs_path,ell)
    M_mat = compute_support_matrix(H_mat,n,ell)
    R_mat = compute_signature_matrix(C_mat,M_mat,n,m,ell)

    result = compute_Jaccard_similarity(R_mat, ell, alpha, beta)
    print("sim(S_alpha,S_beta) =", result)
    
    return None

if ("__main__" == __name__):
    main()