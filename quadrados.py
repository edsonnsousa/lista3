#Quadrados mais proximos#
from math import *
def main():
    numero = input("Digite o numero: ")
    quadrado(numero)
    
def quadrado(numero):
    num = int(sqrt(numero))
    menor = (num)*(num)
    print "O  Maior quadrado menor ou igual a %.1d  eh  %.1d"%(numero,menor)
    
if __name__ == '__main__':
    main()



    
