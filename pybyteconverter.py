# start
import os
def main():
    os.system('cls')
    print("pybyteconverter 0.1 by Francescohh (console)")
    print("Unità:")
    print("1. Byte")
    print("2. KiloByte")
    print("3. MegaByte")
    print("4. GigaByte")
    print("5. TeraByte")
    a = input("Selezionare prima unità(1-5): ")
    b = input("Selezionare seconda unità(1-5): ")
    c = float(input("Inserire valore da convertire: "))
    if a == "1" and b == "2" :
        print((str(c))+"B è uguale a "+(str(c / 1024))+"KB")
        m = input("Vuoi uscire? (s/n)")
        if m == "s":
            os.system('exit')
        elif m == "n":
            main()
    elif a == "1" and b == "3" :
        print((str(c))+"B è uguale a "+(str(c / (1024*1024)))+"MB")
        m = input("Vuoi uscire? (s/n)")
        if m == "s":
            os.system('exit')
        elif m == "n":
            main()
    elif a == "1" and b == "4" :
        print((str(c))+"B è uguale a "+(str(c / (1024*1024*1024)))+"GB")
        m = input("Vuoi uscire? (s/n)")
        if m == "s":
            os.system('exit')
        elif m == "n":
            main()
    elif a == "1" and b == "5" :
        print((str(c))+"B è uguale a "+(str(c / (1024*1024*1024*1024)))+"TB")
        m = input("Vuoi uscire? (s/n)")
        if m == "s":
            os.system('exit')
        elif m == "n":
            main()
    elif a == "2" and b == "1" :
        print((str(c))+"KB è uguale a "+(str(c * 1024))+"B")
        m = input("Vuoi uscire? (s/n)")
        if m == "s":
            os.system('exit')
        elif m == "n":
            main()
    elif a == "2" and b == "3" :
        print((str(c))+"KB è uguale a "+(str(c / 1024))+"MB")
        m = input("Vuoi uscire? (s/n)")
        if m == "s":
            os.system('exit')
        elif m == "n":
            main()
    elif a == "2" and b == "4" :
        print((str(c))+"KB è uguale a "+(str(c / (1024*1024)))+"GB")
        m = input("Vuoi uscire? (s/n)")
        if m == "s":
            os.system('exit')
        elif m == "n":
            main()
    elif a == "2" and b == "5" :
        print((str(c))+"KB è uguale a "+(str(c / (1024*1024*1024)))+"TB")
        m = input("Vuoi uscire? (s/n)")
        if m == "s":
            os.system('exit')
        elif m == "n":
            main()
    elif a == "3" and b == "1" :
        print((str(c))+"MB è uguale a "+(str(c * (1024*1024)))+"B")
        m = input("Vuoi uscire? (s/n)")
        if m == "s":
            os.system('exit')
        elif m == "n":
            main()
    elif a == "3" and b == "2" :
        print((str(c))+"MB è uguale a "+(str(c * 1024))+"KB")
        m = input("Vuoi uscire? (s/n)")
        if m == "s":
            os.system('exit')
        elif m == "n":
            main()
    elif a == "3" and b == "4" :
        print((str(c))+"MB è uguale a "+(str(c / 1024))+"GB")
        m = input("Vuoi uscire? (s/n)")
        if m == "s":
            os.system('exit')
        elif m == "n":
            main()
    elif a == "3" and b == "5" :
        print((str(c))+"MB è uguale a "+(str(c / (1024*1024)))+"TB")
        m = input("Vuoi uscire? (s/n)")
        if m == "s":
            os.system('exit')
        elif m == "n":
            main()
    elif a == "4" and b == "1" :
        print((str(c))+"GB è uguale a "+(str(c * (1024*1024*1024)))+"B")
        m = input("Vuoi uscire? (s/n)")
        if m == "s":
            os.system('exit')
        elif m == "n":
            main()
    elif a == "4" and b == "2" :
        print((str(c))+"GB è uguale a "+(str(c * (1024*1024)))+"KB")
        m = input("Vuoi uscire? (s/n)")
        if m == "s":
            os.system('exit')
        elif m == "n":
            main()
    elif a == "4" and b == "3" :
        print((str(c))+"GB è uguale a "+(str(c * 1024))+"MB")
        m = input("Vuoi uscire? (s/n)")
        if m == "s":
            os.system('exit')
        elif m == "n":
            main()
    elif a == "4" and b == "5" :
        print((str(c))+"GB è uguale a "+(str(c / 1024))+"TB")
        m = input("Vuoi uscire? (s/n)")
        if m == "s":
            os.system('exit')
        elif m == "n":
            main()
    elif a == "5" and b == "1" :
        print((str(c))+"TB è uguale a "+(str(c * (1024*1024*1024*1024)))+"B")
        m = input("Vuoi uscire? (s/n)")
        if m == "s":
            os.system('exit')
        elif m == "n":
            main()
    elif a == "5" and b == "2" :
        print((str(c))+"TB è uguale a "+(str(c * (1024*1024*1024)))+"KB")
        m = input("Vuoi uscire? (s/n)")
        if m == "s":
            os.system('exit')
        elif m == "n":
            main()
    elif a == "5" and b == "3" :
        print((str(c))+"TB è uguale a "+(str(c * (1024*1024)))+"MB")
        m = input("Vuoi uscire? (s/n)")
        if m == "s":
            os.system('exit')
        elif m == "n":
            main()
    elif a == "5" and b == "4" :
        print((str(c))+"TB è uguale a "+(str(c * 1024))+"GB")
        m = input("Vuoi uscire? (s/n)")
        if m == "s":
            os.system('exit')
        elif m == "n":
            main()
    else :
        print("Errore")
        m = input("Vuoi uscire? (s/n)")
        if m == "s":
            os.system('exit')
        elif m == "n":
            main()
main()

