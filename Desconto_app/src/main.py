from pathlib import Path
import sys

if __package__ in (None, ""):
    root = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(root))

from src.repositories.pedido_repository import PedidoRepository
from src.controllers.pedido_controller import PedidoController
from src.services.pedido_service import PedidoService
from src.database.connection import DatabaseConnection
from src.models.desconto import DescontoVIP, DescontoNormal, DescontoPremium
from src.models.pedido import Pedido

if __name__ == "__main__":
    database = DatabaseConnection()
    repo = PedidoRepository(database)
    service = PedidoService(repo)
    controller = PedidoController(service)

    pedido1 = Pedido(cliente="Cliente B", desconto= DescontoVIP())
    pedido1.valor_original = 200.0

    pedido2 = Pedido(cliente="Cliente B", desconto= DescontoVIP())
    pedido2.valor_original = 200.0

    pedido3 = Pedido(cliente="Cliente C", desconto= DescontoPremium())
    pedido3.valor_original = 300.0

    controller.adicionar_pedido(pedido1)
    controller.adicionar_pedido(pedido2)
    controller.adicionar_pedido(pedido3)

    controller.processar_pedidos()

    pedidos = repo.listar_pedidos()

    for pedido in pedidos:
        print(f"Cliente: {pedido.cliente}")
        print(f"Valor final: {pedido.valor_final(pedido.valor_original)}")
