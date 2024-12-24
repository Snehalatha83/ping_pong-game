import pygame, sys, random
from pygame import mixer

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Soccer Championship - Level 2")

# Game Rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 20, 20)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

# Colors
bg_color = pygame.Color("blue")
White = (255, 255, 255)
Orange = (255, 165, 0)
Red = (255, 0, 0)
Yellow = (255, 255, 0)

# Game Variables
ball_speed_x = 10 * random.choice((-1, 1))
ball_speed_y = 10 * random.choice((-1, 1))
player_speed = 0
opponent_speed = 0
game_limit = 5  # Limit for the game

# Text Variables
player_score = 0
opponent_score = 0
player_name = 'CSK'
opponent_name = 'SRH'
game_font = pygame.font.Font("freesansbold.ttf", 32)

# Functions for animations
def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Wall collision
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    # Scoring
    if ball.left <= 0:
        player_score += 1
        ball_restart()
    if ball.right >= screen_width:
        opponent_score += 1
        ball_restart()

    # Paddle collision
    if ball.colliderect(player) and ball_speed_x > 0:
        ball_speed_x *= -1
    if ball.colliderect(opponent) and ball_speed_x < 0:
        ball_speed_x *= -1


def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_animation():
    if opponent.centery < ball.centery:
        opponent.y += 7
    elif opponent.centery > ball.centery:
        opponent.y -= 7
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_y *= random.choice((-1, 1))
    ball_speed_x *= random.choice((-1, 1))


def display_winner(winner_name):
    screen.fill(bg_color)
    winner_text = game_font.render(f"{winner_name} WINS!", True, White)
    screen.blit(winner_text, (screen_width / 2 - 120, screen_height / 2 - 20))
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    # Check if the game limit is reached
    if player_score >= game_limit:
        display_winner(player_name)
    if opponent_score >= game_limit:
        display_winner(opponent_name)

    # Game Logic
    ball_animation()
    player_animation()
    opponent_animation()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, Orange, player)
    pygame.draw.rect(screen, Red, opponent)
    pygame.draw.ellipse(screen, Yellow, ball)
    pygame.draw.aaline(screen, White, (screen_width / 2, 0), (screen_width / 2, screen_height))

    # Display Score
    player_text = game_font.render(f"{player_score}", False, Orange)
    screen.blit(player_text, (410, 315))
    opponent_text = game_font.render(f"{opponent_score}", False, Red)
    screen.blit(opponent_text, (370, 315))

    # Refresh Screen
    pygame.display.flip()
    clock.tick(60)
