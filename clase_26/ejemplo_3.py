while True:
    try:
        numero = int(input("Ingrese un número(distinto de cero): "))
        resultado = 10/numero
        print(f"el resultado es {resultado}")
        break
    except ZeroDivisionError:
        print("El valor ingresado debe ser un número distinto de cero, vuelva a intentarlo!!!")
    except ValueError:
        print("el número ingresado no puede ser un texto, no sea terco!!!")