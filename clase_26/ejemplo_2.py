try:
    print(5/0)
except TypeError:
    print("ocurrió un error de tipo TypeError")
except ZeroDivisionError:
    print("eres un tonto no puedes dividir por cero")
finally:
    print("terminó de ejecutarse nuestro código")

