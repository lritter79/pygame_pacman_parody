import pygame
screenPlay = pygame.image.load("New Piskel.png")
import cage_class
mainScreen = pygame.display.set_mode((1100, 800), 0, 32)
Screen_play_positions = []

class screen_play(cage_class.Sprite):
	def __init__(self, envi, image, position = []):
		cage_class.Sprite.__init__(self, envi, image, position = [0,0])
	def blit_screen(self):
		cage_class.Sprite.blit_screen(self)		
	def get_black_box(self):
		cage_class.Sprite.get_black_box(self)
	def AllPossiblePositions(self):
		first_position = [10, 10]
		HorizontalPositions = 0
		VerticalPositions = 0
		amountToAdd = 0
		while HorizontalPositions < 11:
			while VerticalPositions < 11:
				new_position = [first_position[0], (first_position[1] + amountToAdd)]
				Screen_play_positions.append(new_position)
				amountToAdd = amountToAdd + 11
				VerticalPositions = VerticalPositions + 1
			first_position[0] = first_position[0] + 11
			amountToAdd = 11
			VerticalPositions = 0
			HorizontalPositions = HorizontalPositions + 1
			
if __name__ == '__main__':
	

	SC = screen_play(mainScreen, screenPlay, [0, 0])
	SC.AllPossiblePositions()
	pygame.init()
	pygame.mixer.init()
 	print Screen_play_positions

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()		
		
		mainScreen.fill((0,0,0))
		SC.blit_screen()

		pygame.display.update()

