from doubles import StubSemDesconto
from src.desconto import Pedido

#def test_pedido_com_stub():
    #pedido = Pedido(StubSemDesconto())
    #assert = pedido.total(100) == 100, "O total deve ser 100, pois o stub não aplica desconto"

def test_pedido_com_mock_desconto(mocker):

    mock_desconto = mocker.Mock() #cria um mock do objeto de desconto
    mock_desconto.calcular.return_value = 10  # Simula um desconto de 10

    pedido = Pedido(mock_desconto)
    resultado = pedido.total(100)
    assert resultado == 90, "O total deve ser 90, pois o mock aplica um desconto de 10"

    mock_desconto.calcular.assert_called() 
    mock_desconto.calcular.assert_called_once_with(100)  # Verifica se o método calcular foi chamado com o valor correto
    assert mock_desconto.calcular.call_count == 1, "O método calcular deve ser chamado exatamente uma vez"