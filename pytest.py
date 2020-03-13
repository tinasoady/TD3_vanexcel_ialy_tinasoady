def main():
    S=0
    print ("argument = ", end='')
    n= int(input())
    if (n<2):
        print ("Erreur! ne saisi pas l'argument plus de 2 ou moins")
        return 0
    if (n>2):
        print ("Erreur! ne saisi pas l'argument plus de 2 ou moins")
        return 0
    if (n==2):
        for i in range(1, 3):
            print(i,"er argument est: ", end='')
            a= int(input())
            S= a+S
        print(" la somme vaut : ", s) 
main()
