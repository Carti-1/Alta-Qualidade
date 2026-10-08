from src.app.entities.desconto import DescontoVIP, DescontoNormal, DescontoPremium
from src.app.entities.pedido import Pedido

class CriarPedido:
    def executar(self, cliente: str, valor_original: float, tipo_desconto: str) -> Pedido:
        if tipo_desconto == "normal":
            desconto = DescontoNormal()
        elif tipo_desconto == "vip":
            desconto = DescontoVIP()
        elif tipo_desconto == "premium":
            desconto = DescontoPremium()
        else:
            raise ValueError("Tipo de desconto inválido")
        return Pedido(cliente, valor_original, desconto)