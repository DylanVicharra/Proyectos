from datetime import datetime

class Publicacion:

    def __init__(self,id,fecha,texto,imagen):
        self.id = id
        self.fecha = fecha
        self.texto = texto
        self.imagen = imagen

    def getID(self):
        return self.id

    def getFecha(self):
        return self.fecha 
    
    def getTexto(self):
        return self.texto

    def changeTexto(self,new_texto):
        self.texto = new_texto
        

