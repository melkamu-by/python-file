import pygame
import random
import os
 # --- Configuration & Constants ---
WIDTH, HEIGHT = 600, 400
SNAKE_SIZE = 10
SPEED = 15

# Colors
COLORS = {
    "background": (20, 20, 20),
    "snake": (0, 255, 127),
    "food": (255, 65, 54),
    "text": (255, 255, 255),
    "score": (255, 215, 0)
}

class Snake:
    def __init__(self):
        self.length = 1
        self.body = [[WIDTH / 2, HEIGHT / 2]]
        self.direction = [0, 0] # [x_change, y_change]

    def update(self):
        curr_head = self.body[-1]
        new_head = [curr_head[0] + self.direction[0], curr_head[1] + self.direction[1]]
        self.body.append(new_head)
        if len(self.body) > self.length:
            del self.body[0]

    def draw(self, surface):
        for block in self.body:
            pygame.draw.rect(surface, COLORS["snake"], [block[0], block[1], SNAKE_SIZE, SNAKE_SIZE])

    def has_collided(self):
        head = self.body[-1]
        # Wall collision
        if head[0] >= WIDTH or head[0] < 0 or head[1] >= HEIGHT or head[1] < 0:
            return True
        # Self collision
        if head in self.body[:-1]:
            return True
        return False

class Food:
    def __init__(self):
        self.pos = self.randomize_pos()

    def randomize_pos(self):
        x = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 10.0) * 10.0
        y = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 10.0) * 10.0
        return [x, y]

    def draw(self, surface):
        pygame.draw.rect(surface, COLORS["food"], [self.pos[0], self.pos[1], SNAKE_SIZE, SNAKE_SIZE])

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Pro: OOP Edition")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("bahnschrift", 25)
        self.high_score = self.load_high_score()
        self.reset_game()

    def load_high_score(self):
        if not os.path.exists("highscore.txt"):
            return 0
        with open("highscore.txt", "r") as f:
            return int(f.read() or 0)

    def save_high_score(self):
        with open("highscore.txt", "w") as f:
            f.write(str(self.high_score))

    def reset_game(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    def display_ui(self):
        score_text = self.font.render(f"Score: {self.score}  Best: {self.high_score}", True, COLORS["score"])
        self.screen.blit(score_text, [10, 10])

    def start_menu(self):
        waiting = True
        while waiting:
            self.screen.fill(COLORS["background"])
            msg = self.font.render("SNAKE PRO - Press SPACE to Start", True, COLORS["text"])
            self.screen.blit(msg, [WIDTH/6, HEIGHT/2.5])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: waiting = False

    def run(self):
        self.start_menu()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.snake.direction[0] == 0:
                        self.snake.direction = [-SNAKE_SIZE, 0]
                    elif event.key == pygame.K_RIGHT and self.snake.direction[0] == 0:
                        self.snake.direction = [SNAKE_SIZE, 0]
                    elif event.key == pygame.K_UP and self.snake.direction[1] == 0:
                        self.snake.direction = [0, -SNAKE_SIZE]
                    elif event.key == pygame.K_DOWN and self.snake.direction[1] == 0:
                        self.snake.direction = [0, SNAKE_SIZE]

            self.snake.update()

            if self.snake.has_collided():
                if self.score > self.high_score:
                    self.high_score = self.score
                    self.save_high_score()
                self.reset_game() # Restarts immediately for this example

            if self.snake.body[-1] == self.food.pos:
                self.snake.length += 1
                self.score += 1
                self.food.pos = self.food.randomize_pos()

            self.screen.fill(COLORS["background"])
            self.food.draw(self.screen)
            self.snake.draw(self.screen)
            self.display_ui()
            pygame.display.update()
            self.clock.tick(SPEED)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()