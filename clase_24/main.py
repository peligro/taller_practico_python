class Persona:

    #atributos, ésto es en sí una variable
    #nombre = "César"
    
    
    #se puede un constructor, este método se ejecuta cuando se instancia la clase. Generalmente de las veces se usa para inicializar valores
    def __init__(self, nombre):
        self.nombre = nombre
        
    
    #se pueden definir métodos propios
    # se recomienda dentro de los métodos NO hacer print, en su lugar hacer return
    def getNombre(self, miparametro):
        return f"nombre={self.nombre} | miparametro={miparametro}"



#instanciamos la clase, o creamos un objeto de la clase
persona = Persona('César Cancino')#esta variable pasa a ser un objeto de la clase Persona. Es una instancia de la clase Persona
print(persona.getNombre('mi muñeca me habló'))

#con ésto sabemos si una variable es instancia de una clase determinada o no lo es
#print(isinstance(persona, Persona))












"""
1 - lineal

2 - estructurada, encapsules en funciones o métodos

3 - POO  , clase, en un molde en donde tú almacenas tus métodos o funciones
"""