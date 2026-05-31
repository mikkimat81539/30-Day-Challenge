import pygame, asyncio, random

async def main():
	pygame.init()

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
		pass

	# SNAKE
	snake = Snake(screen_w/2, screen_h/2, 20, 20, "green")

	# MAIN LOOP
	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		screen.fill("black")
	
		# DRAW
		snake.drawSnake(screen)
	
		pygame.display.update()

		await asyncio.sleep(0) 

	pygame.quit()

asyncio.run(main())
