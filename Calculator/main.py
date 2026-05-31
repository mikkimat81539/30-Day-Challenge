import pygame, asyncio

pygame.init()

# SCREEN
screen_w = 350
screen_h = 390
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Calculator")

# OBJECT CLASS
class Object:
	def __init__(self, x_pos, y_pos, width, height, color=None):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.width = width
		self.height = height
		self.color = color

# TEXTBOX CLASS
class Textbox(Object):
	def __init__(self, x_pos, y_pos, width, height):
		super().__init__(x_pos, y_pos, width, height, color=None)
		self.text = ""
		self.rect = pygame.Rect((0, 0), (self.width, self.height))
		self.rect.center = (x_pos, y_pos)
		self.operators = ["+", "-", "*", "/", "(", ")", "%", "."]

	def drawTextbox(self, surface):
		pygame.draw.rect(surface, "white", self.rect)

	def createFont(self, surface):
		# Create Font Object
		createFont = pygame.font.SysFont("Arial", 20)
		renderFont = createFont.render(self.text, True, "black")
		surface.blit(renderFont, (self.rect.left + 5, self.rect.top + 15))

	def typeFont(self, event):
		if event.key == pygame.K_BACKSPACE:
			self.text = self.text[:-1]

		elif event.unicode.isdigit() or event.unicode in self.operators:
			if len(self.text) < 20:
				self.text += event.unicode

			elif len(self.text) > 20:
				self.text[:-1]

# BUTTON CLASS
class Buttons(Object):
	def __init__(self, x_pos, y_pos, width, height, text, color):
		super().__init__(x_pos, y_pos, width, height, color)
		self.rect = pygame.Rect((x_pos, y_pos), (self.width, self.height))
		self.text = text

	def drawButtons(self, surface):
		pygame.draw.rect(surface, self.color, self.rect)

	def createFont(self, surface):
		# Create Font Object
		createFont = pygame.font.SysFont("Arial", 30)
		renderFont = createFont.render(self.text, True, "black")
		surface.blit(renderFont, (self.rect.left + 15, self.rect.top + 10))


# TEXTBOX
inputField = Textbox(screen_w/2, 40, 235, 50)

# BUTTON
buttonList= [
	["C", "(", ")", "/"],
	[7, 8, 9, "*"],
	[4, 5, 6, "-"],
	[1, 2, 3, "+"],
	[0, ".", "%", "="]]

numList = []

init_x = 60
init_y = 90

y = init_y
for row in buttonList:
	x = init_x
	for i in row:
		buttons = Buttons(x, y, 50, 50, str(i), "white")	
		numList.append(buttons)
		x += 60
	y += 60

# MAIN LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			inputField.typeFont(event)
			
			key = pygame.key.get_pressed()

			if key[pygame.K_RETURN]:
				try:
					solve = eval(inputField.text)
					inputField.text = str(solve)

				except ZeroDivisionError:
					inputField.text = "undefined"

		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse = pygame.mouse.get_pos()

			for i in numList:
				if i.rect.collidepoint(mouse):
					if i.text == "C":
						inputField.text = i.text[:-1]

					elif i.text == "=":
						try:
							solve = eval(inputField.text)
							inputField.text = str(solve)
						except ZeroDivisionError:
							inputField.text = "undefined"
	
					else:
						inputField.text += i.text
	
	screen.fill("#32a862")

	# DRAW
	inputField.drawTextbox(screen)

	inputField.createFont(screen)

	for i in numList:
		if i == numList[-1]:
			i.color = "orange"

		i.drawButtons(screen)
		i.createFont(screen)

	pygame.display.update()

	await asyncio.sleep(0)

pygame.quit()
