import pytest
from src.desconto import DescontoNormal, DescontoVIP, DescontoPremium   

def test_desconto_normal():
    desconto = DescontoNormal()
    valor_original = 100.0
    resultado = desconto.calcular(100)
    resultado = desconto.calcular(valor_original)
    assert resultado == 10, f"Esperado 10, mas obteve {resultado}"

# Teste desconto VIP com fixture(prepara o objeto desconto_vip para ser usado nos testes):
@pytest.fixture
def desconto_vip():
    return DescontoVIP()

def test_desconto_vip_100(desconto_vip):
    assert desconto_vip.calcular(100) == 20, "Desconto VIP deve ser 20% do valor original"

def test_desconto_vip_200(desconto_vip):
    assert desconto_vip.calcular(200) == 40, "Desconto VIP deve ser 20% do valor original"


# Teste desconto premium com parametrize(roda o mesmo teste várias vezes com dados diferentes):
@pytest.mark.parametrize("valor, esperado", [
    (100, 30),
    (200, 60),
    (300, 90),
])

def test_desconto_premium(valor, esperado):
    desconto = DescontoPremium()
    resultado = desconto.calcular(valor)
    assert resultado == esperado, f"Esperado {esperado}, mas obteve {resultado}"