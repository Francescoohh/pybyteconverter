# start
import os
import math

def main():
    os.system('cls')
    print("pybyteconverter 0.2 by Francescohh (console)")
    print("Unit:")
    print("1. Byte")
    print("2. KiloByte")
    print("3. MegaByte")
    print("4. GigaByte")
    print("5. TeraByte")
    a = input("Select first unit(1-5): ")
    b = input("Select second unit(1-5): ")
    c = float(input("Insert value to convert: "))
    if a == "1" and b == "2" :
        print((str(c))+"B equals to "+(str(c / 1024))+"KB")
        os.system('pause >nul')
    elif a == "1" and b == "3" :
        print((str(c))+"B equals to "+(str(c / pow(1024,2)))+"MB")
        os.system('pause >nul')
    elif a == "1" and b == "4" :
        print((str(c))+"B equals to "+(str(c / pow(1024,3)))+"GB")
        os.system('pause >nul')
    elif a == "1" and b == "5" :
        print((str(c))+"B equals to "+(str(c / pow(1024,4)))+"TB")
        os.system('pause >nul')
    elif a == "2" and b == "1" :
        print((str(c))+"KB equals to "+(str(c * 1024))+"B")
        os.system('pause >nul')
    elif a == "2" and b == "3" :
        print((str(c))+"KB equals to "+(str(c / 1024))+"MB")
        os.system('pause >nul')
    elif a == "2" and b == "4" :
        print((str(c))+"KB equals to "+(str(c / pow(1024,2)))+"GB")
        os.system('pause >nul')
    elif a == "2" and b == "5" :
        print((str(c))+"KB equals to "+(str(c / pow(1024,3)))+"TB")
        os.system('pause >nul')
    elif a == "3" and b == "1" :
        print((str(c))+"MB equals to "+(str(c * pow(1024,2)))+"B")
        os.system('pause >nul')
    elif a == "3" and b == "2" :
        print((str(c))+"MB equals to "+(str(c * 1024))+"KB")
        os.system('pause >nul')
    elif a == "3" and b == "4" :
        print((str(c))+"MB equals to "+(str(c / 1024))+"GB")
        os.system('pause >nul')
    elif a == "3" and b == "5" :
        print((str(c))+"MB equals to "+(str(c / pow(1024,2)))+"TB")
        os.system('pause >nul')
    elif a == "4" and b == "1" :
        print((str(c))+"GB equals to "+(str(c * pow(1024,3)))+"B")
        os.system('pause >nul')
    elif a == "4" and b == "2" :
        print((str(c))+"GB equals to "+(str(c * pow(1024,2)))+"KB")
        os.system('pause >nul')
    elif a == "4" and b == "3" :
        print((str(c))+"GB equals to "+(str(c * 1024))+"MB")
        os.system('pause >nul')
    elif a == "4" and b == "5" :
        print((str(c))+"GB equals to "+(str(c / 1024))+"TB")
        os.system('pause >nul')
    elif a == "5" and b == "1" :
        print((str(c))+"TB equals to "+(str(c * pow(1024,4)))+"B")
        os.system('pause >nul')
    elif a == "5" and b == "2" :
        print((str(c))+"TB equals to "+(str(c * pow(1024,3)))+"KB")
        os.system('pause >nul')
    elif a == "5" and b == "3" :
        print((str(c))+"TB equals to "+(str(c * pow(1024,2)))+"MB")
        os.system('pause >nul')
    elif a == "5" and b == "4" :
        print((str(c))+"TB equals to "+(str(c * 1024))+"GB")
        os.system('pause >nul')
    else :
        print("Errore")
        os.system('pause >nul')
main()

