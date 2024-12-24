import pygame
import Button

# Create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Soccer Championship')

# Load Button Images
start_img = pygame.image.load('start_btn.png').convert_alpha()
title_img = pygame.image.load('Soccer_Title.png').convert_alpha()
level_2_img = pygame.image.load('2_png.png').convert_alpha()  # Level 2 Button Image
logo_img = pygame.image.load('RCB_VS_SRH.png').convert_alpha()  # Game logo image

# Create Button Instances
Start_button = Button.button(320, 300, start_img, 0.5)
Title_button = Button.button(140, 100, title_img, 1.5)

# Game Loop
run = True
while run:
    screen.fill((202, 228, 241))

    if Start_button.draw(screen):
        # Navigate to Level Selection
        SCREEN_HEIGHT = 800
        SCREEN_WIDTH = 500

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Soccer Championship')

        Level_1_img = pygame.image.load('1_png.png').convert_alpha()

        Level_1_button = Button.button(20, 30, Level_1_img, 0.7)
        Level_2_button = Button.button(200, 30, level_2_img, 0.7)  # Added Level 2 button

        level_selection = True
        while level_selection:
            screen.fill((255, 255, 255))

            # Check for Level 1 Button
            if Level_1_button.draw(screen):
                # Start Level 1
                SCREEN_HEIGHT = 800
                SCREEN_WIDTH = 500

                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                pygame.display.set_caption('Soccer Championship - Level 1')

                logo_button = Button.button(20, 30, logo_img, 1.0)
                start_button_level_1 = Button.button(320, 350, start_img, 0.5)

                level_1_run = True
                while level_1_run:
                    screen.fill((0, 0, 0))

                    if start_button_level_1.draw(screen):
                        import Level_1  # Import Level 1 script here
                    if logo_button.draw(screen):
                        print('LOGO Level 1')
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            level_1_run = False
                    pygame.display.update()

            # Check for Level 2 Button
            if Level_2_button.draw(screen):
                # Start Level 2
                SCREEN_HEIGHT = 800
                SCREEN_WIDTH = 500

                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                pygame.display.set_caption('Soccer Championship - Level 2')

                logo_button = Button.button(20, 30, logo_img, 1.0)
                start_button_level_2 = Button.button(320, 350, start_img, 0.5)

                level_2_run = True
                while level_2_run:
                    screen.fill((0, 0, 0))

                    if start_button_level_2.draw(screen):
                        import Level_2  # Import Level 2 script here
                    if logo_button.draw(screen):
                        print('LOGO Level 2')
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            level_2_run = False
                    pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    level_selection = False
            pygame.display.update()

    if Title_button.draw(screen):
        print('Title')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
