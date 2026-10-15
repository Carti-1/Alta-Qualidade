from src.app.entities.desconto import DescontoVIP, DescontoNormal, DescontoPremium
from src.app.entities.pedido import Pedido
from src.app.gateways.pedido_gateway import IPedidoGateway

class CriarPedido:

    def __init__(self, pedido_gateway: IPedidoGateway):
        self.pedido_gateway = pedido_gateway

    def executar(self, cliente: str, valor_original: float, tipo_desconto: str) -> Pedido:
        if tipo_desconto == "normal":
            desconto = DescontoNormal()
        elif tipo_desconto == "vip":
            desconto = DescontoVIP()
        elif tipo_desconto == "premium":
            desconto = DescontoPremium()
        else:
            raise ValueError("Tipo de desconto inválido")

        pedido = Pedido(cliente, valor_original, desconto)
        self.pedido_gateway.salvar(pedido)

        return pedido

    def listar_pedidos(self) -> list[Pedido]:
        return self.pedido_gateway.listar()