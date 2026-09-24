from abc import ABC, abstractmethod

class IDesconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass

class DescontoNormal(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.1

class DescontoVIP(IDesconto):
    def calcular(self, valor:float) -> float:
        return valor * 0.2

class DescontoPremium(IDesconto):
    def calcular(self, valor:float) -> float:
            return valor * 0.3

