def suma(a, b):
    c = a + b
    return c

def restar(a, b):
    return a-b

def multiplicar(a, b):
    return a*b

def div_entera(a, b):
    if b == 0:
        print("Error division sobre cero")
        return
    return a//b

def div_normal(a, b):
    if b==0:
        print("Error division sobre cero")
        return
    return a/b

def modulo(a, b):
    if b==0:
        print("Error division entre cero")
        return
    return a%b

def potencia(a, b):
    return a**b

def main():
    while True:
        print("Ingresa dos valores")
        x = int(input())
        y = int(input())

        print("1.Sumar\n2.Restar\n3.Division entera")
        print("4.Division\n5.Modulo\n6.Potencia\n7.Multiplicar\n8.Salir")

        op = int(input()) 

        if op == 1:
            print(suma(x, y))
        elif op == 2:
            print(restar(x, y))
        elif op == 3:
            print(div_entera(x, y))
        elif op == 4:
            print(div_normal(x,y))
        elif op == 5:
            print(modulo(x, y))
        elif op == 6:
            print(potencia(x, y))
        elif op == 7:
            print(multiplicar(x, y))
        elif op == 8:
            break
        else:
            print("Opcion no valida")

if __name__ =="__main__":
    main()