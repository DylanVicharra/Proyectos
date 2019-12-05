import mysql.connector
import mysql.connector.errors
from db import queries, dbconf

class Database:
    
    def __init__(self):
        self.conexion = mysql.connector.connect(**dbconf)
        self.cursor = self.conexion.cursor()

    def agregar_contacto(self,contacto):
        self.cursor.execute(queries['add_contacto'],contacto)
        self.conexion.commit()

    def agregar_usuario(self,usuario):
        self.cursor.execute(queries['add_usuario'],usuario)
        self.conexion.commit()

    def agregar_notificacion(self,notificacion):
        self.cursor.execute(queries['add_notificacion'],notificacion)
        self.conexion.commit()
    
    def agregar_publicacion(self,publicacion):
        self.cursor.execute(queries['add_publicacion'],publicacion)
        self.conexion.commit()

    def eliminar_contacto(self,condicion_eliminar):
        self.cursor.execute(queries['del_contacto'],condicion_eliminar)
        self.conexion.commit()

    def eliminar_publicacion(self,condicion_eliminar):
        self.cursor.execute(queries['del_publicacion'],(condicion_eliminar,))
        self.conexion.commit()

    def actualizar_contacto(self,condicion_actualizar):
        self.cursor.execute(queries['upd_contacto'],condicion_actualizar)
        self.conexion.commit()

    def actualizar_publicacion(self,condicion_actualizar):
        self.cursor.execute(queries['upd_publicacion'],condicion_actualizar)
        self.conexion.commit()

    def actualizar_estado(self,condicion):
        self.cursor.execute(queries['upd_estado'],(condicion,))
        self.conexion.commit()
    
    def busqueda(self):
        self.cursor.execute(queries['busqueda'])
        data = self.cursor.fetchall()
        return data

    def listar_usuarios(self):
        self.cursor.execute(queries['list_usuarios'])
        data = self.cursor.fetchall()
        return data

    def listar_roles(self):
        self.cursor.execute(queries['list_roles'])
        data = self.cursor.fetchall()
        return data

    def lista_notificaciones_usuario(self,id):
        self.cursor.execute(queries['list_notificaciones'],(id,))
        data = self.cursor.fetchall()
        return data
        
    def lista_amigos_usuario(self,id):
        self.cursor.execute(queries['list_amigos'],(id,))
        data = self.cursor.fetchall()
        return data

    def lista_solicitudes_usuario(self,id):
        self.cursor.execute(queries['list_solicitudes'],(id,))
        data = self.cursor.fetchall()
        return data

    def lista_publicaciones_usuario(self,id):
        self.cursor.execute(queries['list_publicaciones'],(id,))
        data = self.cursor.fetchall()
        return data

        
