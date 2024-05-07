import tkinter as tk
import random
import time

class SnakeGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Snake Game")
        self.geometry("400x400")
        self.canvas = tk.Canvas(self, bg="black", width=400, height=400)
        self.canvas.pack()
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.food = self.create_food()
        self.direction = "Right"
        self.bind("<Key>", self.change_direction)
        self.score = 0
        self.delay = 100
        self.game_over = False
        self.game_loop()

    def create_food(self):
        while True:
            x = random.randint(0, 39) * 10
            y = random.randint(0, 39) * 10
            if (x, y) not in self.snake:
                return (x, y)

    def draw(self):
        self.canvas.delete("all")
        self.canvas.create_text(50, 10, text=f"Score: {self.score}", fill="white")
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0]+10, self.food[1]+10, fill="red")
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0]+10, segment[1]+10, fill="white")

    def move(self):
        head = self.snake[0]
        if self.direction == "Right":
            new_head = (head[0] + 10, head[1])
        elif self.direction == "Left":
            new_head = (head[0] - 10, head[1])
        elif self.direction == "Up":
            new_head = (head[0], head[1] - 10)
        elif self.direction == "Down":
            new_head = (head[0], head[1] + 10)

        if new_head in self.snake or new_head[0] < 0 or new_head[0] >= 400 or new_head[1] < 0 or new_head[1] >= 400:
            self.game_over = True

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.food = self.create_food()
        else:
            self.snake.pop()

    def game_loop(self):
        while not self.game_over:
            self.move()
            self.draw()
            self.update()
            time.sleep(self.delay / 1000)
            self.canvas.delete("all")
            self.update_idletasks()

        self.canvas.create_text(200, 200, text=f"Game Over! Your Score: {self.score}", fill="white", font=("Arial", 20))

    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            if (event.keysym == "Up" and self.direction != "Down") or \
                    (event.keysym == "Down" and self.direction != "Up") or \
                    (event.keysym == "Left" and self.direction != "Right") or \
                    (event.keysym == "Right" and self.direction != "Left"):
                self.direction = event.keysym

if __name__ == "__main__":
    SnakeGame().mainloop()
