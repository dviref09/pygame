import os
import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pygame tutorial")

#################
#      VAR      #
#################

BLUE_LIGHT = (46, 89, 134)
BLACK = (0, 0, 0)

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

FPS = 60
VEL = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 41

# IMAGE LOAD #
BACKGROUND_IMAGE = pygame.image.load(os.path.join("Assets", "space.png"))
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_yellow.png")
)
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_red.png"))
# ------------------ #

# CHANGE IMAGES #
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,
                           (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),
    -90,
)
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE,
                           (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90
)
# ------------------ #


def draw_window(red, yellow):
    WIN.blit(BACKGROUND_IMAGE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def red_handle_movement(keys_pressed, red):
    # RIGHT
    if keys_pressed[pygame.K_d] and red.x + VEL + red.width < BORDER.x:
        red.x += VEL
    elif keys_pressed[pygame.K_a] and red.x - VEL > 0:  # LEFT
        red.x -= VEL
    elif keys_pressed[pygame.K_w] and red.y - VEL > 0:  # UP
        red.y -= VEL
    elif keys_pressed[pygame.K_s] and red.y + VEL + red.height < HEIGHT - 10:  # DOWN
        red.y += VEL


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_RIGHT] and yellow.x + VEL + yellow.width < WIDTH:  # RIGHT
        yellow.x += VEL
    elif keys_pressed[pygame.K_LEFT] and yellow.x - VEL > BORDER.x + BORDER.width:  # LEFT
        yellow.x -= VEL
    elif keys_pressed[pygame.K_UP] and yellow.y - VEL > 0:  # UP
        yellow.y -= VEL
    elif keys_pressed[pygame.K_DOWN] and yellow.y + VEL + yellow.height < HEIGHT - 10:  # DOWN
        yellow.y += VEL


def main():
    red = pygame.Rect(225, 250, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(675, 250, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        red_handle_movement(keys_pressed, red)
        yellow_handle_movement(keys_pressed, yellow)

        draw_window(red, yellow)

    pygame.quit()


if __name__ == "__main__":
    main()
