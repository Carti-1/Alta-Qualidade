from src_antigo.models.pedido import Pedido
from src_antigo.database.connection import DatabaseConnection

class PedidoRepository:
    """Classe de repositório para armazenar e gerenciar pedidos."""

    def __init__(self, database: DatabaseConnection):
        self.dataabse = database

    def adicionar_pedido(self, pedido: Pedido):
        self.dataabse.pedidos.append(pedido)

    def listar_pedidos(self):
        return self.dataabse.pedidos

    