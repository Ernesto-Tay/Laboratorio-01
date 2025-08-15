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

class Impresora(Dispositivo):
    def __init__(self,ID,marca,modelo,direccion_ip,tipo_impresion):
        super().__init__(ID,marca,modelo,direccion_ip)
        self.tipo_impresion = tipo_impresion

