def IDDupeError(Exception):
    "Pasa cuando una ID ingresada ya existe"
    pass
def IDNegativeError(Exception):
    "Pasa cuando una ID es negativa"
    pass
def IDInexistError(Exception):
    "Pasa cuando una ID buscada no existe"
    pass

dispositivos = {}
class Dispositivo:
    def __init__(self, marca,modelo,direccion_ip):
        self.marca = marca
        self.modelo = modelo
        self.direccion_ip = direccion_ip

class Computadora(Dispositivo):
    def __init__(self,marca,modelo,direccion_ip,usuario_asignado,sistema_operativo):
        super().__init__(marca,modelo,direccion_ip)
        self.usuario_asignado = usuario_asignado
        self.sistema_operativo = sistema_operativo
        self.tipo = "computadora"

class Impresora(Dispositivo):
    def __init__(self,marca,modelo,direccion_ip,tipo_impresion):
        super().__init__(marca,modelo,direccion_ip)
        self.tipo_impresion = tipo_impresion
        self.tipo = "impresora"

while True:
    print("\n\n----------------SISTEMA DE MANEJO DE DISPOSITIVOS---------------\n1. Registrar un dispositivo\n2. Mostrar todos los dispositivos\n3. Eliminar un dispositivo\n4. Salir")
    select = input("Seleccione una opción: ")
    match select:
        case "1":
            while True:
                try:
                    ID = int(input("\nIngresa la ID del dispositivo: "))
                    marca = input("Marca del dispositivo: ").capitalize()
                    tipo = input("Tipo de dispositivo (Computadora/Impresora): ").capitalize()
                    modelo = input("Modelo del dispositivo: ").capitalize()
                    direccion_ip = input("Direccion IP del dispositivo: ")
                    if any( ex_ID == ID for ex_ID in dispositivos.keys()):
                        raise IDDupeError("La ID ingresada ya está en uso")
                    elif ID < 0:
                        raise IDNegativeError("El valor de la ID no puede ser negativo")

                    if tipo == "Computadora":
                        usuario = input("Usuario asignado: ")
                        sistema = input("Sistema operativo: ")
                        dispositivos[ID] : {
                            Computadora(marca,modelo,direccion_ip,usuario,sistema)
                        }

                    elif tipo == "Impresora":
                        impresion = input("Tipo de impresión: ").capitalize()
                        dispositivos[ID] : {
                            Impresora(marca,modelo,direccion_ip,impresion)
                        }
                except IDDupeError as e:
                    print(e)
                except IDNegativeError as e:
                    print(e)
                except ValueError:
                    print("Ingrese solo números en la ID")


        case "2":
            if not dispositivos:
                print("No hay dispositivos registrados aún")
            else:
                Comp = False
                Printers = False
                if any(dispositivo.tipo == "Computadora" for dispositivo in dispositivos.values()):
                    Comp = True
                if any(dispositivo.tipo == "Impresora" for dispositivo in dispositivos.values()):
                    Printers = True
                for id, dispositivo in dispositivos.items():
                    if Comp:
                        print("\n---COMPUTADORAS INGRESADAS---")
                        if dispositivo.tipo == "Computadora":
                            print(f"ID: {id}\nMARCA: {dispositivo.marca}\nMODELO: {dispositivo.modelo}\nDIRECCION IP: {dispositivo.direccion_ip}\nUSUARIO: {dispositivo.usuario_asignado}\nSISTEMA OPERATIVO: {dispositivo.sistema_operativo}")

                    if Printers:
                        print("\n---IMPRESSION INGRESADAS---")
                        if dispositivo.tipo == "Impresora":
                            print(
                                f"ID: {id}\nMARCA: {dispositivo.marca}\nMODELO: {dispositivo.modelo}\nDIRECCION IP: {dispositivo.direccion_ip}\nTIPO DE IMPRESION: {dispositivo.tipo_impresion}")


        case "3":
            if not dispositivos:
                print("No hay dispositivos ingresados")
            else:
                while True:
                    try:
                        ID = int(input("\nIngresa la ID del dispositivo a eliminar: "))
                        if not dispositivos.get(ID):
                            raise IDInexistError("El dispositivo buscado no existe")
                        else:
                            del dispositivos[ID]
                            break
                    except ValueError:
                        print("Ingrese una ID válida (solo números enteros)")
                    except Exception as e:
                        print("Error inesperado", e)


        case "4":
            print("Saliendo...")
            break
        case _:
            print("Opción inválida, intente nuevamente")