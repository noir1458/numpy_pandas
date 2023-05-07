
import numpy as np
import time

def make_meta():
    # your code
    # meta.npz는 원소개수 3개인 np.array 2개로 저장되어있고, 차례로 n, k, d 값에 대응
    # 주어진 csv파일과 선택한 k를 바탕으로 make_meta() 함수에 구현하여 사용
    # n k d=1
    # n k d>1
    npz_data = np.empty(shape=(2,3),dtype=np.int64)
    # k값 랜덤으로 선택
    np.random.seed(int(time.time()))
    generate_k = np.random.randint(150,200,2,dtype=np.int32)
    npz_data[0,1], npz_data[1,1] = generate_k[0], generate_k[1]

    # n값, d값 array에 쓰기
    csv_a = np.loadtxt('programmer_income.csv',delimiter=',',dtype=np.unicode_) #d=1
    npz_data[0,0], npz_data[0,2] = csv_a.shape[0]-1, csv_a.shape[1]-1
    csv_b = np.loadtxt('car_price.csv',delimiter=',',dtype=np.unicode_) #d>1
    npz_data[1,0], npz_data[1,2] = csv_b.shape[0]-1, csv_b.shape[1]-1

    # npz 파일 쓰기
    np.save('./meta',npz_data)
    meta_file_path = './meta.npy'
    return meta_file_path

def read_meta(meta_file_path):
    # your code
    meta_load = np.load(meta_file_path)
    meta = meta_load
    return meta

def read_input(csv_file_path,n,d):
    D_n = np.empty(shape=(n,d+1))
    # your code
    # csv 파일을 읽어서 2D np.array에 저장하여 D_n으로 돌려주기
    # n,d는 meta.npz 파일에서 읽은 input dataset Dn의 크기 n과 d값
    # programmer_income.csv는 d=1, car_price는 d>1
    #read_csv = np.loadtxt(csv_file_path,delimiter=',',)
    read_csv = np.genfromtxt(csv_file_path,delimiter=',',skip_header=1,dtype=np.unicode_)
    D_n = read_csv
    return D_n

def compute_MSE_over_vector(a,b):
    mse = np.empty(shape=(1,1), dtype=np.float64)
    # your code
    mse[0,0] = np.mean((np.power(a-b,2)))
    return mse

def compute_MSE_over_matrix(A,B):
    k = A.shape[0] # k 값 내용 필요
    MSE = np.empty(shape=(k,1), dtype=np.float64)
    # your code
    tmp_array = np.empty(shape=(0,1),dtype=np.float64)
    for row_num in range(k): # 행 단위로 MSE 계산하여 쌓는다
        add_array = compute_MSE_over_vector(A[row_num,:],B[row_num,:])
        tmp_array = np.vstack([tmp_array,add_array])
    MSE = tmp_array
    return MSE

def compute_object_function(X, Y, theta, theta_0):
    J_th_th0 = [] # the output of object function
    # your code
    #theta_0_Add = np.tile(theta_0,(1,X.shape[1])) # k x n 으로 theta_0을 늘려서 더해준다
    theta_0_Add = theta_0
    # theta (k x d), X (d x n), theta_0_Add (K x n)
    A = np.dot(theta,X) + theta_0_Add
    B = np.tile(Y,(theta_0.shape[0],1)) # Y (1 x n)를 k x n 으로 늘린다
    MSE = compute_MSE_over_matrix(A,B)
    J_th_th0 = [theta[np.argmin(MSE)],theta_0[np.argmin(MSE)],MSE[np.argmin(MSE)]]
    return J_th_th0 # object function 의 결과는 MSE를 최소화시키는 theta, theta_0

    # @brief the main func for looking for optimal (theta,theta_0)
    # @param X input X
    # @param Y output Y
    # @param n the number of X, Y
    # @param k the number of theta
    # @param d the dimension of each x_i
def compute_random_linear_regression(X,Y,n,k,d):
    # your code
    theta_star, theta_0_star, mse_star = None,None,None
    np.random.seed(int(time.time()))
    theta_array = np.random.randint(1,150000,(k,d))   # k x d 크기의 theta array - 각 행을 theta 라고 하기, 총 k개
    theta_0_array = np.random.randint(1,150000,(k,1)) # k x 1 크기의 theta_0 array - 각 행을 theta_0 라고 하기, 총 k개
    
    J_th_th0_output = compute_object_function(X,Y,theta_array,theta_0_array)
    theta_star, theta_0_star, mse_star = J_th_th0_output[0], J_th_th0_output[1], J_th_th0_output[2]
    return (theta_star, theta_0_star, mse_star)

