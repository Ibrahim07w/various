import pygame
import time
import random

pygame.font.init()
W, H = 800, 600
PW, PH = 40, 30
SW, SH = 10, 15
VELOCITY = 4
STAR_VELOCITY = 2
LIFES = 3
background = pygame.transform.scale(pygame.image.load('C:/Users/ibrah/Downloads/bg.jpeg'), (W, H))
window = pygame.display.set_mode((W, H))
pygame.display.set_caption('space dodger')
FONT = pygame.font.SysFont('comicsans', 30)

def draw(player, elapsed_time, stars, lifes):
    global W
    window.blit(background, (0, 0))
    time_text = FONT.render(f'{round(elapsed_time)}s', 1, 'white')
    life_text = FONT.render(f'{lifes} lifes left', 1, 'white')
    window.blit(time_text, (10, 10))
    window.blit(life_text, (W - life_text.get_width() - 10, 10))
    pygame.draw.rect(window, 'red', player)
    for star in stars:
        pygame.draw.rect(window, 'white', star)
    pygame.display.update()

def main():
    global STAR_VELOCITY
    global LIFES
    run = True
    start_time = time.time()
    elapsed_time = 0
    player = pygame.Rect(W//2, H-PH, PW, PH)
    clock = pygame.time.Clock()
    stars_timer = 2000
    star_count = 0
    stars = []
    stars_number = 3
    lost = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        stars_number = min(5, stars_number + elapsed_time // 60)
        STAR_VELOCITY = min(5, STAR_VELOCITY + elapsed_time // 60)

        if star_count > stars_timer:
            for _ in range(int(stars_number)):
                star_x = random.randint(0, W - SW)
                star = pygame.Rect(star_x, -SH, SW, SH)
                stars.append(star)
            stars_timer = max(200, stars_timer - 40)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - VELOCITY >= 0:
            player.x -= 5
        if keys[pygame.K_RIGHT] and player.x + VELOCITY + PW <= W:
            player.x += 5

        for star in stars:
            star.y += STAR_VELOCITY
            if star.y > H:
                stars.remove(star)
            elif star.colliderect(player):
                stars.remove(star)
                LIFES -= 1
                if LIFES == 0:
                    lost = True
                    break

        if lost:
            lose_text = FONT.render('you lost', 1, 'white')
            window.blit(lose_text, (W/2-lose_text.get_width()/2 , H/2-lose_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars, LIFES)
    pygame.quit()

if __name__ == '__main__':
    main()