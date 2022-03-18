import string


class Atributos:
    def __init__(self, tipo: string, valor, fondo, valores, nombre, evento) -> None:
        self.tipo = tipo
        self.valor = valor
        self.fondo = fondo
        self.valores = valores
        self.nombre = nombre
        self.evento = evento
        pass