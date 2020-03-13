def main():
    s=0
    print("argument = ", end='')
    n = int(input())
    if (n==2):
        for i in range (1, 3):
            print ("valeur ",i," = ",end='')
            a = int(input())
            s = a + s
        print("la somme vaut : ",s)
    else :
        print("Erreur!")
        main()
main()
