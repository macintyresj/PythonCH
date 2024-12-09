def new_user(manejador, nombre, apellido, edad, contrasena):
    return manejador.agregar_cliente(nombre, apellido, edad, contrasena)

def show_user(manejador, nombre_usuario):
    manejador.mostrar_cliente(nombre_usuario)

def login(manejador, nombre_usuario, contrasena):
    return manejador.autenticar_cliente(nombre_usuario, contrasena)
