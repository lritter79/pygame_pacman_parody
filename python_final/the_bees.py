import pygame
import cage_class
import random
theBees = pygame.image.load('The_Bees.png')
theBeesBackwards = pygame.image.load('Reverse_Bees.png')
mainScreen = pygame.display.set_mode((1100, 800), 0, 32)
class Bees(cage_class.Sprite):
	def __init__(self, envi, image, position = [0,0]):
		cage_class.Sprite.__init__(self, envi, image, position = [0,0])
		self.D = 3#random.randint(1, 4)
		self.hitting = " "
	def WrapAround(self):
		cage_class.Sprite.WrapAround(self)

	def get_black_box(self):
		cage_class.Sprite.get_black_box(self)

#	def getDirection(self):
		#directions = [1, 2, 3, 4]		
		#self.D = random.choice(directions)
	def checkForWalls(self, ThatWall):
		cage_class.Sprite.checkForWalls(self, ThatWall)

	def checkForCollisions(self, otherSprite):
		cage_class.Sprite.checkForCollisions(self, otherSprite)
		

	def movement(self, walls):
#		directions = [1, 2, 3, 4]
		#self.getDirection()
	 
		if self.D == 1:
			self.position[0] -=7					
			self.direction = "L"				
			self.image = theBeesBackwards
	#		self.D = random.randint(1, 4)
		if self.D == 2:					
			self.position[0] +=7
			self.direction = "R"				
			self.image = theBees
	#		self.D = random.randint(1, 4)
		if self.D == 3:
			self.position[1] -=7					
			self.direction = "U"
	#		self.D = random.randint(1, 4)
		if self.D == 4:
			self.position[1] +=7
			self.direction = "D"
	#		self.D = random.randint(1, 4)

		for EachWall in walls:
			self.checkForWalls(EachWall)

	def get_bees(self):
		self.listOfBees = []
		b1 = Bees(mainScreen, theBees, [0, 0])
		b1.position = [11, 11]
		self.listOfBees.append(b1)	
		b2 = Bees(mainScreen, theBees, [0, 0])
		b2.position = [11, 690]
		self.listOfBees.append(b2)	
		b3 = Bees(mainScreen, theBees, [0, 0])
		b3.position = [990, 11]
		self.listOfBees.append(b3)	
		b4 = Bees(mainScreen, theBees, [0, 0])
		b4.position = [990, 690]
		self.listOfBees.append(b4)
			






y = (random.randint(0,750))
x = (random.randint(0,1000))
screen = pygame.display.set_mode((1000, 750))
beezus = Bees(screen, theBees, [x, y])
beezus.position[0] = x
beezus.position[1] = y
if __name__ == '__main__':
	pygame.init()


	beezus.blit_screen()
	pygame.display.update()

	while True:
			screen.fill((0,0,0))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit() 
			beezus.movement()
			beezus.checkForWall()
			beezus.blit_screen()
			print beezus.position
			#insert blackbox	#also: fill screen	
			pygame.display.update()
