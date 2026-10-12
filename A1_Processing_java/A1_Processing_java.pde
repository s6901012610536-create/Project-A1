// ==================== window ====================
int WIDTH = 800;
int HEIGHT = 600;

color WHITE = color(255, 255, 255);
color BLACK = color(0, 0, 0);
color GREEN = color(50, 200, 50);
color YELLOW = color(230, 200, 50);
color RED = color(220, 60, 60);
color GRAY = color(200, 200, 200);

int[] answer = new int[4];
int[] guess = new int[4];
String[] result = new String[4];

int guessCount = 0;
String message = "";

// ==================== Setup ====================

void setup() {
  size(800, 600);
  surface.setTitle("Guess The Number");

  textAlign(CENTER, CENTER);

  for (int i = 0; i < 4; i++) {
    answer[i] = int(random(10));
  }

  println("Answer: " + answer[0] + answer[1]
    + answer[2] + answer[3]);
}

// ==================== check ====================

void checkAnswer() {
  if (guessCount == 4) {
    for (int i = 0; i < 4; i++) {
      if (guess[i] == answer[i]) {
        result[i] = "green";
      } else {
        boolean found = false;

        for (int j = 0; j < 4; j++) {
          if (guess[i] == answer[j]) {
            found = true;
          }
        }

        if (found) {
          result[i] = "yellow";
        } else {
          result[i] = "red";
        }
      }
    }

    boolean win = true;

    for (int i = 0; i < 4; i++) {
      if (guess[i] != answer[i]) {
        win = false;
      }
    }

    if (win) {
      message = "YOU WIN!";
    } else {
      message = "Try Again!";
      guessCount = 0;
    }
  }
}

// ==================== key press ====================

void keyPressed() {
  if (key >= '0' && key <= '9') {
    if (guessCount < 4) {
      guess[guessCount] = key - '0';
      guessCount++;
    }
  }

  if (key == BACKSPACE) {
    if (guessCount > 0) {
      guessCount--;
    }
  }

  if (key == ENTER || key == RETURN) {
    checkAnswer();
  }
}

// ==================== mouse ====================

void mousePressed() {
  if (mouseX >= 300 && mouseX <= 500
    && mouseY >= 400 && mouseY <= 460) {
    checkAnswer();
  }
}

// ==================== game ====================

void draw() {
  background(WHITE);

  fill(BLACK);
  textSize(55);
  text("GUESS THE NUMBER", WIDTH / 2, 75);

  textSize(30);
  text("Enter 4 numbers", WIDTH / 2, 145);

  int startX = 190;
  int y = 200;

  for (int i = 0; i < 4; i++) {
    int x = startX + i * 110;

    color boxColor = GRAY;

    if (result[i] != null) {
      if (result[i].equals("green")) {
        boxColor = GREEN;
      } else if (result[i].equals("yellow")) {
        boxColor = YELLOW;
      } else if (result[i].equals("red")) {
        boxColor = RED;
      }
    }

    fill(boxColor);
    rect(x, y, 90, 90);

    if (i < guessCount) {
      fill(BLACK);
      textSize(50);
      text(guess[i], x + 45, y + 45);
    }
  }

  fill(GRAY);
  rect(300, 400, 200, 60);

  fill(BLACK);
  textSize(35);
  text("Enter", WIDTH / 2, 430);

  textSize(40);
  text(message, WIDTH / 2, 340);
}
