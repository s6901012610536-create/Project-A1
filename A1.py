import pygame
import random

pygame.init()
#====================
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess The Number")
#====================
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (50, 200, 50)
YELLOW = (230, 200, 50)
RED = (220, 60, 60)
GRAY = (200, 200, 200)
#====================
font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 35)
title_font = pygame.font.Font(None, 70)
#====================
answer = []

for i in range(4):
    x = random.randint(0, 9)
    answer.append(x)

print("Answer:", answer)
#====================
guess = []
result = []
message = ""
running = True

#====================GAME

while running:

    #====================ระบบเกม
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        
        #====================
        if event.type == pygame.KEYDOWN:

            if event.unicode.isdigit():

                if len(guess) < 4:
                    guess.append(int(event.unicode))

            if event.key == pygame.K_BACKSPACE:

                if len(guess) > 0:
                    guess.pop()

            if event.key == pygame.K_RETURN:

                if len(guess) == 4:

                    result = []

                    for i in range(4):

                        if guess[i] == answer[i]:
                            result.append("green")

                        elif guess[i] in answer:
                            result.append("yellow")

                        else:
                            result.append("red")

                    if guess == answer:
                        message = "YOU WIN!"

                    else:
                        message = "Try Again!"
                        guess = []
        

        if event.type == pygame.MOUSEBUTTONDOWN:

            if button.collidepoint(event.pos) and len(guess) == 4:

                result = []

                for i in range(4):

                    if guess[i] == answer[i]:
                        result.append("green")

                    elif guess[i] in answer:
                        result.append("yellow")

                    else:
                        result.append("red")    

                if guess == answer:
                    message = "YOU WIN!"

                else:
                    message = "Try Again!"
                    guess = []    
                            

    #====================แสดงผล
    screen.fill(WHITE)

    title = title_font.render("GUESS THE NUMBER", True, BLACK)

    screen.blit(
        title,
        (WIDTH // 2 - title.get_width() // 2, 50)
    )

    #====================
    start_x = 190
    y = 200

    for i in range(4):

        x = start_x + i * 110

        box_color = GRAY

        if i < len(result):

            if result[i] == "green":
                box_color = GREEN

            elif result[i] == "yellow":
                box_color = YELLOW

            elif result[i] == "red":
                box_color = RED

        pygame.draw.rect(
            screen,
            box_color,
            (x, y, 90, 90)
        )

        if i < len(guess):

            number = font.render(
                str(guess[i]),
                True,
                BLACK
            )

            screen.blit(
                number,
                (
                    x + 45 - number.get_width() // 2,
                    y + 45 - number.get_height() // 2
                )
            )

    #====================
    button = pygame.Rect(300, 400, 200, 60)
    pygame.draw.rect(screen, GRAY, button)

    Enter = small_font.render(
        "Enter",
        True,
        BLACK
    )
    
    screen.blit(
        Enter,
        (
            WIDTH // 2 - Enter.get_width() // 2,
            420
        )
    )


    #====================
    text = small_font.render(
        "Enter 4 numbers",
        True,
        BLACK
    )

    screen.blit(
        text,
        (
            WIDTH // 2 - text.get_width() // 2,
            120
        )
    )

    msg = font.render(
        message,
        True,
        BLACK
    )

    screen.blit(
        msg,
        (
            WIDTH // 2 - msg.get_width() // 2,
            320
        )
    )

    pygame.display.update()

pygame.quit()