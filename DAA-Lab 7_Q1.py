def FindRowWithGreatest1(Matrix):
    for i in range(len(Matrix)):
        noofOne=0
        for j in range(len(Matrix[i])):
            if Matrix[i][j]==1:
                noofOne+=1
    print(noofOne)

Matrix=[[0,0,0,1],[1,1,0,1],[0,0,0,0],[1,1,1,1]]
k=[]
FindRowWithGreatest1(Matrix)