def matrisol(j,i): #Verilen uzunluklarda bır sıfır matris oluşturur.
    x=[[0 for b in range(i)] for a in range(j)]
    return x


def matrisyukseklik(x): #Verilen matrisin yüksekliğini döndürür.
    return len(x)


def matrisgenislik(x): #Verilen matrisin genişliğini döndürür ve bütün genişliklerin eşit olup olmadığını kontrol eder.Eğer matrisin genişlikleri eşit değilse False değerini döndürür.
    y=len(x[0])
    for i in range(1,len(x)):
        if y==len(x[i]):
            y=len(x[i])
        else:
            return False
            break
    return y


def matriscarp(x,y): #Verilen iki matrsisi çarpımını döndürür.Eğer çarpılamazlarsa False değerini döndürür.
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


def matrisyap(x): #Verilen string'i 2 boyutlu bir diziye dönüştürür ve bütün string'leri integer yapar.(virgül ve boşluklardan ayırır.)
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

input()