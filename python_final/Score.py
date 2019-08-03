import sys
import pygame
from pygame.locals import *

pygame.init()
size = width, height = 800,500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("testing")
myfont = pygame.font.SysFont("monospace", 16)
WHITE = (255,255,255)

score = 0

while True:
	pygame.display.flip()
	for event in pygame.event.get():
		# I remove the timer just for my testing
		if event.type == pygame.QUIT: sys.exit()

	screen.fill(WHITE)

	disclaimertext = myfont.render("Some disclaimer...", 1, (0,0,0))
	screen.blit(disclaimertext, (5, 480))

	scoretext = myfont.render("Score {0}".format(score), 1, (0,0,0))
	screen.blit(scoretext, (5, 10))
	score += 1