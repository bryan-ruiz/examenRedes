
class Tweet:

    def __init__(self,hora,usuario, datos):
        self.hora = hora
        self.usuario=usuario
        self.datos=datos

    def getHora(self):
        return self.hora

    def getUsuario(self):
        return self.usuario

    def getDatos(self):
        return self.datos
