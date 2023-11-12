def NoofFlips(Matrix):
    flips = 0
    
    for i in range(len(Matrix[0])):
        if Matrix[0][i] == 0:
            Matrix[0][i] = 1
            flips += 1
    
    for i in range(len(Matrix)):
        if Matrix[i][0] == 0:
            Matrix[i][0] = 1
            flips += 1
    
    for i in range(len(Matrix)):
        if Matrix[i][-1] == 0:
            Matrix[i][-1] = 1
            flips += 1
    
    for i in range(len(Matrix[-1])):
        if Matrix[-1][i] == 0:
            Matrix[-1][i] = 1
            flips += 1
    
    return flips

Matrix = [[0, 1, 1, 1], [1, 1, 0, 1], [1, 1, 0, 1]]
print("No of flips required", NoofFlips(Matrix))
