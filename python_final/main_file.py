import pygame
import random
import cage_class
#cage; moving
import time
import the_bees
import ScreenPlayClass
import counter_class
import wall_class
#using these for the score, leanred about this way here: http://stackoverflow.com/questions/19733226/python-pygame-how-to-make-my-score-text-update-itself-forever
import sys
from pygame.locals import *
#bees; random
import pygame.mixer

mainScreen = pygame.display.set_mode((1100, 815), 0, 32)
nCage = pygame.image.load('Cage_Sprite.png')
lilCage = screenPlay = pygame.image.load("LifeCounter.png")
beeCage = pygame.image.load('Bee_Cage.png')
theBees = pygame.image.load('The_Bees.png')
theBeesBackwards = pygame.image.load('Reverse_Bees.png')
not_the_bees = pygame.mixer.Sound("NotTheBees.wav")
nextLevel = pygame.mixer.Sound("122255__jivatma07__level-complete.wav")
channel = not_the_bees.play()
vamp = pygame.mixer.Sound("Vampire.wav")
screenPlay = pygame.image.load("ScreenPlay.png")
EdgeWalls = pygame.image.load('wall3.png')
Upperwalls = pygame.image.load('upperWall.png')
mwv = pygame.image.load('MazeWallVert.png')
mwh = pygame.image.load('MazeWallHorz.png')
y = (random.randint(0,750))
x = (random.randint(0,1000))


if __name__ == '__main__':
	not_the_bees.stop()
	pygame.init()
	myfont = pygame.font.SysFont("monospace", 16)
	WHITE = (255,255,255)

	pygame.mixer.init()
	mainScreen.fill((0,0,0))
	pygame.mixer.music.load("Nic_Cage_Song.wav")
	pygame.key.set_repeat(30,30)
	pygame.display.set_caption("The Wicker Pacman")
	
	#### The Cage sprite
	N = cage_class.Sprite(mainScreen, nCage, [0, 0])
	N.position = [400, 416]
	##########################    Wall Stuff
	
	prime_wall = wall_class.Wall(mainScreen, beeCage, [100, 90])
	prime_wall.get_walls()
	prime_wall.position = [0, 0]

	######## Life Counters
	C = counter_class.counter(mainScreen, lilCage, [0, 0])
	C.AllPossiblePositions()
	C.PlaceLifeCounters()

	##########################    Bee Stuff
	da_bees = the_bees.Bees(mainScreen, theBees, [0, 0])
	da_bees.get_bees()
	da_bees.position

