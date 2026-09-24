from pathlib import Path
import sys

if __package__ in (None, ""):
    root = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(root))

from src.services.pedido_service import PedidoService
from src.models.desconto import DescontoVIP, DescontoNormal, DescontoPremium
from src.models.pedido import Pedido

if __name__ == "__main__":
    service = PedidoService()

    """Criando pedidos e aplicando descontos"""
    pedido1 = Pedido("Cliente A", DescontoNormal())
    pedido1.valor_original = 100.0

    pedido2 = Pedido("Cliente B", DescontoVIP())
    pedido2.valor_original = 200.0

    pedido3 = Pedido("Cliente C", DescontoPremium())
    pedido3.valor_original = 300.0

    service.adicionar_pedido(pedido1)
    service.adicionar_pedido(pedido2)
    service.adicionar_pedido(pedido3)

    service.processar_pedidos()