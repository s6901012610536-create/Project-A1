# ==================== window ====================

WIDTH = 800
HEIGHT = 600

WHITE = color(255, 255, 255)
BLACK = color(0, 0, 0)
GREEN = color(50, 200, 50)
YELLOW = color(230, 200, 50)
RED = color(220, 60, 60)
GRAY = color(200, 200, 200)

answer = []
guess = []
result = []
message = ""

# ==================== Setup ====================

def setup():
    size(WIDTH, HEIGHT)
    background(WHITE)

    textFont(createFont("Arial", 35))

    for i in range(4):
        x = int(random(10))
        answer.append(x)

    print("Answer:", answer)


# ==================== check ====================

def check_answer():
    global guess, result, message

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


# ==================== key press ====================

def keyPressed():
    global guess

    if key >= '0' and key <= '9':
        if len(guess) < 4:
            guess.append(int(key))

    elif keyCode == BACKSPACE:
        if len(guess) > 0:
            guess.pop()

    elif keyCode == ENTER or keyCode == RETURN:
        check_answer()


# ==================== mouse ====================

def mousePressed():
    if mouseX >= 300 and mouseX <= 500:
        if mouseY >= 400 and mouseY <= 460:
            check_answer()


# ==================== game ====================

def draw():
    background(WHITE)

    fill(BLACK)
    textAlign(CENTER, CENTER)
    textSize(55)
    text("GUESS THE NUMBER", WIDTH / 2, 75)

    textSize(30)
    text("Enter 4 numbers", WIDTH / 2, 145)

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

        fill(box_color)
        rect(x, y, 90, 90)

        if i < len(guess):
            fill(BLACK)
            textSize(50)
            text(str(guess[i]), x + 45, y + 45)

    fill(GRAY)
    rect(300, 400, 200, 60)

    fill(BLACK)
    textSize(35)
    text("Enter", WIDTH / 2, 430)

    textSize(40)
    text(message, WIDTH / 2, 340)
