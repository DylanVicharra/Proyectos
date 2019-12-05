# Diccionario con la configuracion de base de datos

dbconf = {
    'host':'localhost',
    'database':'mydb',
    'user':'root',
    'password':''
}

queries = {
    'add_usuario':'INSERT INTO usuario (emailUsuario, passwordUsuario, nombreUsuario, apellidoUsuario, generoUsuario, fotoUsuario) VALUES (%s,%s,%s,%s,%s,%s)',
    'add_contacto':'INSERT INTO contacto (Usuario_idUsuario, Usuario_idUsuario2, estadoContacto, Rol_idRol) VALUES (%s,%s,%s,%s)',
    'add_publicacion':'INSERT INTO publicacion (fechaPublicacion, textoPublicacion, imagenPublicacion, Usuario_idUsuario) VALUES (%s,%s,%s,%s)',
    'add_notificacion':'INSERT INTO notificacion (Usuario_idUsuario, descripcionNotificacion) VALUES (%s,%s)',
    'add_rol':'INSERT INTO rol (descripcionRol) VALUES (%s)',
    'del_contacto':'DELETE FROM contacto WHERE (Usuario_idUsuario = %s AND Usuario_idUsuario2 = %s) OR (Usuario_idUsuario = %s AND Usuario_idUsuario2 = %s)',
    'del_publicacion':'DELETE FROM publicacion WHERE idPublicacion = %s',
    'upd_estado':'UPDATE contacto SET estadoContacto = true WHERE Usuario_idUsuario = %s',
    'upd_contacto':'UPDATE contacto SET Rol_idRol = %s WHERE Usuario_idUsuario = %s OR Usuario_idUsuario2 = %s ',
    'upd_publicacion':'UPDATE publicacion SET fechaPublicacion = %s, textoPublicacion = %s WHERE idPublicacion = %s',
    'list_usuarios':'SELECT * FROM usuario',
    'list_roles':'SELECT * FROM rol',
    'list_amigos':'select idUsuario, nombreUsuario, apellidoUsuario, fotoUsuario, Rol_idRol from (select @id_select := %s i) id, lista_amigo',
    'list_solicitudes':'select idUsuario, nombreUsuario, apellidoUsuario, fotoUsuario from (select @id_select := %s i) id, solicitudes_pendientes',
    'list_notificaciones':'SElECT idNotificacion, descripcionNotificacion FROM notificacion WHERE Usuario_idUsuario = %s',
    'list_publicaciones':'SElECT idPublicacion, fechaPublicacion, textoPublicacion, imagenPublicacion FROM publicacion WHERE Usuario_idUsuario = %s',
    'busqueda':'SELECT * FROM datos_busqueda'
}

