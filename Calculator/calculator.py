import pygame

pygame.init()

# SCREEN
screen_w = 370
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
		self.operators = ["+", "-", "*", "/"]

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
			if len(self.text) < 17:
				self.text += event.unicode

# BUTTONS

# TEXTBOX
inputField = Textbox(screen_w/2, 40, 200, 50)

# MAIN LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			inputField.typeFont(event)

	screen.fill("#32a862")

	# DRAW
	inputField.drawTextbox(screen)

	inputField.createFont(screen)

	pygame.display.update()

pygame.quit()
