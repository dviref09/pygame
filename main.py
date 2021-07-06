from typing import Text
import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pygame tutorial")

#### \/
#### \/
##### VAR
#### /\
#### /\
BLUE_LIGHT = (46, 89, 134)
FPS = 60

def draw_window():
    WIN.fill(BLUE_LIGHT)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window()
    
    pygame.quit()

if __name__ == "__main__":
    main()