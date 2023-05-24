import numpy as np

NUMBER_OF_WORDS = 21407 # 행의 개수(n)
NUMBER_OF_SETS = 2013 # 열의 개수(m)
NUMBER_OF_HASHES = 100 # hash 함수의 개수(ell) 

def _Jaccard_similarity(X,Y):
    union_XY = np.union1d(X,Y)
    intersection_XY = np.intersect1d(X,Y)
    sim = len(intersection_XY) / len(union_XY)
    return sim


def build_characteristic_matrix(chr_mat_path, n, m): # n:행개수 m:열개수
    # csv파일 내에 이미 (n,m)의 크기를 가지는 matrix가 있다. 따라서 읽기만 하면 된다.
    C_mat = np.genfromtxt(chr_mat_path, delimiter = ",", dtype = np.int8) 
    return C_mat

def build_hash_functions(hash_coefs_path, ell): # ell:hash함수의 개수
    # csv파일 내에 이미 (ell,2)의 크기를 가지는 matrix가 있다. 따라서 읽기만 하면 된다.
    H_mat = np.genfromtxt(hash_coefs_path, delimiter = ",", dtype = np.int32)
    return H_mat

def compute_support_matrix(H_mat, n, ell): # H_mat: hash함수 계수
    Operator = np.vstack((np.arange(0,n), np.ones(n, dtype=np.int32))) # [0 ~ n-1]행렬과 [1이 n개]행렬 세로로 합치기
    """
    Operator = [[0,1,2,...,n-1]
               [1,1,1,...,1]]    <- 1이 n개가 들어있음
    """
    # H_mat은 (100,2), Operator는 (2,n)의 크기로 dot연산 가능. 따라서 결과값은 (100,n)의 크기
    # H_mat은 0번째 열이 1차항의 계수, 1번째 열이 상수항의 계수임.
    # 따라서 0번째 열에 0,1,2,...,n을 곱한 후 상수항을 더한 후 %n연산을 하면 M_mat을 구할 수 있다.
    # 그러므로 np.dot(H_mat,Operator)을 하면 0번째 열에 0,1,2,...,n을 곱한 후 상수항을 더한 값들을 모은 matrix가 나온다.
    # 그런데 그 값들이 열기준으로 나열된 것이 아니라 행기준으로 나열되므로 transpose 시킨다.
    # 그러므로 크기는 (n,100)이 된다. 
    # 그 후 %n연산을 하면 M_mat을 구할 수 있다.
    M_mat = np.transpose(np.dot(H_mat,Operator)) % n 
    return M_mat

def compute_signature_matrix(C_mat, M_mat, n, m, ell):
    R_mat = np.full((ell,m), np.inf) # 초기상태
    for i in range(n): 
        for j in range(1, m+1): # j는 index가 1부터 시작한다. (0부터 해도 답이 맞으면 정답처리)
            if C_mat[i][j-1] == 1: # 그러므로 j가 아닌 j-1
                for k in range(1, ell+1): # k는 1부터 시작한다. (0부터 해도 답이 맞으면 정답처리)
                    R_mat[k-1][j-1] = min(R_mat[k-1][j-1], M_mat[i][k-1]) # 그러므로 k가 아닌 k-1 
    return R_mat

def compute_Jaccard_similarity(R_mat, ell, alpha, beta):
    assert (1 <= alpha) and (ell >= beta) # R_mat은 행이 ell개이므로 이 범위 사이에 alpha, beta 존재
    S_alpha = R_mat[alpha - 1]
    S_beta = R_mat[beta - 1]
    return _Jaccard_similarity(S_alpha, S_beta)

def main():
    n, m, ell = NUMBER_OF_WORDS, NUMBER_OF_SETS, NUMBER_OF_HASHES
    targets = input("Enter your alpha, beta:").split(",")
    alpha, beta = int(targets[0]), int(targets[1])

    chr_mat_path = "./chr_mat.csv" # 특성행렬 파일 위치 
    hash_coefs_path = "./hash_coefs.csv" # 보조행렬 파일 위치
    
    C_mat = build_characteristic_matrix(chr_mat_path, n, m)
    H_mat = build_hash_functions(hash_coefs_path, ell)
    M_mat = compute_support_matrix(H_mat, n, ell)
    R_mat = compute_signature_matrix(C_mat, M_mat, n, m, ell)
    
    result = compute_Jaccard_similarity(R_mat, ell, alpha, beta)
    print("sim(S_alpha,S_beta) =", result)
    return None

if ("__main__" == __name__):
    main()

