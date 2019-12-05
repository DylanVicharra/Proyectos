class Solicitud:
    
    def __init__(self,id,nombre,apellido,foto):
        self.id = int(id)
        self.nombre = nombre
        self.apellido = apellido
        self.foto = foto

    def getID(self):
        return self.id
    
    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getFoto(self):
        return self.foto