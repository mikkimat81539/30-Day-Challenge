import pygame, asyncio, random

async def main():
	pygame.init()

	# CLOCK
	clock = pygame.time.Clock()

	# SCREEN
	screen_w = 500
	screen_h = 400
	screen = pygame.display.set_mode((screen_w, screen_h))
	pygame.display.set_caption("Snake Game")


	# OBJECT CLASS
	class Object:
		def __init__(self, x_pos, y_pos, color):
			self.x_pos = x_pos
			self.y_pos = y_pos
			self.color = color

	# PLAYER CLASS
	class Snake(Object):
		def __init__(self, x_pos, y_pos, width, height, color):
			super().__init__(x_pos, y_pos, color)
			self.width = width
			self.height = height
			self.color = color
			self.rect = pygame.Rect((x_pos, y_pos), (self.width, self.height))
			self.rect.center = (x_pos, y_pos)
			self.speed = 5

		def drawSnake(self, surface):
			pygame.draw.rect(surface, self.color, self.rect)

		def moveSnake(self):
			key = pygame.key.get_pressed()
	
			if key[pygame.K_LEFT]:
				self.rect.x -= self.speed

			if key[pygame.K_RIGHT]:
				self.rect.x += self.speed
			
			if key[pygame.K_UP]:
				self.rect.y -= self.speed

			if key[pygame.K_DOWN]:
				self.rect.y += self.speed

	# FOOD CLASS
	class Food(Object):
		def __init__(self, x_pos, y_pos, width, height, color):
			super().__init__(x_pos, y_pos, color)
			self.width = width
			self.height = height
			self.color = color
			self.rect = pygame.Rect((x_pos, y_pos), (self.width, self.height))
			self.rect.center = (x_pos, y_pos)

		def drawFood(self, surface):
			pygame.draw.rect(surface, self.color, self.rect)


	# SNAKE
	snakeHead = Snake(screen_w/2, screen_h/2, 20, 20, "green")
	
	snakeBody1 = Snake(snakeHead.x_pos + 25, screen_h/2, 20, 20, "green")

	snakeBody2 = Snake(snakeBody1.x_pos + 25, screen_h/2, 20, 20, "green")

	snake = [snakeHead, snakeBody1, snakeBody2]	

	# FOOD
	food = Food(random.randint(10, screen_w-10), random.randint(10, screen_h-10), 10, 10, "red")


	for i in snake:
		if snakeHead.rect.colliderect(food.rect):
			snakebody = Snake(i[-1].x_pos + 25, screen_h/2, 20, 20, "green")
			snake.append(snakebody)

	# MAIN LOOP
	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		screen.fill("black")

		# Draw and Move
		snakeHead.moveSnake()

		for i in snake:
			i.drawSnake(screen)

		food.drawFood(screen)
	
		pygame.display.update()

		clock.tick(60)

		await asyncio.sleep(0) 

	pygame.quit()

asyncio.run(main())
