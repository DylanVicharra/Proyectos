class Usuario:

    def __init__(self,id,email,password,nombre,apellido,genero,foto):
        self.id = int(id)
        self.email = email
        self.password = password
        self.nombre = nombre
        self.apellido = apellido 
        self.genero = genero
        self.foto = foto
        self.amigos = []
        self.soli_pendientes = []
        self.publicaciones = []
        self.grupos = []
        self.notificaciones = []

    def getID(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getPassword(self):
        return self.password

    def getFoto(self):
        return self.foto

    def getEmail(self):
        return self.email

    def getGenero(self):
        return self.genero

    def getAmigos(self):
        return self.amigos

    def getNotificaciones(self):
        return self.notificaciones

    def getPublicaciones(self):
        return self.publicaciones

    def getSolicitudes(self):
        return self.soli_pendientes

    def changePassword(self,new_password):
        pass

    def changeFoto(self,new_foto):
        self.foto = new_foto

    def setAmigos(self,amigos):
        self.amigos = amigos

    def setNotificaciones(self,notificaciones):
        self.notificaciones = notificaciones 

    def setPublicaciones(self,publicaciones):
        self.publicaciones = publicaciones

    def setSolicitudes(self,solicitudes):
        self.soli_pendientes = solicitudes

    def eliminarNotificacion(self,notificacion):
        for noti in self.notificaciones:
            if (noti.getID() == notificacion.getID):
                self.notificaciones.remove(noti)

    def eliminarPublicacion(self,publicacion):
        for publi in self.publicaciones:
            if (publi.getID() == publicacion.getID()):
                self.publicaciones.remove(publi)

    def eliminarAmigo(self,amigo):
        for ami in self.amigos:
            if (ami.getID() == amigo.getID()):
                self.amigos.remove(ami)

    def elimiarGrupo(self,grupo):
        for gru in self.grupos:
            if (gru.getID() == grupo.getID()):
                self.grupos.remove(gru)
    

    