##########################    Screen pLay Stuff
	SC = ScreenPlayClass.screen_play(mainScreen, screenPlay, [0, 0])
	SC.AllPossiblePositions()
	SC.PlaceScreenPlays()


	for event in pygame.event.get():
				if event.type == pygame.QUIT:
						exit() 
	#got the idea for this start screen from here: http://stackoverflow.com/questions/20356307/how-would-i-add-a-start-screen-to-this-pygame-python-code
	#START SCREEN + INSTRUCTIONS
	end_it = False
	while (end_it == False):
			mainScreen.fill((0,0,0))
			introfont=pygame.font.SysFont("comicsansms", 20)
			text1 = introfont.render("In 2000 AD, Hollywood superstar Nicolas Cage fell into millions of dollars in debt to the IRS", 1, (255, 0, 0))
			text2 = introfont.render("Now he has no choice but to star in an ominous film called 'The Wicker Man' ", 1, (255, 255, 0))
			text3 = introfont.render("But can even an Oscar Winning actor survive such a turd????", 1, (0, 0, 255))
			text4 = introfont.render("(Press Space to continue)", 1, (0, 255, 0))
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						end_it = True
					else:
						pass
			mainScreen.blit(text1,(150,200))
			mainScreen.blit(text2,(155,300))
			mainScreen.blit(text3,(160,400))
			mainScreen.blit(text4,(315,500))
			pygame.display.flip()

	end_it = False
	while (end_it == False):
		
		mainScreen.fill((0,0,0))
		end_screen = True
		introfont=pygame.font.SysFont("comicsansms", 20)
		resetFont=pygame.font.SysFont("comicsansms", 40)
		text1 = introfont.render("In order to pay off your debt you must collect screen plays", 1, (255, 0, 0))
		text2 = introfont.render("Move Nicolas Cage with the arrow keys ", 1, (255, 255, 0))
		text3 = introfont.render("But watch out for the bees. If they touch you, you'll become a meme. You only have 3 lives", 1, (0, 0, 255))
		text4 = introfont.render("(Press Space to start)", 1, (0, 255, 0))
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					#pygame.mixer.music.play(-1, 0.0) 	
					end_it = True
				else:
					pass
		mainScreen.blit(text1,(150,200))
		mainScreen.blit(text2,(155,300))
		mainScreen.blit(text3,(160,400))
		mainScreen.blit(text4,(315,500))
		pygame.display.flip()
	
	while N.checkForDead() != True:

		mainScreen.fill((0,0,0))
		
		for EachScreenPlay in SC.listOfScreenPlays:	
			EachScreenPlay.get_black_box()
			EachScreenPlay.blit_screen()
		
		N.movement(pygame.event.get(), prime_wall.listOfWalls)
		N.get_black_box()
		N.WrapAround()
		N.blit_screen()	

		for EachBee in da_bees.listOfBees:
			EachBee.movement(prime_wall.listOfWalls)
			EachBee.get_black_box()	
			EachBee.WrapAround()
			EachBee.blit_screen()
		
		
		
		
		for EachScreenPlay in SC.listOfScreenPlays:
			if EachScreenPlay.black_box.colliderect(N.black_box) == True:
				SC.listOfScreenPlays.remove(EachScreenPlay)
				N.Debt_to_IRS = N.Debt_to_IRS - 100
				SC.number_of_screen_plays_left = SC.number_of_screen_plays_left - 1

		

		for eachWall in prime_wall.listOfWalls:
			eachWall.blit_screen()
	
		for eachCounter in C.listOfCounters:
			eachCounter.blit_screen()


		scoretext = myfont.render("Your debt to the IRS is $ %d" % (N.Debt_to_IRS), 1, (255,255,255))
		mainScreen.blit(scoretext, (20, 797))

		
			

		for EachBee in da_bees.listOfBees: #list of bees is where all the bee objects on screen are
			if N.black_box.colliderect(EachBee.black_box):#N is the player and the bees are the AI
				N.image = beeCage
				timeForBees = time.time() + 6
				pygame.mixer.music.stop()
				vamp.stop()
				not_the_bees.play()
				N.blit_screen()
				ResetText = resetFont.render("Your career is injured", 40, (255,255,0))#the text we want on screen
				mainScreen.blit(ResetText, (400, 350))
				for EachBee in da_bees.listOfBees:
					EachBee.blit_screen()#updating the screen so that there are no longer bees there		
					#changing the player's image
				N.blit_screen
				numberOfBees = 4
				while numberOfBees > 0:#use this while loop to remove the bees from the screen so we can reset them
						da_bees.listOfBees.remove(da_bees.listOfBees[0])
						numberOfBees = numberOfBees - 1
						print "ah"
				pygame.display.update()
				print "not"
				#have to the death sequence based on an attribute and not sounds
				while time.time() <= timeForBees:#or while not_the_bees.play() is playing
					
					print "the"
				print " bees"
				N.position = [402, 416]#resets players 
				N.lives = N.lives - 1
				C.listOfCounters.remove(C.listOfCounters[0])#removes the life counters on the side of the screen
				da_bees.get_bees()#calls all the bee objects in this method
				
				for EachBee in da_bees.listOfBees:
					EachBee.blit_screen()#places the bees
				N.image = nCage#sets players image to original image
				N.blit_screen
		
		if SC.number_of_screen_plays_left == 0:
			nextLevel.play()
			ResetText = resetFont.render("Good job, get ready for next level", 40, (255,255,0))#the text we want on screen
			mainScreen.blit(ResetText, (300, 350))
			for EachBee in da_bees.listOfBees:
				EachBee.blit_screen()#updating the screen so that there are no longer bees there		
			resetTime = time.time() + 2
					#changing the player's image
			numberOfBees = 4
			while numberOfBees > 0:#use this while loop to remove the bees from the screen so we can reset them
					da_bees.listOfBees.remove(da_bees.listOfBees[0])
					numberOfBees = numberOfBees - 1
					print "ah"
			pygame.display.update()
			while time.time() <= resetTime:#or while not_the_bees.play() is playing
					
					print "the"
			SC.AllPossiblePositions()
			SC.PlaceScreenPlays()
			N.position = [400, 416]
			SC.number_of_screen_plays_left = 70
			da_bees.get_bees()
			end_screen = True

		pygame.display.update()


		if N.checkForDead() == True:
			print "Game Over"		
			
			not_the_bees.stop()
			vamp.stop()
			pygame.mixer.music.stop()
			end_screen = False
			pygame.display.flip()
		
		if N.Debt_to_IRS == 0:
			not_the_bees.stop()
			vamp.stop()
			pygame.mixer.music.stop()
			end_screen = False
			pygame.display.flip()	
	
	while end_screen == False:
			mainScreen.fill((0,0,0))
			introfont = pygame.font.SysFont("comicsansms", 30)
			text1 = introfont.render("Game over", 1, (255, 0, 0))
			text2 = introfont.render("Your debt to the IRS was $ %d" % (N.Debt_to_IRS), 1, (0, 255, 0))
			text3 = introfont.render("Press Space to quit", 1, (0, 0, 255))
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						N.lives = 4
						end_screen = True			
					else:
						pass

			mainScreen.blit(text1,(450,200))
			mainScreen.blit(text2,(275, 350))
			mainScreen.blit(text3,(400,500))
			pygame.display.flip()




