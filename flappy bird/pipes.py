import random, pygame
from settings import WIDTH, HEIGHT, PIPE_GAP, PIPE_WIDTH, PIPE_SPEED, GROUND_HEIGHT, GREEN, DARK_GREEN

class Pipe:
    def __init__(self):
        self.x = WIDTH + 100
        self.gap_y = random.randint(150, HEIGHT - GROUND_HEIGHT - 150)
        self.passed = False
        
    def update(self):
        self.x -= PIPE_SPEED
       
    @property
    def top_rect(self):
        return pygame.Rect(self.x, 0, PIPE_WIDTH, self.gap_y - PIPE_GAP // 2)
        
    @property
    def bottom_rect(self):
        top = self.gap_y + PIPE_GAP // 2
        return pygame.Rect(self.x, top, PIPE_WIDTH, HEIGHT - GROUND_HEIGHT - top)
        
        
    def draw(self, screen):
        for rect in (self.top_rect, self.bottom_rect):
            pygame.draw.rect(screen, GREEN, rect)
            pygame.draw.rect(screen, DARK_GREEN, rect, 3)
            
    def offscreen(self):
        return self.x + PIPE_WIDTH < 0