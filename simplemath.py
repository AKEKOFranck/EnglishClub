def simplemath():
    while True:
        x = int(input("Entrez un premier chiffre = "))
        y = int(input("Entrez un second chiffre = "))
        z = input("a-A:+, b-B:-, c-C:*, d-D:/, q:quitter = ")
        
        if z == 'q':
            break
        elif z == 'a' or z == 'A':
            print(x + y)
        elif z == 'b' or z == 'B':
            print(x - y)
        elif z == 'c' or z == 'C':
            print(x * y)
        elif z == 'd' or z == 'D':
            if y == 0:
                print("Division impossible")
            else:
                print(x / y)
        else:
            print("Option invalide, veuillez réessayer.")

simplemath()