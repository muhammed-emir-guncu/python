def matrisol(j,i):
    x=[[0 for b in range(i)] for a in range(j)]
    return x
def matrisyukseklik(x):
    return len(x)
def matrisgenislik(x):
    y=len(x[0])
    for i in range(1,len(x)):
        if y==len(x[i]):
            y=len(x[i])
        else:
            return False
            break
    return y

def matriscarp(x,y):
    z=list()
    if(matrisgenislik(x)==matrisyukseklik(y)):
        z=matrisol(matrisyukseklik(x),matrisgenislik(y))
        for j in range(matrisyukseklik(x)):
            for i in range(matrisgenislik(y)):
                for k in range(matrisyukseklik(y)):
                    z[j][i]+=x[j][k]*y[k][i]
        return z
    else:
        return False


def matrisyap(x):
    x = x.split(",")
    for i in range(len(x)):
        x[i] = x[i].split(" ")
        for j in range(x[i].count("")):
            x[i].remove("")
    for j in range(len(x)):
        for i in range(len(x[j])):
            x[j][i] = int(x[j][i])
    return x
a=matrisyap(input(" , matris gir: "))
b=matrisyap(input(" , matris gir: "))
print(matriscarp(a,b))

