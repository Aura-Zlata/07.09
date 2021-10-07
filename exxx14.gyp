matrice=[]
n=int(input('Introdu nr de linii: '))
dp=0
ds=0
msdp=0
mjdp=0
mjds=0

for i in range(0,n):
    i=[]
    for j in range(0,n):
        j=int(input())
        i.append(j)
    matrice.append(i)

for i in range(0,n):
    for j in range(0,n):
        if (i == j):
            dp += matrice[i][j]
            print(dp, 'Suma componentelor pe diagonala principala este = ')
        if ((i + j) == (n-1)):
            ds += matrice[i][j]
            print(ds, 'Suma componentelor pe diagonala principala este= ')
        if (i>j):
            msdp += matrice[i][j]
            print(msdp, 'Suma componentelor mai sus de diagonala principala este= ')
        if (i<j):
            mjdp += matrice[i][j]
            print(mjdp, 'Suma componentelor mai jos de diagonala principala este= ')
        if ((i+j)<(n-1)):
            mss += matrice[i][j]
            print(mss, 'Suma componentelor mai sus de diagonala secundara este= ')
        if ((i+j)>(n-1)):
            mjds += matrice[i][j]
            print(mjds, 'Suma componentelor mai jos de diagonala secundara= ')