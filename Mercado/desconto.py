from abc import ABC, abstractmethod

#Classe abstrata define o contrato para os descontos, garantindo que todas as subclasses implementem o método calcular.
class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass

class DescontoNormal(Desconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.1  # Aplica um desconto de 10%

class DescontoVIP(Desconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.2  # Aplica um desconto de 20%

class DescontoPremium(Desconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.3  # Aplica um desconto de 30%

def main():
    valor = 100.0  # Valor original do produto

    desconto_normal = DescontoNormal()
    desconto_vip = DescontoVIP()
    desconto_premium = DescontoPremium()

    print(f"Desconto Normal: {desconto_normal.calcular(valor):.2f}")
    print(f"Desconto VIP: {desconto_vip.calcular(valor):.2f}")
    print(f"Desconto Premium: {desconto_premium.calcular(valor):.2f}")

if __name__ == "__main__":
    main()
