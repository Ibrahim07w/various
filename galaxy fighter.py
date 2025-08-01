import pygame
pygame.font.init()

W, H = 900, 600
window = pygame.display.set_mode((W, H))
pygame.display.set_caption('space fighter')
red_image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('C:/Users/ibrah/Downloads/spaceship_red.png'), (50, 40)), 90)
yellow_image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('C:/Users/ibrah/Downloads/spaceship_yellow.png'), (50, 40)), 270)
VELOCITY = 4
BULLET_VELOCITY = 8
BORDER = pygame.Rect(W/2-2, 0, 4, H)
MAX_BULLETS = 5
RED_HIT = pygame.USEREVENT + 1
YELLOW_HIT = pygame.USEREVENT + 2
FONT = pygame.font.SysFont('comicsans', 40)
background = pygame.transform.scale(pygame.image.load('C:/Users/ibrah/Downloads/bg.jpeg'), (W, H))

def draw(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    window.blit(background, (0,0))
    pygame.draw.rect(window, (0,0,0), BORDER)
    red_health_text = FONT.render(f'health {red_health}', 1, 'white')
    yellow_health_text = FONT.render(f'health {yellow_health}', 1, 'white')
    window.blit(red_health_text, (10, 10))
    window.blit(yellow_health_text, (W-yellow_health_text.get_width()-10, 10))
    window.blit(red_image, (red.x, red.y))
    window.blit(yellow_image, (yellow.x, yellow.y))
    for bullet in red_bullets:
        pygame.draw.rect(window, (255, 0, 0), bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(window, (255, 255, 0), bullet)
    pygame.display.update()

def draw_winner(text):
    winner_text = FONT.render(text, 1, 'white')
    window.blit(winner_text, (W/2 - winner_text.get_width()/2, H/2 - winner_text.get_width()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def red_movement(keys, red):
    if keys[pygame.K_a] and red.x - VELOCITY >= 0:
        red.x -= VELOCITY
    if keys[pygame.K_d] and red.x + VELOCITY + 40 <= W/2-2:
        red.x += VELOCITY
    if keys[pygame.K_w] and red.y - VELOCITY >= 0:
        red.y -= VELOCITY
    if keys[pygame.K_s] and red.y + VELOCITY + 50 <= H:
        red.y += VELOCITY
def yellow_movement(keys, yellow):
    if keys[pygame.K_LEFT] and yellow.x - VELOCITY >= W/2+2:
        yellow.x -= VELOCITY
    if keys[pygame.K_UP] and yellow.y - VELOCITY >= 0:
        yellow.y -= VELOCITY
    if keys[pygame.K_RIGHT] and yellow.x + VELOCITY + 50 <= W:
        yellow.x += VELOCITY
    if keys[pygame.K_DOWN] and yellow.y +VELOCITY + 50 <= H:
        yellow.y += VELOCITY
    
def handel_bullets(red_bullets, yellow_bullets, red, yellow):
    for bullet in red_bullets:
        bullet.x += BULLET_VELOCITY
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            red_bullets.remove(bullet)
        if bullet.x >= W:
            red_bullets.remove(bullet)
    for bullet in yellow_bullets:
        bullet.x -= BULLET_VELOCITY
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            yellow_bullets.remove(bullet)
        if bullet.x <= 0:
            yellow_bullets.remove(bullet)

def main():
    run = True
    clock = pygame.time.Clock()
    red = pygame.Rect(200, 300, 50, 40)
    yellow = pygame.Rect(700, 300, 50, 40)
    red_bullets, yellow_bullets = [], []
    red_health = 10
    yellow_health = 10
    winner_text = ''

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x + red.width, red.y + red.height // 2 - 2, 10, 4)
                    red_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x, yellow.y + yellow.height // 2 - 2, 10, 4)
                    yellow_bullets.append(bullet)
            if event.type == RED_HIT:
                yellow_health -= 1
            if event.type == YELLOW_HIT:
                red_health -= 1
        if red_health == 0:
            winner_text = 'yellow wins'
        if yellow_health == 0:
            winner_text = 'red_wins'

        keys = pygame.key.get_pressed()
        red_movement(keys, red)
        yellow_movement(keys, yellow)
        handel_bullets(red_bullets, yellow_bullets, red, yellow)
        draw(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

        if winner_text:
            draw_winner(winner_text)
    pygame.quit()

if __name__ == '__main__':
    main()