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

		def drawSnake(self, surface):
			pygame.draw.rect(surface, self.color, self.rect)

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
	snake = [Snake(screen_w/2, screen_h/2, 20, 20, "green"),
	Snake(screen_w/2 + 25, screen_h/2, 20, 20, "green"), 
	Snake(screen_w/2 + 50, screen_h/2, 20, 20, "green")]	

	# FOOD
	food = Food(random.randint(10, screen_w-10), random.randint(10, screen_h-10), 10, 10, "red")

	# DIRECTION
	direction = 'LEFT'	
	change_to = direction

	# MAIN LOOP
	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					change_to = 'LEFT'

				if event.key == pygame.K_RIGHT:
					change_to = 'RIGHT'

				if event.key == pygame.K_UP:
					change_to = 'UP'

				if event.key == pygame.K_DOWN:
					change_to = 'DOWN'	

		screen.fill("black")

		# MOVEMENT
		if change_to == 'UP' and direction != 'DOWN':
			direction = 'UP'

		if change_to == 'DOWN' and direction != 'UP':
			direction = 'DOWN'

		if change_to == 'LEFT' and direction != 'RIGHT':
			direction = 'LEFT'

		if change_to == 'RIGHT' and direction != 'LEFT':
			direction = 'RIGHT'


		# MOVE SNAKE
		for i in snake:
			if direction == 'UP':
				i.rect.y -= 10

			if direction == 'DOWN':
				i.rect.y += 10

			if direction == 'LEFT':
				i.rect.x -= 10

			if direction == 'RIGHT':
				i.rect.x += 10

		# DRAW
		food.drawFood(screen)

		for i in snake:
			i.drawSnake(screen)
	
		pygame.display.update()

		clock.tick(20)

		await asyncio.sleep(0) 

	pygame.quit()

asyncio.run(main())
