from src.desconto import IDesconto


class StubSemDesconto(IDesconto):
    def calcular(self, valor: float) -> float:
        return 0


# STUB - Tela (não renderiza)
class StubScreen:
    def __init__(self):
        self.width = 800
        self.height = 600
    
    def blit(self, image, rect):
        pass
    
    def fill(self, color):
        pass
    
    def get_rect(self):
        class Rect:
            right = 800
            midbottom = (400, 600)
        return Rect()

