class Cliente:
    def __init__(self, id_cliente, nombre, apellido, nombre_usuario, contrasena, edad):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.edad = edad
        self.productos_comprados = []

    def __str__(self):
        productos = ', '.join(self.productos_comprados) if self.productos_comprados else 'Ninguno'
        return f"Cliente({self.id_cliente}): {self.nombre} {self.apellido}, Usuario: {self.nombre_usuario}, Edad: {self.edad}, Productos Comprados: {productos}"

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def comprar(self, producto, precio):
        self.productos_comprados.append(f"{producto} (${precio})")
        print(f"{self.nombre} {self.apellido} compraste {producto} por ${precio}")
