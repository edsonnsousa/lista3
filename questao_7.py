#Soma dos valores entre numeros#
def main ():
    numero= int(input("Digite um numero"))
    num(numero)
def num(numero):
    total  =0
    for i in range(1,numero+1):
            total=i+total
    print "Soma dos valores entre 1 e %d eh %d"%(numero,total)


if __name__ == '__main__':
    main()
