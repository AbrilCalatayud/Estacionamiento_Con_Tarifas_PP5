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

    def agregar_modificador(self, modificador):
        if not isinstance(modificador, ModificadorTarifa):
            raise TypeError("Se ha rechazado el modificador, porque no cumple con el contrato")

        self._modificadores.append(modificador)

    @property
    def modificadores(self):
        return tuple(self._modificadores)

    def total(self, tarifa_por_hora):
        total = tarifa_por_hora * self.horas

        for modificador in self._modificadores:
            total = modificador.aplicar(total, self.horas)

        return total

class EstadiaMensual(Estadia):
    def __init__(self, patente, horas, porcentaje_descuento):
        super().__init__(patente, horas)

        if porcentaje_descuento <= 0 or porcentaje_descuento >= 100:
            raise ValueError("El porcentaje de descuento debe ser positivo y menor a 100")

        self.porcentaje_descuento = porcentaje_descuento / 100

    def total(self, tarifa_por_hora):
        return super().total(tarifa_por_hora) * (1 - self.porcentaje_descuento)

def facturar(estadias, tarifa_por_hora):
    total_general = 0.0

    for estadia in estadias:
        total_general += estadia.total(tarifa_por_hora)

    return total_general