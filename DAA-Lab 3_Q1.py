a=[1,3,2]
b=[9,4,12]
c=[6,8,18]
D=[]


def Divisibleby3OrNot(M):
    for i in M :
        if i%3==0:
            print(i)
            D.append(i)

def GreaterThan50OrNot(D):
    E=1
    for i in D:
        E=E*i

    if E >50:
        print("Result of Multiplication of numbers divisible by 3 in given matrix is",E)
        print("Multiplication of numbers divisible by 3 in given matrix is greater than 50")


Divisibleby3OrNot(a)
Divisibleby3OrNot(b)
Divisibleby3OrNot(c)

GreaterThan50OrNot(D)