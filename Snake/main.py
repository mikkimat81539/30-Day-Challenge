import pygame, asyncio, random, sys

def lose(screen):
	createFont = pygame.font.SysFont("Arial", 20)	

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		screen.fill("black")
	
		renderFont = createFont.render("Game Over", True, "white")
	
		screen.blit(renderFont, (210, 200))
		pygame.display.flip()

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
	class Snake:
		def __init__(self):
			self.x_pos = screen_w/2
			self.y_pos = screen_h/2
			self.xdir = 1
			self.ydir = 0

			self.head = pygame.Rect(self.x_pos, self.y_pos, 20, 20)
			self.body = [pygame.Rect(self.x_pos-25, self.y_pos, 20, 20)]
			self.dead = False 

		def update(self):
			self.body.append(self.head)
			for i in range(len(self.body)-1):
				self.body[i].x = self.body[i+1].x
				self.body[i].y = self.body[i+1].y
	
			self.head.x += self.xdir * 25
			self.head.y += self.ydir * 25
			self.body.remove(self.head)


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
	snake = Snake()

	# FOOD
	food = Food(random.randint(20, screen_w-20), random.randint(20, screen_h-20), 10, 10, "red")

	points = 0

	def eating(food, screen, points):
		createFont = pygame.font.SysFont("Arial", 20)	
		renderFont = createFont.render(f"Points: {points}", True, "white")
		screen.blit(renderFont, (10, 10))


		if snake.head.colliderect(food.rect):
			points += 1
			snake.body.append(pygame.Rect(snake.body[-1].x, snake.body[-1].y, 20, 20))
			
			food.rect.x = random.randint(20, screen_w-20)
			food.rect.y = random.randint(20, screen_h-20)	

		return points

	def death(screen):
		if snake.head.x <= 1 or snake.head.x >= screen_w - 20:
			lose(screen)

		elif snake.head.y <= 1 or snake.head.y >= screen_h - 20:
			lose(screen)

		if snake.head.collidelistall(snake.body):
			lose(screen)

	# MAIN LOOP
	running = True

	while running:
		death(screen)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT and snake.xdir != 1:
					snake.xdir = -1
					snake.ydir = 0

				elif event.key == pygame.K_RIGHT and snake.xdir != -1:
					snake.xdir = 1
					snake.ydir = 0

				elif event.key == pygame.K_UP and snake.ydir != 1:
					snake.xdir = 0
					snake.ydir = -1

				elif event.key == pygame.K_DOWN and snake.ydir != -1:
					snake.xdir = 0
					snake.ydir = 1

		screen.fill("black")

		snake.update()
		
		points = eating(food, screen, points)

		# DRAW
		pygame.draw.rect(screen, "green", snake.head)

		for i in snake.body:
			pygame.draw.rect(screen, "green", i)

		food.drawFood(screen)

		pygame.display.update()

		clock.tick(5)

		await asyncio.sleep(0) 

	pygame.quit()

asyncio.run(main())
