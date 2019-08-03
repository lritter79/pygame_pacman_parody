import pygame
lilCage = screenPlay = pygame.image.load("LifeCounter.png")
import cage_class
mainScreen = pygame.display.set_mode((1100, 815), 0, 32)

class counter(cage_class.Sprite):
	def __init__(self, envi, image, position = []):
		cage_class.Sprite.__init__(self, envi, image, position = [0,0])
		self.Screen_play_positions = []
		self.number_of_screen_plays_left = 70
		self.position = [1000, 801]

	def blit_screen(self):
		cage_class.Sprite.blit_screen(self)		
	
	def get_black_box(self):
		cage_class.Sprite.get_black_box(self)

	def AllPossiblePositions(self):
		self.counterPositions = []
		first_position = [1000, 800]
		HorizontalPositions = 0
		VerticalPositions = 0
		amountToAdd = 0
		while HorizontalPositions < 1:
			while VerticalPositions < 4:
				new_position = [(first_position[0]+amountToAdd), first_position[1]]
				self.counterPositions.append(new_position)
				amountToAdd = amountToAdd + 35
				VerticalPositions = VerticalPositions + 1
			VerticalPositions = 0
			first_position[0] = first_position[0] + 1
			amountToAdd = 0
			HorizontalPositions = HorizontalPositions + 1
	
	def PlaceLifeCounters(self):
		self.listOfCounters = []
		numberOfCounters = 4
		numberOfCountersCreated = 0 
		while (numberOfCountersCreated < numberOfCounters):
			currentPosition = self.counterPositions[0]
			x = counter(mainScreen, lilCage, [0, 0])
			x.position = currentPosition
			self.listOfCounters.append(x)
			numberOfCountersCreated = numberOfCountersCreated + 1
			self.counterPositions.remove(self.counterPositions[0])

if __name__ == '__main__':
	
	#print len(ScreenPlays)
	C = counter(mainScreen, lilCage, [0, 0])
	C.AllPossiblePositions()
	
### Find way to make this part into a method
#	listOfScreenPlays = []
#	numberOfScreenPlaysINeed = 121
#	numberOfScreenPlaysCreated = 0 
#	while (numberOfScreenPlaysCreated < numberOfScreenPlaysINeed):
#		currentPosition = SC.Screen_play_positions[0]
#		x = screen_play(mainScreen, screenPlay, [0, 0])
#		x.position = currentPosition
#		listOfScreenPlays.append(x)
#		numberOfScreenPlaysCreated = numberOfScreenPlaysCreated + 1
#		SC.Screen_play_positions.remove(SC.Screen_play_positions[0])
	pygame.init()
	pygame.mixer.init()
	C.PlaceLifeCounters()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()		
		
		mainScreen.fill((0,0,0))
		C.blit_screen()
		for eachCounter in C.listOfCounters:
			eachCounter.blit_screen()
		pygame.display.update()
