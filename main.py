from manejador_clientes import ManejadorClientes
import login

def start():
    manejador = ManejadorClientes()
    usuario_autenticado = None

    option = "si"
    print("Bienvenido al sistema de gestión de clientes")

    while option == "si":
        if usuario_autenticado:
            print(f"Usuario autenticado: {usuario_autenticado.nombre_usuario}")
        choose = input("1. Nuevo cliente\n"
                       "2. Ingresar\n"
                       "3. Mostrar información del cliente\n"
                       "4. Comprar\n"
                       "(Ingrese 1, 2, 3 o 4): ")

        if choose == "1":
            nombre = input("¿Cuál es tu nombre?").lower()
            apellido = input("¿Cuál es tu apellido?").lower()
            edad = input('¿Cuál es tu edad?')
            contrasena = input("Ingrese una contraseña")
            usuario_autenticado = login.new_user(manejador, nombre, apellido, edad, contrasena)
        elif choose == "2":
            nombre_usuario = input("Ingrese su nombre de usuario: ")
            contrasena = input("Ingrese su contraseña: ")
            usuario_autenticado = login.login(manejador, nombre_usuario, contrasena)
        elif choose == "3":
            if usuario_autenticado:
                login.show_user(manejador, usuario_autenticado.nombre_usuario)
            else:
                nombre_usuario = input("Ingrese un nombre de usuario: ")
                login.show_user(manejador, nombre_usuario)
        elif choose == "4":
            if usuario_autenticado:
                producto = input("Ingrese el nombre del producto que desea comprar: ")
                precio = float(input("Ingrese el precio del producto: "))
                usuario_autenticado.comprar(producto, precio)
            else:
                print("Debe iniciar sesión antes de realizar una compra.")
        else:
            print("Opción inválida")

        option = input("¿Desea realizar otra acción? (ingrese si/no): ").lower()

    print("Adiós")

if __name__ == "__main__":
    start()
