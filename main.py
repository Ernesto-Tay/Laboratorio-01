dispositivos = {}
class Dispositivo:
    def __init__(self,ID, marca,modelo,direccion_ip):
        self.ID = ID
        self.marca = marca
        self.modelo = modelo
        self.direccion_ip = direccion_ip

class Computadora(Dispositivo):
    def __init__(self,ID,marca,modelo,direccion_ip,usuario_asignado,sistema_operativo):
        super().__init__(ID,marca,modelo,direccion_ip)
        self.usuario_asignado = usuario_asignado
        self.sistema_operativo = sistema_operativo
        self.tipo = "computadora"

class Impresora(Dispositivo):
    def __init__(self,ID,marca,modelo,direccion_ip,tipo_impresion):
        super().__init__(ID,marca,modelo,direccion_ip)
        self.tipo_impresion = tipo_impresion
        self.tipo = "impresora"

while True:
    print("\n\n----------------SISTEMA DE MANEJO DE DISPOSITIVOS---------------\n1. Registrar un dispositivo\n2. Mostrar todos los dispositivos\n3. Eliminar un dispositivo\n4. Salir")
    select = input("Seleccione una opción: ")
    match select:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            print("Saliendo...")
            break
        case _:
            print("Opción inválida, intente nuevamente")