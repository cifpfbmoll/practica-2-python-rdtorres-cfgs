import sys

print("Escriba un número")
N = int(input())
if N%2 ==0:
    print (N, 'es un número par')
else:
    print(N, 'es un número impar')
sys.exit()
