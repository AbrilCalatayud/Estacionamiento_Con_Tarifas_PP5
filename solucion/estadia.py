from solucion.estacionamiento import ModificadorTarifa

class Estadia:
    def __init__(self, patente, horas):
        if not patente.strip():
            raise ValueError("La patente no puede estar vacía")
        if horas <= 0:
            raise ValueError("Las horas deben ser positivas")

        self.patente = patente
        self.horas = horas
        self._modificadores = []