def main():
    # call functions
    meta = read_meta(make_meta())
    
    #print(meta)
    # meta 파일 정보 이용해서 csv읽기
    if input('d = 1 경우 1 나머지는 2 입력 : ') == '1':
        n,k,d = meta[0,0],meta[0,1],meta[0,2]
        csv1 = read_input('./programmer_income.csv',n,d)
        X = np.transpose(csv1[:,:d]).astype(np.float32)     # d x n 크기 X , Y_i는 마지막 col에 해당
        Y = np.transpose(csv1[:,d:]).astype(np.int32)     # 1 x n 크기 Y
    else:
        n,k,d = meta[1,0],meta[1,1],meta[1,2]
        csv2 = read_input('./car_price.csv',n,d)
        Y = csv2[:,2].astype(np.int32).reshape(n,1) # Y_i에 해당하는 selling price가 중간에 위치함
        Y = Y.transpose()   # 1 x n 크기 Y

        X = np.empty(shape=(0,n),dtype=np.float64)
        for tmp in range(d+1):
            if tmp == 0: # car_name.csv에 있는 자동차 이름에 대응되는 순번을 읽어서 사용.
                name_csv = np.genfromtxt('car_name.csv',delimiter=',',skip_header=1,dtype=np.unicode_)
                name_Array = np.transpose(name_csv)
                x_tmp = np.transpose(csv2[:,tmp]).astype(np.unicode_)
                # 자동차 이름을 car_name에 있는 자동차 이름에 대응되는 순번을 읽어서 사용..
                for idx in range(x_tmp.shape[0]):
                    if x_tmp[idx] in name_Array:
                        find_idx = np.where(name_Array == x_tmp[idx])
                        x_tmp[idx] = find_idx[0][0]                   
                    else:
                        x_tmp[idx] = 97 # Maruti Swift Dzire VDi(마지막 i가 소문자) 찾을때 문제 발생..idx 198? 196?
                        # car_name.csv 안에 Maruti Swift Dzire VDi가 없음 (Maruti Swift Dzire VDI 는 있지만...)
                        # car_price.csv 198,2439번째 줄 등 Maruti Swift Dzire VDi 11개 존재
                #print(idx_array)
                X = np.vstack([X,x_tmp.astype(np.int64)])
            elif tmp == 1: # year
                x_tmp = np.transpose(csv2[:,tmp]).astype(np.int32)
                X = np.vstack([X,x_tmp])
            elif tmp == 2: # selling price 는 Y_i
                pass
            elif tmp == 3: # km_driven
                x_tmp = np.transpose(csv2[:,tmp]).astype(np.int32)
                X = np.vstack([X,x_tmp])
            elif tmp == 4: # fuel
                # 연료유형 순서대로 1 Petrol/2 Diesel/3 CNG/4 LPG/5 Electric
                x_tmp = np.transpose(csv2[:,tmp]).astype(np.unicode_)
                x_tmp = np.where(x_tmp=='Petrol',1,x_tmp)
                x_tmp = np.where(x_tmp=='Diesel',2,x_tmp)
                x_tmp = np.where(x_tmp=='CNG',3,x_tmp)
                x_tmp = np.where(x_tmp=='LPG',4,x_tmp)
                x_tmp = np.where(x_tmp=='Electric',5,x_tmp)
                X = np.vstack([X,x_tmp.astype(np.int32)])
            elif tmp == 5: # seller_type 1 Individual/2 Dealer/3 Trustmark Dealer
                x_tmp = np.transpose(csv2[:,tmp]).astype(np.unicode_)
                x_tmp = np.where(x_tmp=='Individual',1,x_tmp)
                x_tmp = np.where(x_tmp=='Dealer',2,x_tmp)
                x_tmp = np.where(x_tmp=='Trustmark Dealer',3,x_tmp)
                X = np.vstack([X,x_tmp.astype(np.int32)])
            elif tmp==6: # transmission  1 Manual/2 Automatic
                x_tmp = np.transpose(csv2[:,tmp]).astype(np.unicode_)
                x_tmp = np.where(x_tmp=='Manual',1,x_tmp)
                x_tmp = np.where(x_tmp=='Automatic',2,x_tmp)
                X = np.vstack([X,x_tmp.astype(np.int32)])
            else: # tmp == 7 # owner 1 First Owner/2 Second Owner/3 Third Owner/4 Fourth & Above Owner/5 Test Drive Car
                x_tmp = np.transpose(csv2[:,tmp]).astype(np.unicode_)
                x_tmp = np.where(x_tmp=='First Owner',1,x_tmp)
                x_tmp = np.where(x_tmp=='Second Owner',2,x_tmp)
                x_tmp = np.where(x_tmp=='Third Owner',3,x_tmp)
                x_tmp = np.where(x_tmp=='Fourth & Above Owner',4,x_tmp)
                x_tmp = np.where(x_tmp=='Test Drive Car',5,x_tmp)
                X = np.vstack([X,x_tmp.astype(np.int32)])

    result = compute_random_linear_regression(X,Y,n,k,d)

    print('결과 : ',end='')
    print(result)

    '''
    #test
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    if d == 1:
        x = np.arange(-25,25)
        y = result[0][0]*x + result[1][0]
        plt.plot(x, y)  # draw line
        plt.axvline(x=0, color = 'r')  # draw x =0 axes
        plt.axhline(y=0, color = 'r')   # draw y =0 axes  
        for tmp in range(n):
            x= X[0,tmp]
            y =Y[0,tmp]
            plt.plot(x, y, 'o')   # draw dots
    else:
        fig = plt.figure(figsize=(9, 6))
        ax = fig.add_subplot(111, projection='3d')  
        x=np.linspace(2000,1700,10)
        y=np.linspace(13000,17000,10)
        x,y=np.meshgrid(x,y)
        z=result[0][0]*x+result[0][1]*y+result[1][0]
        ax.view_init(25,50)
        ax.plot_surface(x,y,z,alpha=1.0,cmap=plt.cm.coolwarm)
        #ax.plot(x,y,z)
        for tmp in range(n):
            if result[0][0]*X[0,tmp]+result[0][1]*X[1,tmp]+result[1][0] > Y[0,tmp]:
                ax.scatter(X[0,tmp],X[1,tmp],Y[0,tmp], marker='o',s=10,c='g')
            else:
                ax.scatter(X[0,tmp],X[1,tmp],Y[0,tmp], marker='o',s=10,c='r')
        # x
    plt.show()
    '''
    

    return None

if ("__main__" == __name__):
    main()