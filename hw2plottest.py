
    #test
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    if d == 1:
        x = np.arange(-25,25)
        y = result[0][0]*x + result[1][0]
        plt.plot(x, y)  # draw line\
        plt.axvline(x=0, color = 'r')  # draw x =0 axes
        plt.axhline(y=0, color = 'r')   # draw y =0 axes  
        for tmp in range(n):
            x= X[0,tmp]
            y =Y[0,tmp]
            plt.plot(x, y, 'o')   # draw dots
    else:
        #fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        print(Y.shape)
        for tmp in range(n):
            x3= X[0,tmp]
            y3 =Y[tmp]
            z3 =X[1,tmp]
        plt.scatter(x3, y3, z3)
        
        x4 = np.arange(-25,25,0.1)
        y4 = result[0][0]*x4 + result[1][0]
        z4 = np.arange(0,100,0.1)
        ax.plot(x4, y4, z4)
        plt.tight_layout()
        # for tmp in range(n):
        #     x= X[0,tmp]
        #     z =X[1,tmp]
        #     y =Y[tmp]
        #     plt.plot(x, y, z, 'o')   # draw dots
    # plt.plot(x, y, x, y, 'o')
    plt.show()
    