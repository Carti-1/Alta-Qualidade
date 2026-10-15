from pathlib import Path
import sys


# Permite executar tanto `python src/main.py` quanto `python -m src.main`.
if __package__ in (None, ""):
    raiz_projeto = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(raiz_projeto))

from src.app.adapters.controllers.pedido_controller import PedidoController
from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.presenters.pedido_presenter import PedidoPresenter
from src.app.use_cases.criar_pedido import CriarPedido


def exibir_pedido(pedido: dict) -> None:
    print(f"Cliente: {pedido['cliente']}")
    print(f"Valor original: R$ {pedido['valor_original']:.2f}")
    print(f"Desconto: R$ {pedido['valor_desconto']:.2f}")
    print(f"Valor final: R$ {pedido['valor_final']:.2f}")
    print(f"Tipo de desconto: {pedido['tipo_desconto']}")


def criar_pedido(controller: PedidoController) -> None:
    cliente = input("Nome do cliente: ").strip()
    if not cliente:
        print("O nome do cliente não pode ficar vazio.")
        return

    try:
        valor_original = float(input("Valor original do pedido: R$ ").replace(",", "."))
    except ValueError:
        print("Informe um valor numérico válido.")
        return

    if valor_original <= 0:
        print("O valor do pedido deve ser maior que zero.")
        return

    tipo_desconto = input("Tipo de desconto (normal, vip ou premium): ").strip().lower()

    try:
        pedido = controller.criar_pedido(cliente, valor_original, tipo_desconto)
    except ValueError as erro:
        print(f"Não foi possível criar o pedido: {erro}")
        return

    print("\nPedido criado:")
    exibir_pedido(pedido)


def listar_pedidos(controller: PedidoController) -> None:
    pedidos = controller.listar_pedidos()

    if not pedidos:
        print("Nenhum pedido foi realizado ainda.")
        return

    print("\nPedidos realizados:")
    for indice, pedido in enumerate(pedidos, start=1):
        print(f"\nPedido {indice}")
        exibir_pedido(pedido)


def main() -> None:
    banco = MemoryDatabase()
    repositorio = MemoryPedidoRepository(banco)
    caso_de_uso = CriarPedido(repositorio)
    presenter = PedidoPresenter()
    controller = PedidoController(caso_de_uso, presenter)

    while True:
        print("\n=== Gestão de pedidos ===")
        print("1. Criar pedido")
        print("2. Listar pedidos")
        print("0. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            criar_pedido(controller)
        elif opcao == "2":
            listar_pedidos(controller)
        elif opcao == "0":
            print("Encerrando.")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 0.")


if __name__ == "__main__":
    main()
