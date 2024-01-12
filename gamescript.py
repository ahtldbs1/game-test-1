import pygame
import sys
import random

pygame.init()


screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("피하기 게임")


white = (1, 1, 89)
black = (255, 192, 203)


player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

ball_radius = 20
ball_x = random.randint(0, screen_width - ball_radius * 2)
ball_y = -ball_radius
ball_speed = 10

player_image = pygame.image.load("pororo.png")
ball_image = pygame.image.load("poop.png")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    ball_y += ball_speed
    if ball_y > screen_height:
        ball_y = -ball_radius
        ball_x = random.randint(0, screen_width - ball_radius * 2)

    if (
        player_x < ball_x < player_x + player_width
        and player_y < ball_y < player_y + player_height
    ):
        print("게임 오버!")
        pygame.quit()
        sys.exit()

    screen.fill((255, 255, 255))  # 흰색으로 채우기

    # 이미지 그리기
    screen.blit(player_image, (player_x, player_y))
    screen.blit(ball_image, (ball_x, ball_y))

    pygame.display.flip()
    clock.tick(60)
