from doubles import StubSemDesconto, StubScreen
from src.desconto import Pedido

def test_pedido_com_stub():
    pedido = Pedido(StubSemDesconto())
    assert pedido.total(100) == 100, "O total deve ser 100, pois o stub não aplica desconto"

def test_pedido_com_mock_desconto(mocker):

    mock_desconto = mocker.Mock() #cria um mock do objeto de desconto
    mock_desconto.calcular.return_value = 10  # Simula um desconto de 10

    pedido = Pedido(mock_desconto)
    resultado = pedido.total(100)
    assert resultado == 90, "O total deve ser 90, pois o mock aplica um desconto de 10"

    mock_desconto.calcular.assert_called() 
    mock_desconto.calcular.assert_called_once_with(100)  # Verifica se o método calcular foi chamado com o valor correto
    assert mock_desconto.calcular.call_count == 1, "O método calcular deve ser chamado exatamente uma vez"

def test_screen_com_stub():
    
    screen = StubScreen()  # Cria um stub da tela
    screen.blit(None, None)  # Simula renderizar
    screen.fill((255, 255, 255)) 
    
    assert screen.width == 800, "A largura da tela deve ser 800"
    assert screen.height == 600, "A altura da tela deve ser 600"

def test_nave_com_mock(mocker):
    """Mock verifica se os métodos da nave foram chamados."""
    
    mock_screen = mocker.Mock()  # Cria um mock da tela
    mock_ship = mocker.Mock()  # Cria um mock da nave
    mock_ship.update.return_value = None  
    mock_ship.blitme.return_value = None  
    
    # Simula chamadas aos métodos da nave
    mock_ship.update()
    resultado = mock_ship.update()
    
    # Verifica se update foi chamado
    mock_ship.update.assert_called()
    assert mock_ship.update.call_count == 2, "O método update() deve ser chamado 2 vezes"
    
    # Verifica blitme
    mock_ship.blitme()
    mock_ship.blitme.assert_called()
    assert mock_ship.blitme.call_count == 1, "O método blitme() deve ser chamado uma vez"