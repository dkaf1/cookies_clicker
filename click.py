import pygame, time, random
pygame.init()

WIDHT, HEIGHT = 1200, 900

screen = pygame.display.set_mode((WIDHT, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font('Kidmans.ttf', 50) 


bg_surf = pygame.transform.scale(pygame.image.load("bg.jpg").convert(), (WIDHT, HEIGHT))

cookie_pos = (WIDHT/4, HEIGHT/2+100)
cookies_surf = pygame.image.load("cookiePNG.png").convert_alpha()
cookies_rect = cookies_surf.get_rect(center = cookie_pos)

boutique_surf = pygame.image.load("boutique.png").convert_alpha()
boutique_rect = boutique_surf.get_rect(midbottom = (3*WIDHT/4, HEIGHT/3))

animation_list = []   

score = 0
k = 1

def animation(event, pos):
    surf = font.render(f'+ {k}', True, 50)
    rect = surf.get_rect(center = pos)
    while event:
        screen.blit(surf, rect)

while True:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and cookies_rect.collidepoint(mouse_pos):
            cookies_surf = pygame.transform.rotozoom(cookies_surf, 0, 1.3)
            cookies_rect = cookies_surf.get_rect(center = cookie_pos)
            animation_list.append(font.render(F"+ {k}", True, 'brown'))
            score += k*1
        else: 
            cookies_surf = pygame.image.load("cookiePNG.png").convert_alpha()
            cookies_rect = cookies_surf.get_rect(center = cookie_pos)

    score_surf = font.render(f"SCORE = {score}", True, 'BLACK')
    score_rect = score_surf.get_rect(midbottom = (WIDHT/4, HEIGHT/2-200))

    screen.blit(bg_surf, (0, 0))
    screen.blit(cookies_surf, cookies_rect)
    screen.blit(score_surf, score_rect)
    screen.blit(boutique_surf, boutique_rect)

    pygame.display.update()
    clock.tick(60)