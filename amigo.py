class Amigo:

    def __init__(self,id,nombre,apellido,foto,rol):
        self.id = int(id)
        self.nombre = nombre
        self.apellido = apellido
        self.foto = foto
        self.rol = rol
        self.publicaciones = []

    def getID(self):
        return self.id
    
    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido
        
    def getRol(self):
        return self.rol

    def getPublicaciones(self):
        return self.publicaciones
    
    def setPublicaciones(self,publicaciones):
        self.publicaciones = publicaciones