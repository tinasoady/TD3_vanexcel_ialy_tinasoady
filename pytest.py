def main():
    S=0
    print ("argument = ", end='')
    n = int(input())
    if (n==2):
        for i in range (1, 3):
            print ("argument",i," = ", end='')
            a = int(input())
            S= a+S
        print("la somme vaut : ", S)
    else :
        print("Erreur! ")
        main()
main()
