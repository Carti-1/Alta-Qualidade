import pygame
from bullet import Bullet 

class BulletManager:

    def __init__(self, screen, settings, ship) -> None:
        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.bullets = pygame.sprite.Group()

    def _fire_bullet(self) -> None:
        """Dispara um projétil se o limite de projéteis ainda não tiver sido alcançado.[cite: 1]"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self.screen, self.settings, self.ship)
            self.bullets.add(new_bullet)

    def _update_bullets(self, aliens) -> None:
        """Atualiza a posição dos projéteis e se livra dos projéteis antigos.[cite: 1]"""
        self.bullets.update()
        self._remove_offscreen_bullets()
        self._check_bullet_alien_collisions(aliens)

    def _remove_offscreen_bullets(self) -> None:
        """Remove os projéteis que desapareceram da tela.[cite: 1]"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_bullet_alien_collisions(self, aliens) -> None:
        """Verifica colisões entre projéteis e alienígenas.[cite: 1]"""
        pygame.sprite.groupcollide(self.bullets, aliens, True, True)