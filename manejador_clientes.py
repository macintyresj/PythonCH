# manejador_clientes.py

from cliente import Cliente

class ManejadorClientes:
    def __init__(self):
        self.clientes = {}

    def agregar_cliente(self, nombre, apellido, edad, contrasena):
        user_id = "user00" + str(len(self.clientes) + 1)
        nombre_usuario = nombre[0] + apellido + edad
        cliente = Cliente(id_cliente=user_id, nombre=nombre, apellido=apellido, nombre_usuario=nombre_usuario, contrasena=contrasena, edad=int(edad))
        self.clientes[user_id] = cliente
        print(f"Cliente {cliente.nombre} {cliente.apellido} agregado exitosamente. Su nombre de usuario es {cliente.nombre_usuario}")
        return cliente

    def mostrar_cliente(self, nombre_usuario):
        for cliente in self.clientes.values():
            if cliente.nombre_usuario == nombre_usuario:
                print(cliente)
                return
        print("Cliente no encontrado")

    def autenticar_cliente(self, nombre_usuario = "test", contrasena = "123"):
        for cliente in self.clientes.values():
            if cliente.nombre_usuario == nombre_usuario and cliente.contrasena == contrasena:
                print("Inicio de sesión exitoso")
                return cliente
        print("Nombre de usuario o contraseña incorrectos")
        return None
