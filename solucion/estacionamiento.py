from abc import ABC, abstractmethod

class ModificadorTarifa(ABC):
    @abstractmethod
    def aplicar(self, total: float, horas: int) -> float:
        """Devuelve el nuevo total."""

class Nocturna(ModificadorTarifa):
    def aplicar(self, total, horas):
        return total + 200 * horas

class FinDeSemana(ModificadorTarifa):
    def aplicar(self, total, horas):
        return total * 1.5