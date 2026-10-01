import pygame
from settings import GRAVITY, FLAP_STRENGTH, YELLOW, WHITE, BLACK, ORANGE

class Bird:
    def __init__(self, x=70): #x=70 is the starting pos of the bird
        self.x = x
        self.reset()
        
    def reset(self):
        self.y = 300
        self.vel = 0
        
    def flap(self):
        self.vel = FLAP_STRENGTH #-8
        
    def update(self):
        self.vel += GRAVITY # -8 + 0.5
        self.y += self.vel # 300 + 0
        
    @property
    def rect(self):
        return pygame.Rect(self.x - 15, self.y - 12,30,24)
        
    def draw(self, screen):
        angle = max(-30, min(-self.vel * 4, 0)) if self.vel < 0 else max(-90, -self.vel * 4)
        
        surf = pygame.Surface((40, 30), pygame.SRCALPHA)
        pygame.draw.ellipse(surf, YELLOW, (5, 3, 30, 24))
        pygame.draw.circle(surf, WHITE, (28, 11), 5)
        pygame.draw.circle(surf, BLACK, (30, 11), 2)
        pygame.draw.polygon(surf, ORANGE, [(33, 15), (40, 18), (33, 22)])
        
        rotated = pygame.transform.rotate(surf, angle)
        screen.blit(rotated, rotated.get_rect(center=(self.x, self.y)))
