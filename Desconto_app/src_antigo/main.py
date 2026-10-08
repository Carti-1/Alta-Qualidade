from pathlib import Path
import sys  

if __package__ in (None, ""):
    root = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(root))

from src_antigo.repositories.pedido_repository import PedidoRepository
from src_antigo.controllers.pedido_controller import PedidoController
from src_antigo.services.pedido_service import PedidoService
from src_antigo.database.connection import DatabaseConnection
from src_antigo.models.desconto import DescontoVIP, DescontoNormal, DescontoPremium
from src_antigo.models.pedido import Pedido

if __name__ == "__main__":
    database = DatabaseConnection()
    repo = PedidoRepository(database)
    service = PedidoService(repo)
    controller = PedidoController(service)

    pedido1 = Pedido("Cliente 1", DescontoVIP())
    pedido1.valor_original = 100.0

    pedido2 = Pedido("Cliente 2", DescontoVIP())
    pedido2.valor_original = 100.0

    pedido3 = Pedido("Cliente 3", DescontoPremium())
    pedido3.valor_original = 100.0

    controller.adicionar_pedido(pedido1)
    controller.adicionar_pedido(pedido2)
    controller.adicionar_pedido(pedido3)

    controller.processar_pedidos()

    pedidos = repo.listar_pedidos()

    for pedido in pedidos:
        print(f"Cliente: {pedido.cliente}")
        print(f"Valor final: {pedido.valor_final(pedido.valor_original)}")
