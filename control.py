from database import Database
from amigo import Amigo
from notificacion import Notificacion
from publicacion import Publicacion
from rol import Rol
from solicitud import Solicitud
from datetime import datetime
import hashlib

class Control:

    def __init__(self):
        self.base = Database() 

    def validarLogin(self,usuario,password):
        password = self.codificar_password(password) # codifico de nuevo para comparar, ya que sha256 es unidireccional
        dataUsuarios = self.base.listar_usuarios()
        
        for data in dataUsuarios:
            if ((usuario in data) and (password in data)):
                return data
        
        return False

    def codificar_password(self,password):
        code_password = hashlib.sha256(bytes(password,'utf-8')).hexdigest()
        return code_password

    def checkNombre(self,nombre,errores):
        erroresNombre = []
        long=len(nombre) #Calcular la longitud del nomre de usuario
        y=nombre.isalpha() #Calcula que la cadena contenga valores alfabeticos
        
        if y== False: # La cadena contiene valores no alfabeticos
            erroresNombre.append("El nombre de usuario puede contener solo letras")
            
        if long < 2: 
            erroresNombre.append("El nombre de usuario debe contener al menos 3 caracteres")
            
        if erroresNombre != []:
            errores["nombre"]=erroresNombre

    def checkApellido(self,apellido,errores):
        erroresApellido = []
        long=len(apellido) #Calcular la longitud del nomre de usuario
        y=apellido.isalpha() #Calcula que la cadena contenga valores alfabeticos
        
        if y== False: # La cadena contiene valores no alfabeticos
            erroresApellido.append("El apellido de usuario puede contener solo letras")
            
        if long < 2: 
            erroresApellido.append("El apellido de usuario debe contener al menos 3 caracteres")
            
        if erroresApellido != []:
            errores["apellido"]=erroresApellido

    def checkGenero(self,genero,errores):
        erroresGenero = []

        if (genero !='M' and genero !='F'):
            erroresGenero.append('El genero no es uno de los disponibles')

        if erroresGenero != []:
            errores["genero"]=erroresGenero

    def checkPassword(self,password,errores):
        erroresPassword = []
        validar=False #que se vayan cumpliendo los requisitos uno a uno.
        long=len(password) #Calcula la longitud de la contraseña
        espacio=False  #variable para identificar espacios
        mayuscula=False #variable para identificar letras mayúsculas
        minuscula=False #variable para contar identificar letras minúsculas
        numeros=False #variable para identificar números
        y=password.isalnum()#si es alfanumérica retona True
        correcto=True #verifica que hayan mayuscula, minuscula, numeros y no alfanuméricos
                
        for carac in password: #ciclo for que recorre caracter por caracter en la contraseña

            if carac.isspace()==True: #Saber si el caracter es un espacio
                espacio=True #si encuentra un espacio se cambia el valor user

            if carac.isupper()== True: #saber si hay mayuscula
                mayuscula=True #acumulador o contador de mayusculas
                        
            if carac.islower()== True: #saber si hay minúsculas
                minuscula=True #acumulador o contador de minúsculas
                        
            if carac.isdigit()== True: #saber si hay números
                numeros=True #acumulador o contador de numeros
                                    
        if espacio==True: #hay espacios en blanco
            erroresPassword.append("La contraseña no puede contener espacios")
        else:
            validar=True #se cumple el primer requisito que no hayan espacios
                            
        if long <8 and validar==True:
            erroresPassword.append("Mínimo 8 caracteres")
            validar=False #cambia a Flase si no se cumple el requisito móinimo de caracteres

        if mayuscula == True and minuscula ==True and numeros == True and y== False and validar ==True:
            validar = True #Cumple el requisito de tener mayuscula, minuscula, numeros y no alfanuméricos
        else:
            correcto=False #uno o mas requisitos de mayuscula, minuscula, numeros y no alfanuméricos no se cumple
                
        if validar == True and correcto==False:
            erroresPassword.append("La contraseña elegida no es segura: debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")

        if erroresPassword != []:
            errores['password']=erroresPassword

    def checkEmail(self,email,errores):
        erroresEmail = []

        if email.find('@') < 0:
            erroresEmail.append('El email ingresado no es uno correcto')

        # Verifico que el email no este ya en uso
        data = self.base.listar_usuarios()

        for usuario in data:
            if email in usuario:
                 erroresEmail.append('El email ingresado ya esta en uso')

        if erroresEmail != []:
            errores['email']=erroresEmail

    def validarRegister(self,nombre,apellido,genero,password,email):
        errores = {}

        self.checkNombre(nombre,errores)
        self.checkApellido(apellido,errores)
        self.checkGenero(genero,errores)
        self.checkPassword(password,errores)
        self.checkEmail(email,errores)
            
        return errores

    def busqueda_usuario(self,usuario_posible,lista_amigos,usuario):
        # Trae una vista con cierta informacion  
        busqueda = self.base.busqueda()
        # Declaro esta variable para guardar a los posibles usuario que coinciden
        posibles = []
        # Numeracion de usuario
        number = 0

        for pos in busqueda:
            if usuario_posible in pos:
                
                amigo = Amigo(*pos,None)
                
                if self.check_busqueda(amigo,lista_amigos,usuario):
                    posibles.append(amigo)
                    print(f'{number}. {posibles[number].getNombre()} {posibles[number].getApellido()}') 
                    number+=1

        return posibles

    def check_busqueda(self,posible,lista_amigos,usuario):
        
        for amigo in lista_amigos:
            if (amigo.getID() == posible.getID()):
                return False
            elif (usuario.getID() == posible.getID()):
                return False

        return True
                

    def agregar_publicacion(self,usuario):
        print('Nueva Publicacion: ')
        # La fecha de publicacion se hace ni bien se termina de ingresar la info
        texto = str(input('Texto: '))
        imagen = None # Pensado para pantallas
        fecha = datetime.now()
        
        # Armo la tupla 
        publicacion = (fecha,texto,imagen,usuario.getID())

        self.base.agregar_publicacion(publicacion)

        input('Presiona cualquier tecla... ')

    def agregar_amigo(self,usuario,posible_amigo):
        # Se pasa los datos a la clase que agrega la nueva informacion a la base de datos
        usuario_remitente = usuario.getID()
        usuario_amigo = posible_amigo.getID()
        estado = False # Porque es una nueva relacion
        rol = None # Ya que el usuario despues de agregar, le da un rol (si el otro usuario lo acepta)
        # Se crea una tupla con toda la info que va a guardarse, Relacion es False ya que se envia solicitud por primera vez
        contacto = (usuario_remitente,usuario_amigo,estado,rol)
        # Se agrega en la base de datos
        self.base.agregar_contacto(contacto) 
        print('Se ha envia la solicitud de amistad')
        #Se envia un notificacion de amistad al posible amigo
        self.notificar(usuario,posible_amigo)

        input('Presiona cualquier tecla... ')

    def notificar(self,usuario_remitente,usuario_destinatario):
        # Se crea una tupla con los datos de la notificacion a guardar
        nueva_notificacion = (usuario_destinatario.getID(),f'Usted tiene una solicitud pendiente de {usuario_remitente.getNombre()} {usuario_remitente.getApellido()}')
        # Se guarda en la base de datos
        self.base.agregar_notificacion(nueva_notificacion)

    def actualizar_rol(self,rol,amigo):
        condicion = (rol,amigo.getID(),amigo.getID())

        self.base.actualizar_contacto(condicion)

        print('Se ha actualizado el rol correctamente')

    def modificar_publicacion(self,nuevo_texto,publicacion):
        nueva_fecha = datetime.now()
        condicion = (nueva_fecha,nuevo_texto,publicacion.getID())
        
        self.base.actualizar_publicacion(condicion)
        print('Se ha modificado la publicacion correctamente')

    def modificar_estado(self,solicitud):
        self.base.actualizar_estado(solicitud.getID())
        print('Ahora son amigos')
        input('Presiona cualquier tecla... ')

    def eliminar_amigo(self,usuario,amigo):
        # Se armaran dos tuplas con dos combinaciones distintas
        fst_con = (usuario.getID(),amigo.getID())
        snd_con = (amigo.getID(),usuario.getID())
        # uno las tuplas 
        condicion = (*fst_con,*snd_con)
        
        self.base.eliminar_contacto(condicion)     

        print('Se ha eliminado al usuario de su lista de amigos')   

    def eliminar_publicacion(self,publicacion):
        self.base.eliminar_publicacion(publicacion.getID()) 

        print('Se ha eliminado la publicacion')

    def lista_amigos(self,usuario):
        # Se trae de la base de datos a los amigos del usuario
        data = self.base.lista_amigos_usuario(usuario.getID())
        amigos = []
        for dato in data:
            # Actualizo sus publicaciones
            amigo = self.lista_publicaciones(Amigo(*dato))
            # Agrego en la lista
            amigos.append(amigo)
        
        # Se lo almacena dentro del objeto usuario
        usuario.setAmigos(amigos)

        return usuario
    
    def lista_notificaciones(self,usuario):
        data = self.base.lista_notificaciones_usuario(usuario.getID())
        notificaciones = []
        for notificacion in data:
            notificaciones.append(Notificacion(*notificacion))

        usuario.setNotificaciones(notificaciones)
        return usuario
            
    def lista_publicaciones(self,usuario):
        data = self.base.lista_publicaciones_usuario(usuario.getID())
        publicaciones = []
        for publicacion in data:
            publicaciones.append(Publicacion(*publicacion))    

        usuario.setPublicaciones(publicaciones)
        return usuario        

    def lista_roles(self):
        data = self.base.listar_roles()
        roles = []
        for rol in data:
            roles.append(Rol(*rol))

        return roles

    def lista_soli_pendientes(self,usuario):
        data = self.base.lista_solicitudes_usuario(usuario.getID())
        solicitudes = []
        for solicitud in data:
            solicitudes.append(Solicitud(*solicitud))

        usuario.setSolicitudes(solicitudes)
        return solicitudes        

    def actualizar_datos(self,usuario):
        self.lista_amigos(usuario)
        self.lista_notificaciones(usuario)
        self.lista_publicaciones(usuario)
        self.lista_soli_pendientes(usuario)

        return usuario


