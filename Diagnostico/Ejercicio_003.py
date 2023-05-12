print("Introduce los datos de la matriz A por filas ")
row11=input(int)
row12=input(int)
row13=input(int)
row21=input(int)
row22=input(int)
row23=input(int)


m = [[row11, row12, row13], [row21, row22, row23]]

matriz = len(m)

for i in range(matriz):
  print(m[i])


print("Introduce los datos de la matriz B por filas ")
fila11=input(int)
fila12=input(int)
fila21=input(int)
fila22=input(int)
fila31=input(int)
fila32=input(int)

m2 = [[fila11, fila12], [fila21, fila22], [fila31, fila32]]

matriz2 = len(m2)

for i in range(matriz2):
  print(m2[i])