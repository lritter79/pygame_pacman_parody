#imporrt in main program for homework
#find out how to make black box
import pygame
import pygame.mixer
import random
pygame.mixer.init()
vamp = pygame.mixer.Sound("Vampire.wav")
bees = pygame.mixer.Sound("Not_the_Bees.wav")
mainScreen = pygame.display.set_mode((1100, 800), 0, 32)
class Sprite:
	def __init__(self, envi, image, position = [0,0]):
		self.envi = envi
		self.position = position
		self.position = [392, 416]
		self.image = image
		self.lives = 4
		self.direction = " "
		self.hitting = " "
		self.D = " "
		self.Debt_to_IRS = 1000000000
		self.alive = 1

	def blit_screen(self):
		self.envi.blit(self.image,self.position)
	
	def get_black_box(self):
		self.black_box = pygame.Rect((self.position[0], self.position[1]),(self.image.get_width(), self.image.get_height()))
		pygame.draw.rect(mainScreen, (0,0,0), self.black_box)
		
	def movement(self, inputt, walls):
		for event in inputt:
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.position[0] -=11
					self.direction = "L"
				elif event.key == pygame.K_RIGHT:
					self.position[0] +=11
					self.direction = "R"
				elif event.key == pygame.K_DOWN:
					self.position[1] +=11
					self.direction = "D"
				elif event.key == pygame.K_UP:
					self.position[1] -=11
					self.direction = "U"
		for EachWall in walls:
			self.checkForWalls(EachWall)
			print self.hitting
				
	def WrapAround(self):
		if self.position[0] < -100:
			self.position[0] = 1100
			vamp.play()
		if self.position[0] > 1100:
			self.position[0] = 0
			vamp.play()
		if self.position[1] > 800:
			self.position[1] = 0
			vamp.play()
		if self.position[1] < -100:
			self.position[1] = 800
			#vamp.play()
	
	def checkForCollisions(self, otherSprite):
		self.get_black_box()
		otherSprite.get_black_box()
		if self.black_box.colliderect(otherSprite.black_box) == True:
			print "collision"
			return True	
			self.hitting = "T"

	def checkForDead(self):
		if self.lives == 0:
			return True
		else:
			return False

	def checkForWalls(self, ThatWall):
		
		self.get_black_box()
		ThatWall.get_black_box()
		if self.black_box.colliderect(ThatWall.black_box) == True:	
			if self.direction == "L":
				self.position[0] = self.position[0] + 11
				self.hitting = "T"
				self.D = random.randint(1, 4)
				return True
	
			if self.direction == "R":
				self.position[0] = self.position[0] - 11
				self.hitting = "T"
				self.D = random.randint(1, 4)
				return True
				
			if self.direction == "U":
				self.position[1] = self.position[1] + 11
				self.hitting = "T"
				self.D = random.randint(1, 4)
				return True
				self.hitting = "T"
			if self.direction == "D":
				self.position[1] = self.position[1] - 11
				self.hitting = "T"
				self.D = random.randint(1, 4)
				return True


if __name__ == '__main__':

	nCage = pygame.image.load('Cage_Sprite.png')
	player = pygame.Rect(300, 100, 40, 40)
	pygame.init()
	pygame.mixer.init()
	pygame.key.set_repeat(30,30)
	bees = pygame.mixer.Sound("Not_the_Bees.wav")



	N = Sprite(mainScreen, nCage, [200, 355])
	N.blit_screen()

	black=(0,0,0)
	end_it = False
	while (end_it == False):
			mainScreen.fill(black)
			myfont=pygame.font.SysFont("Britannic Bold", 40)
			nlabel=myfont.render("Welcome to the Start Screen", 1, (255, 0, 0))
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						end_it = True
					else:
						pass
			mainScreen.blit(nlabel,(200,200))
			pygame.display.flip()
	while True:
		wallz = []
		a_wall = Sprite(mainScreen, nCage, [200, 455])
		wallz.append(a_wall)
		mainScreen.fill((0,0,0))
		#insert blackbox
		#also: fill screen
		N.movement(pygame.event.get(), wallz)
		N.checkForWalls(a_wall)
		N.blit_screen()
		print N.position
		
		pygame.display.update()
