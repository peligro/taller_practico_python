#nombre = input("Dime tu nombre: ")


n1=input("Ingresa un número: ")
n2=input("Ingresa otro número: ")

if len(n1) >=1:
    resultado = int(n1) + int(n2)
    print(f"el resultado de los números ingresados es : {resultado}")
else:
    print("el número 1 está vacío")
#print(type(nombre))