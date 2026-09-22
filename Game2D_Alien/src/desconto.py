# Interfaces segregadas (ISP - Interface Segregation Principle)
class IDesconto:
    def calcular(self, valor: float) -> float:
        raise NotImplementedError("Subclasses devem implementar o método calcular.")

class ICupom:
    def aplicar_cupom(self, codigo: str) -> bool:
        raise NotImplementedError("Subclasses devem implementar o método aplicar_cupom.")
    
class IVIP:
    def validar_usuario_vip(self, usuario: str) -> bool:
        raise NotImplementedError("Subclasses devem implementar o método validar_usuario_vip.")


# Classes de Desconto (LSP - Liskov Substitution Principle)
class DescontoNormal(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.1  # 10% de desconto

class DescontoVIP(IDesconto, ICupom, IVIP):
    def calcular(self, valor: float) -> float:
        return valor * 0.2  # 20% de desconto

    def aplicar_cupom(self, codigo: str) -> bool:
        return True  # Valida o cupom

    def validar_usuario_vip(self, usuario: str) -> bool:
        return usuario == "vip"

class DescontoPremium(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.3  # 30% de desconto


# Funções polimórficas clientes que dependem de abstrações (LSP & ISP)
def aplicar_desconto(desconto: IDesconto, valor: float) -> float:
    return desconto.calcular(valor)

def aplicar_cupom(cupom: ICupom, codigo: str) -> bool:
    return cupom.aplicar_cupom(codigo)


# Classe com Inversão de Dependência (DIP - Dependency Inversion Principle)
class Pedido:
    def __init__(self, desconto: IDesconto):
        self.desconto = desconto

    def total(self, valor: float) -> float:
        return valor - self.desconto.calcular(valor)


if __name__ == "__main__":
    valor = 100.0  # Valor original do produto

    normal = DescontoNormal()
    vip = DescontoVIP()
    premium = DescontoPremium()

    # Demonstração LSP:
    # Qualquer subclasse de IDesconto pode ser usada onde IDesconto é esperado
    print("--- Demonstração LSP (Liskov Substitution Principle) ---")
    print("Desconto Normal:", aplicar_desconto(normal, valor))
    print("Desconto VIP:", aplicar_desconto(vip, valor))
    print("Desconto Premium:", aplicar_desconto(premium, valor))

    # Demonstração ISP:
    # Classes implementam apenas as interfaces necessárias
    print("\n--- Demonstração ISP (Interface Segregation Principle) ---")
    print("Cupom VIP:", aplicar_cupom(vip, "DESC10"))
    print("Validação VIP:", vip.validar_usuario_vip("vip"))

    # Demonstração DIP:
    # Pedido depende de abstração (IDesconto) e não de implementação concreta
    print("\n--- Demonstração DIP (Dependency Inversion Principle) ---")
    pedido_normal = Pedido(normal)
    pedido_vip = Pedido(vip)
    pedido_premium = Pedido(premium)

    print("Total com Desconto Normal:", pedido_normal.total(valor))
    print("Total com Desconto VIP:", pedido_vip.total(valor))
    print("Total com Desconto Premium:", pedido_premium.total(valor))  