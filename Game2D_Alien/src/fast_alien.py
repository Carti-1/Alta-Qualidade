from alien import Alien

class FastAlien(Alien):
    """Alienígena mais rápido."""

    def update(self) -> None:
        """Move o alienígena para a direita ou para a esquerda, dependendo da direção da frota."""
        self.x += (self.settings.alien_speed * 2) * self.settings.fleet_direction
        self.rect.x = self.x
        