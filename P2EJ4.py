import sys
print("Vamos a ver cual es el número más grande")
A = int(input("Escriba el primer número "))
B = int(input("Escriba el segundo número "))
if A == B:
    print (A, 'es igual a ', B,)
elif A > B:
    print(A, 'es mayor a ', B,)
else:
    print(B, 'es mayor a ', A,)
sys.exit()
