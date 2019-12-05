import os
import msvcrt

class menuUsuario:

    def __init__(self,usuario,control_de_datos):
        self.login_usuario = usuario
        self.control = control_de_datos

    def menu(self):
        cond = True
        while (cond):
            self.control.actualizar_datos(self.login_usuario) # actualizo las listas del usuario 

            os.system('cls')

            print(f'Bienvenido {self.login_usuario.getNombre()} {self.login_usuario.getApellido()}')
            print(f'Menu de usuario\n')
            print(f'1.Informacion Personal.\n2.Iniciar una Publicacion\n3.Agregar un Amigo.\n4.Notificaciones\n5.Solicitudes pendientes\n6.Lista de Amigos\n7.Mis Publicaciones')       

            seleccion = msvcrt.getwch()

            if seleccion == '1':
                self.informacion_personal()
            elif seleccion == '2':
                self.control.agregar_publicacion(self.login_usuario)
            elif seleccion == '3':
                self.busqueda_amigo()
            elif seleccion == '4':
                self.mostrar_notificaciones()
            elif seleccion == '5':
                self.mostrar_solicitudes()
            elif seleccion == '6':
                self.mostrar_lista_amigos()
            elif seleccion == '7':
                self.mostrar_lista_publicaciones()
            elif seleccion == '\x1b':
                cond = False

    def informacion_personal(self):
        os.system('cls')

        print('Informacion Personal:')
        print(f'ID: {self.login_usuario.getID()}\nNombre y Apellido: {self.login_usuario.getNombre()} {self.login_usuario.getApellido()}')
        print(f'Email: {self.login_usuario.getEmail()}\nGenero: {self.login_usuario.getGenero()}')

        input('Presione cualquier tecla para continuar... ')
        self.menu() 

    def busqueda_amigo(self):
        os.system('cls')
        print('Busqueda')
        # Ingreso el nombre o apellido del usuario que deseo buscar
        usuario_posible = input('Porfavor, ingrese un nombre o apellido: ') 
        # Se almacena en una lista a los posibles "amigos" y se muestra en pantalla 
        usuarios_posibles = self.control.busqueda_usuario(usuario_posible,self.login_usuario.getAmigos(),self.login_usuario)
        # Se elige a un usuario dentro de la lista mostrada para agregar

        
        if usuarios_posibles == []:
            print('No se ha encontrado a algun usuario con ese nombre o apellido')
            input('Presione cualquier tecla para continuar... ')
        else:
            print('Esc. para salir de este menu, sino presione cualquier tecla')
            # Detecta si se toca la tecla "Esc"
            tecla=msvcrt.getwch()

            if tecla=='\x1b':
                pass
                # Se devuelve al menu principal
            else:
                try:
                    # Se elige un numero de la lista imprimida
                    usuario_elegido = int(input('Ingrese el numero de contacto a agregar: '))
                    # Se llama a la funcion agregar amigo que lo agragara a la base de datos
                    self.control.agregar_amigo(self.login_usuario,usuarios_posibles[usuario_elegido])
                except: 
                    print('No ha ingresado un valor correcto')
                    input('Presiona cualquier tecla... ')
                    self.busqueda_amigo()

    def mostrar_notificaciones(self):
        os.system('cls')
        notificaciones = self.login_usuario.getNotificaciones()
        print('Notificaciones:')

        if notificaciones == []:
            print(f'No tiene notificaciones')
        else:
            for notificacion in notificaciones:
                print(f'{notificacion.getDescripcion()}')
        
        input('Presione cualquier tecla')

    def mostrar_lista_amigos(self):
        os.system('cls')
        i = 0
        amigos = self.login_usuario.getAmigos()
        print("Lista de Amigos")
        if amigos == []:
            print(f'No tiene amigos agregados...')
            input('Presione cualquier tecla para continuar... ')
        else:
            for amigo in amigos:
                print(f'{i}. Perfil:\nNombre y Apellido: {amigo.getNombre()} {amigo.getApellido()}')
                i+=1

            print(f'Esc. para salir de este menu, sino cualquier tecla para continuar')
            tecla=msvcrt.getwch()
        
            if tecla=='\x1b':
                pass
            else:
                try:
                    var = int(input(f'Ingrese un numero de la lista: '))

                    self.submenu_amigos(amigos[var])
                except: 
                    print('No ha ingresado un valor correcto')
                    input('Presiona cualquier tecla... ')
                    self.mostrar_lista_amigos()
  
    def mostrar_lista_publicaciones(self):
        os.system('cls')
        i = 0
        publicaciones = self.login_usuario.getPublicaciones()
        print(f'Mis Publicaciones')

        if publicaciones == []:
            print(f'No tienes publicaciones hechas')
            input('Presione cualquier tecla para continuar... ')
        else:
            for publicacion in publicaciones:
                print(f'{i}.\nFecha: {publicacion.getFecha()}\n: {publicacion.getTexto()} :')
                i+=1
            
            print(f'Esc. para salir de este menu, sino cualquier tecla para continuar')
            tecla=msvcrt.getwch()
        
            if tecla=='\x1b':
                pass
            else:
                try:
                    var = int(input(f'Ingrese un numero de la lista: '))

                    self.submenu_publicacion(publicaciones[var])
                except: 
                    print('No ha ingresado un valor correcto')
                    input('Presiona cualquier tecla... ')
                    self.mostrar_lista_publicaciones()

    def mostrar_solicitudes(self):
        os.system('cls')
        i = 0
        solicitudes = self.login_usuario.getSolicitudes()
        print(f'Solicitudes Pendientes:')

        if solicitudes == []:
            print(f'No tiene solicitudes')
            input('Presione cualquier tecla para continuar... ')
        else:
            for solicitud in solicitudes:
                print(f'{i}.Solicitud de {solicitud.getNombre()} {solicitud.getApellido()}')
                i+=1

            print(f'Esc. para salir de este menu, sino cualquier tecla para continuar')
            tecla=msvcrt.getwch() 

            if tecla=='\x1b':
                pass
            else:
                try:
                    var = int(input('Ingrese un numero de la lista: '))

                    self.submenu_solicitud(solicitudes[var])
                except: 
                    print('No ha ingresado un valor correcto')
                    input('Presiona cualquier tecla... ')
                    self.mostrar_solicitudes()

    def submenu_solicitud(self,solicitud):
        os.system('cls')
        print(f'Desea agregar al usuario {solicitud.getNombre()} {solicitud.getApellido()} (Y/N)')

        tecla = msvcrt.getwch()

        if tecla == 'y':
            self.control.modificar_estado(solicitud)
        elif tecla == 'n':
            self.control.eliminar_amigo(self.login_usuario,solicitud)

    def submenu_amigos(self,amigo):
        cond = True
        while (cond):
            os.system('cls')
            
            print(f'Submenu\n1.Publicaciones\n2.Colocar un Rol\n3.Eliminar Amigo')
            
            tecla = msvcrt.getwch()

            if tecla == '1':
                publicaciones_amigo = amigo.getPublicaciones()

                if publicaciones_amigo == []:
                    print(f'No tiene publicaciones hechas')
                else:
                    for publicacion in publicaciones_amigo:
                        print(f'{i}.\nFecha: {publicacion.getFecha()}\n:{publicacion.getTexto()}:')
                        i+=1
                    
                input('Presione cualquier tecla para continuar...')

            elif tecla == '2':
                os.system('cls')
                roles = self.control.lista_roles()
                print('Roles:')

                for rol in roles:
                    print(f'{rol.getID()}. {rol.getDescripcion()}')

                var = int(input('Elija un rol de la siguiente lista: '))

                self.control.actualizar_rol(var,amigo)

                input('Presione cualquier tecla para continuar... ')
                
            elif tecla == '3':
                self.control.eliminar_amigo(self.login_usuario,amigo)
                break
                
            elif tecla == '\x1b':
                cond = False   

    def submenu_publicacion(self,publicacion):
        cond = True 
        while (cond):
            os.system('cls')
            
            print(f'Submenu\n1.Modificar publicacion\n2.Eliminar publicacion')
            
            tecla = msvcrt.getwch()

            if tecla == '1':
                var = str(input('Nuevo Texto:'))
                self.control.modificar_publicacion(var,publicacion)
                input('Presione cualquier tecla para continuar... ')
            elif tecla == '2':
                self.control.eliminar_publicacion(publicacion)
                input('Presione cualquier tecla para continuar... ')
                break
            elif tecla == '\x1b':
                cond = False
