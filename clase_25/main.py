#herencia, en si es conectar una clase con la otra

class Padre():
    
    def retornarTexto(self):
        return "hola mi mamá me los compró"


class Hija(Padre):
    
    def miMetodo(self):
        return self.retornarTexto()


hija = Hija()
print(hija.miMetodo())