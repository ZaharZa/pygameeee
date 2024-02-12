import pygame
import random

print('Ваше имя? Напишите ниже пожалуйста ↓')
name = input()
print('Выбери уровень: 1 - 3')
a = int(input())
w = ' level - '

if a == 1:
    pygame.init()
    width, height = 1500, 1000
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Увернись')

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)

    player_size = 50
    player_x = width // 2
    player_y = height - player_size - 20
    player_speed = 5

    enemy_size = 50
    enemy_x = random.randint(0, width - enemy_size)
    enemy_y = 0
    enemy_speed = 5

    score = 0
    font = pygame.font.Font(None, 36)

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < width - player_size:
            player_x += player_speed

        enemy_y += enemy_speed
        if enemy_y > height:
            enemy_y = 0
            enemy_x = random.randint(0, width - enemy_size)
            score += 1

        if player_y < enemy_y + enemy_size and player_y + player_size > enemy_y:
            if player_x < enemy_x + enemy_size and player_x + player_size > enemy_x:
                running = False

        screen.fill(black)
        pygame.draw.rect(screen, white, (player_x, player_y, player_size, player_size))
        pygame.draw.rect(screen, red, (enemy_x, enemy_y, enemy_size, enemy_size))

        score_text = font.render('Счет: ' + str(score), True, white)
        screen.blit(score_text, (10, 10))
        lvl_text = font.render('Уровень: 1', True, white)
        screen.blit(lvl_text, (10, 35))

        pygame.display.flip()
        clock.tick(60)

    game_over_text = font.render('Game Over', True, white)
    screen.blit(game_over_text, (width // 2 - 100, height // 2 - 18))
    pygame.display.flip()

    pygame.time.wait(2000)

if a == 2:
    pygame.init()
    width, height = 1500, 1000
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Увернись')

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)

    player_size = 50
    player_x = width // 2
    player_y = height - player_size - 20
    player_speed = 4

    enemy_size = 50
    enemy_x = random.randint(0, width - enemy_size)
    enemy_y = 0
    enemy_speed = 9

    score = 0
    font = pygame.font.Font(None, 36)

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < width - player_size:
            player_x += player_speed

        enemy_y += enemy_speed
        if enemy_y > height:
            enemy_y = 0
            enemy_x = random.randint(0, width - enemy_size)
            score += 1

        if player_y < enemy_y + enemy_size and player_y + player_size > enemy_y:
            if player_x < enemy_x + enemy_size and player_x + player_size > enemy_x:
                running = False

        screen.fill(black)
        pygame.draw.rect(screen, white, (player_x, player_y, player_size, player_size))
        pygame.draw.rect(screen, red, (enemy_x, enemy_y, enemy_size, enemy_size))

        score_text = font.render('Счет: ' + str(score), True, white)
        screen.blit(score_text, (10, 10))

        lvl_text = font.render('Уровень: 2', True, white)
        screen.blit(lvl_text, (10, 35))

        pygame.display.flip()
        clock.tick(60)

    game_over_text = font.render('Game Over', True, white)
    screen.blit(game_over_text, (width // 2 - 100, height // 2 - 18))
    pygame.display.flip()

    pygame.time.wait(2000)

if a == 3:
    pygame.init()
    width, height = 1500, 1000
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Увернись')

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)

    player_size = 50
    player_x = width // 2
    player_y = height - player_size - 20
    player_speed = 3

    enemy_size = 50
    enemy_x = random.randint(0, width - enemy_size)
    enemy_y = 0
    enemy_speed = 13

    score = 0
    font = pygame.font.Font(None, 36)

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < width - player_size:
            player_x += player_speed

        enemy_y += enemy_speed
        if enemy_y > height:
            enemy_y = 0
            enemy_x = random.randint(0, width - enemy_size)
            score += 1

        if player_y < enemy_y + enemy_size and player_y + player_size > enemy_y:
            if player_x < enemy_x + enemy_size and player_x + player_size > enemy_x:
                running = False

        screen.fill(black)
        pygame.draw.rect(screen, white, (player_x, player_y, player_size, player_size))
        pygame.draw.rect(screen, red, (enemy_x, enemy_y, enemy_size, enemy_size))

        score_text = font.render('Счет: ' + str(score), True, white)
        screen.blit(score_text, (10, 10))

        lvl_text = font.render('Уровень: 3', True, white)
        screen.blit(lvl_text, (10, 35))

        pygame.display.flip()
        clock.tick(60)

    game_over_text = font.render('Game Over', True, white)
    screen.blit(game_over_text, (width // 2 - 100, height // 2 - 18))
    pygame.display.flip()

    pygame.time.wait(2000)


else: print('Пока такого уровня нет.')
print("Вaш счёт: " + str(score))
with open('schet.txt', 'a') as file:
    file.write(name + ' ' + str(score) + w + str(a) + ', ' )

pygame.quit()
