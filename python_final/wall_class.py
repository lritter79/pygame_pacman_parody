import pygame
import cage_class
#see http://stackoverflow.com/questions/24301702/walls-in-pygame 
mainScreen = pygame.display.set_mode((1100, 800), 0, 32)
Walls = pygame.image.load('MazeWallVert.png')
mwv = pygame.image.load('MazeWallVert.png')
mwh = pygame.image.load('MazeWallHorz.png')
EdgeWalls = pygame.image.load('wall3.png')
Upperwalls = pygame.image.load('upperWall.png')
class Wall(cage_class.Sprite):	
	def __init__(self, envi, image, position = []):
		cage_class.Sprite.__init__(self, envi, image, position = [0,0])
		self.listOfWalls = []
	def blit_screen(self):
		cage_class.Sprite.blit_screen(self)		
	def get_black_box(self):
		cage_class.Sprite.get_black_box(self)
	def get_walls(self):
		
		lb1 = Wall(mainScreen, EdgeWalls, [0, 0])
		self.listOfWalls.append(lb1)
		lb2 = Wall(mainScreen, EdgeWalls, [0, 0])
		self.listOfWalls.append(lb2)
		lb1.position = [0, 0]
		lb2.position = [0, 465]
		rb1 = Wall(mainScreen, EdgeWalls, [0, 0])
		self.listOfWalls.append(rb1)
		rb2 = Wall(mainScreen, EdgeWalls, [0, 0])
		self.listOfWalls.append(rb2)
		rb1.position = [1090, 0]
		rb2.position = [1090, 465]	
		uw1 = Wall(mainScreen, Upperwalls, [0, 0])
		self.listOfWalls.append(uw1)
		uw2 = Wall(mainScreen, Upperwalls, [0, 0])
		self.listOfWalls.append(uw2)	
		uw1.position = [0, -4]
		uw2.position = [0, 790]
		sw1 = Wall(mainScreen, Upperwalls, [0, 0])
		self.listOfWalls.append(sw1)
		sw2 = Wall(mainScreen, Upperwalls, [0, 0])
		self.listOfWalls.append(sw2)	
		sw1.position = [-990, 340]
		sw2.position = [-990, 465]
		sw3 = Wall(mainScreen, Upperwalls, [0, 0])
		self.listOfWalls.append(sw3)
		sw4 = Wall(mainScreen, Upperwalls, [0, 0])
		self.listOfWalls.append(sw4)	
		sw3.position = [990, 340]
		sw4.position = [990, 465]
		
		###the N
		nicN1 = Wall(mainScreen, mwv, [0, 0])
		self.listOfWalls.append(nicN1)
		nicN1.position = [210, 120]
		nicN2 = Wall(mainScreen, mwh, [0, 0])
		self.listOfWalls.append(nicN2)
		nicN2.position = [210, 110]
		nicN3 = Wall(mainScreen, mwv, [0, 0])
		self.listOfWalls.append(nicN3)
		nicN3.position = [320, 120]
		nicI1 = Wall(mainScreen, mwv, [0, 0])
		self.listOfWalls.append(nicI1)
		nicI1.position = [445, 120]
		nicI2 = Wall(mainScreen, mwv, [0, 0])
		self.listOfWalls.append(nicI2)
		nicI2.position = [445, 10]
		####the C
		nicC1 = Wall(mainScreen, mwv, [0, 0])
		self.listOfWalls.append(nicC1)
		nicC1.position = [560, 115]
		nicC2 = Wall(mainScreen, mwh, [0, 0])
		self.listOfWalls.append(nicC2)
		nicC2.position = [560, 113]
		nicC3 = Wall(mainScreen, mwh, [0, 0])
		self.listOfWalls.append(nicC3)
		nicC3.position = [560, 230]
		nicC4 = Wall(mainScreen, mwv, [0, 0])
		self.listOfWalls.append(nicC4)
		nicC4.position = [665, 5]

		####second C
		nicC4 = Wall(mainScreen, mwv, [0, 0])
		self.listOfWalls.append(nicC4)
		nicC4.position = [225, 565]
		nicC5 = Wall(mainScreen, mwh, [0, 0])
		self.listOfWalls.append(nicC5)
		nicC5.position = [225, 465]
		nicC6 = Wall(mainScreen, mwh, [0, 0])
		self.listOfWalls.append(nicC6)
		nicC6.position = [225, 670]
		nicC7 = Wall(mainScreen, mwv, [0, 0])
		self.listOfWalls.append(nicC7)
		nicC7.position = [225, 465]

		#####the A
		nicA1 = Wall(mainScreen, mwv, [0, 0])
		self.listOfWalls.append(nicA1)
		nicA1.position = [350, 363]
		nicA2 = Wall(mainScreen, mwv, [0, 0])
		self.listOfWalls.append(nicA2)
		nicA2.position = [350, 430]
		nicA3 = Wall(mainScreen, mwh, [0, 0])
		self.listOfWalls.append(nicA3)
		nicA3.position = [350, 360]
		nicA4 = Wall(mainScreen, mwh, [0, 0])
		self.listOfWalls.append(nicA4)
		nicA4.position = [430, 360]
		nicA5 = Wall(mainScreen, mwv, [0, 0])
		self.listOfWalls.append(nicA5)
		nicA5.position = [534, 363]
		nicA5 = Wall(mainScreen, mwv, [0, 0])
		self.listOfWalls.append(nicA5)
		nicA5.position = [534, 460]
		###the G
		nicG1 = Wall(mainScreen, mwv, [0, 0])
		self.listOfWalls.append(nicG1)
		nicG1.position = [534, 500]
		nicG2 = Wall(mainScreen, mwh, [0, 0])
		self.listOfWalls.append(nicG2)
		nicG2.position = [540, 360]
		nicG3 = Wall(mainScreen, mwh, [0, 0])
		self.listOfWalls.append(nicG3)
		nicG3.position = [630, 360]
		nicG4 = Wall(mainScreen, mwh, [0, 0])
		self.listOfWalls.append(nicG4)
		nicG4.position = [540, 604]
		nicG5 = Wall(mainScreen, mwh, [0, 0])
		self.listOfWalls.append(nicG5)
		nicG5.position = [630, 604]
		nicG6 = Wall(mainScreen, mwv, [0, 0])
		self.listOfWalls.append(nicG6)
		nicG6.position = [734, 490]
		nicG7 = Wall(mainScreen, mwh, [0, 0])
		self.listOfWalls.append(nicG7)
		nicG7.position = [630, 480]
		#####the E

		nicE1 = Wall(mainScreen, mwv, [0, 0])
		self.listOfWalls.append(nicE1)
		nicE1.position = [765, 580]
		nicE2 = Wall(mainScreen, mwh, [0, 0])
		self.listOfWalls.append(nicE2)
		nicE2.position = [770, 675]
		nicE4 = Wall(mainScreen, mwh, [0, 0])
		self.listOfWalls.append(nicE4)
		nicE4.position = [765, 560]
		nicE5 = Wall(mainScreen, mwv, [0, 0])
		self.listOfWalls.append(nicE5)
		nicE5.position = [765, 680]
		nicE6 = Wall(mainScreen, mwv, [0, 0])
		self.listOfWalls.append(nicE6)
		nicE6.position = [765, 570]
		nicE7 = Wall(mainScreen, mwh, [0, 0])
		self.listOfWalls.append(nicE7)
		nicE7.position = [765, 790]
		self.blit_screen()

if __name__ == '__main__':
	
	the_wall = Wall(mainScreen, mwv, [0, 0])
	the_wall.get_walls()
	the_wall.position[1] = 330
	the_wall.position[0] = 500
	
	pygame.init()
	pygame.mixer.init()
 

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()		
		
		mainScreen.fill((0,0,0))
		the_wall.blit_screen()
		for eachWall in the_wall.listOfWalls:
			eachWall.blit_screen()
		pygame.display.update()


