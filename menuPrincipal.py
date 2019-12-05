from control import Control
from menuUsuario import menuUsuario, os, msvcrt
from usuario import Usuario
import getpass
import stdiomask



def login_usuario(control): 
    intento=3
    while intento!=0:
        os.system('cls')
        print("Bienvenido a CARALIBRO")
        print("Por favor ingrese la siguiente informacion:")
        user= input("ID de Usuario o Email: ") 
        password=stdiomask.getpass("Password: ",mask='*')


        if user.isdigit():
            user = int(user)

        data = control.validarLogin(user,password)

        if data is False:
            intento-=1
            print('usuario no existe o contraseña incorrecta ')
            print(f'Le queda/n {intento} intento/s')
            input("presione cualquier tecla para continuar...")
        else:
            menuUs = menuUsuario(Usuario(*data),control)
            menuUs.menu()
            input('Hasta Luego')
            break

def registro_usuario(control):
    os.system('cls')
    print("Ingrese la siguiente informacion")

    nombre = str(input('Nombre: '))
    apellido = str(input('Apellido: '))
    genero = str(input('Genero (M/F): ')) #hacer un combo box
    password = str(input('Password: ')) # hacer una confirmacion de password (prueba)
    email = str(input('Email: ')) # pensar si hacer confirmacion de email o no

    errores = control.validarRegister(nombre,apellido,genero,password,email)

    if errores != {}:
        print(f'Tiene los siguientes errores: \n{errores}')
        input("presione cualquier tecla para continuar...")
        registro_usuario(control)
    else:
        new_user = (email,control.codificar_password(password),nombre,apellido,genero,None)
        control.base.agregar_usuario(new_user)
        print('Usuario registrado.')
        input("presione cualquier tecla para volver a cargar los datos...")
        login_usuario(control)

def main():
    control = Control() 
    cond = True
    while (cond):     
        os.system('cls')
        print("Bienvenido a CARALIBRO \n1. Loguear \n2. Registrarse")

        # Detecta la tecla pulsada
        tecla=msvcrt.getwch()
        
        if tecla == '1':
            login_usuario(control)
        elif tecla == '2':
            registro_usuario(control)
        elif tecla == '\x1b':
            print(f'Finalizando aplicacion...\nGracias por usarla')
            cond = False

if __name__ == "__main__":
    main()
    
    

    
   