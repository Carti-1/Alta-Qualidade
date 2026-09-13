from src.desconto import IDesconto

class StubSemDesconto(IDesconto):
    def calcular(self, valor: float) -> float:
        return 0  # Retorna sempre 0, simulando um cenário sem desconto