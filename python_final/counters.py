import pygame
lilCage = screenPlay = pygame.image.load("LifeCounter.png")
import cage_class
mainScreen = pygame.display.set_mode((1100, 800), 0, 32)

class counter(cage_class.Sprite):
	def __init__(self, envi, image, position = []):
		cage_class.Sprite.__init__(self, envi, image, position = [0,0])
		self.Screen_play_positions = []
		self.number_of_screen_plays_left = 70
	
	def blit_screen(self):
		cage_class.Sprite.blit_screen(self)		
	
	def get_black_box(self):
		cage_class.Sprite.get_black_box(self)

	def AllPossiblePositions(self):
		first_position = [35, 30]
		HorizontalPositions = 0
		VerticalPositions = 0
		amountToAdd = 0
		while HorizontalPositions < 3:
			while VerticalPositions < 1:
				new_position = [first_position[0], (first_position[1] + amountToAdd)]
				self.Screen_play_positions.append(new_position)
				amountToAdd = amountToAdd + 20
				VerticalPositions = VerticalPositions + 1
			VerticalPositions = 0
			first_position[0] = first_position[0] + 1
			amountToAdd = 0
			HorizontalPositions = HorizontalPositions + 1
	def PlaceLifeCounters(self):
		self.listOfCounters = []
		numberOfCounters = 3
		numberOfCountersCreated = 0 
		while (numberOfScreenPlaysCreated < numberOfScreenPlaysINeed):
			currentPosition = self.Screen_play_positions[0]
			x = screen_play(mainScreen, screenPlay, [0, 0])
			x.position = currentPosition
			self.listOfScreenPlays.append(x)
			numberOfScreenPlaysCreated = numberOfScreenPlaysCreated + 1
			self.Screen_play_positions.remove(self.Screen_play_positions[0])

if __name__ == '__main__':
	
	#print len(ScreenPlays)
	SC = screen_play(mainScreen, screenPlay, [0, 0])
	SC.AllPossiblePositions()
	print SC.Screen_play_positions
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
	SC.PlaceScreenPlays()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()		
		
		mainScreen.fill((0,0,0))
		SC.blit_screen()
		for eachScreenPlay in SC.listOfScreenPlays:
			eachScreenPlay.blit_screen()
		pygame.display.update()
