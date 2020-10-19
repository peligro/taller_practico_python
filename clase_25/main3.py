#colaboración de objetos, y ésto es llamar a una clase desde otra (Inyección de dependencias)

class Padre():
    
    def retornarTexto(self):
        return "hola mi mamá me los compró"


class Hija():
    
    def __init__(self):
        self.p = Padre()
        
    
    def otroMetodo(self):
        return self.p.retornarTexto()


h = Hija()
print(h.otroMetodo())
