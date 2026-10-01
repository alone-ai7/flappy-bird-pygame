import pygame, sys
from settings import (WIDTH, HEIGHT, PIPE_INTERVAL, GROUND_HEIGHT, SKY, GROUND, DARK_GREEN, WHITE, BLACK)

from bird import Bird
from pipes import Pipe

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 40, bold=True)
small_font = pygame.font.SysFont("arial", 22)

SPAWN_PIPE = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_PIPE, PIPE_INTERVAL)

def draw_text(txt, fnt, y, color=WHITE):
    shadow = fnt.render(txt, True, BLACK)
    label = fnt.render(txt, True, color)
    x = WIDTH // 2 - label.get_width() // 2
    screen.blit(label, (x, y))
    
def main():
    bird = Bird()
    pipes = []
    
    score = 0
    best = 0 
    state = "ready"
    open = True
    
    while open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            flap_input = (
                (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)
                or event.type == pygame.MOUSEBUTTONDOWN
            )
            
            if flap_input:
                if state == "ready":
                    state = "playing"
                    bird.flap()
                elif state == "playing":
                    bird.flap()
                elif state == "dead":
                    bird.reset()
                    pipes.clear()
                    score = 0
                    state = "ready"
                    
            if event.type == SPAWN_PIPE and state == "playing":
                pipes.append(Pipe())
                
                
        if state == "playing":
            bird.update()
            for pipe in pipes:
                pipe.update()
                if not pipe.passed and pipe.x + pipe.top_rect.width < bird.x:
                    pipe.passed = True
                    score += 1
                if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect):
                    state = "dead"
            pipes = [p for p in pipes if not p.offscreen()]
            
            if bird.y + 12 >= HEIGHT - GROUND_HEIGHT or bird.y - 12 <= 0:
                state = "dead"
               
            best = max(best, score)
            
        screen.fill(SKY)
        for pipe in pipes:
            pipe.draw(screen)
        pygame.draw.rect(screen, GROUND, (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))
        pygame.draw.line(screen, DARK_GREEN, (0, HEIGHT - GROUND_HEIGHT), (WIDTH, HEIGHT - GROUND_HEIGHT), 4)
        bird.draw(screen)
        
        if state == "ready":
            draw_text("Flappy Bird", font, 150)
            draw_text("Press SPACE or click to flap", small_font, 220)
        elif state == "playing":
            draw_text(str(score), font, 40)
        else:
            draw_text("Game Over", font, 180)
            draw_text(f"Score: {score} Best: {best}", small_font, 240)
            draw_text("Press SPACE or click to retry", small_font, 275)
            
        pygame.display.flip()
        clock.tick(60)
        
if __name__ == "__main__":
    main()