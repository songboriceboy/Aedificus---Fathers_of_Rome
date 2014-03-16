import pygame, random
from pygame.locals import *

pygame.init()

FPS = 60
FPSCLOCK = pygame.time.Clock()
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
HALFWINDOWWIDTH = int(WINDOWWIDTH / 2)
HALFWINDOWHEIGHT = int(WINDOWHEIGHT / 2)
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), DOUBLEBUF)


CELLSIZE = 20
HALFCELL = 10
MAPXCELLS = 200
MAPYCELLS = 200
MAPWIDTH = CELLSIZE * MAPXCELLS
MAPHEIGHT = CELLSIZE * MAPYCELLS
SCROLLACCEL = 1 # map scroll
SCROLLDRAG = 2 # bigger is less drag
MAPEDGEBOUNCE = 10
MAXSCROLLSPEED = 4


TREEFREQUENCY = random.randint(50, 100)   # 1/xth of tiles are trees
TREEMAXHEALTH = 400
WOODPERTREE = 50
TREECHOPSPEED = 1
MAXTREESDESIGNATED = 20 # to help performance
STARTRESOURCES    = {'wood': 50, 'iron': 10, 'cheese': 250}
STARTMAXRESOURCES = {'wood': 100, 'iron': 40, 'cheese': 250}
HUMANMOVESPEED = 2
CONSTRUCTIONSPEED = 3 # progress towards completion added per tick
STARTINGHAPPINESS = 20
STARTINGHUNGER = 1500
MAXHUNGER = 1500
HUNGERWARNING = 800
HUNGERURGENT = 300
BUBBLEMARGIN = 3


# Colours     R    G    B  ALPHA
WHITE     = (255, 255, 255, 255)
BLACK     = (  0,   0,   0, 255)
RED       = (255,   0,   0, 255)
DARKRED   = (220,   0,   0, 255)
BLUE      = (  0,   0, 255, 255)
SKYBLUE   = (135, 206, 250, 255)
YELLOW    = (255, 250,  17, 255)
GREEN     = (  0, 255,   0, 255)
ORANGE    = (255, 165,   0, 255)
DARKGREEN = (  0, 155,   0, 255)
DARKGREY  = ( 60,  60,  60, 255)
LIGHTGREY = (180, 180, 180, 255)
BROWN     = (139,  69,  19, 255)
DARKBROWN = (100,  30,   0, 255)
BROWNBLACK= ( 50,  0,    0, 255)
CREAM     = (255, 255, 204, 255)
COLOURKEY = (  1,   2,   3, 255)
BLUETRANS = (  0,   0, 255, 100)


FIRSTNAMES = 'Robert Jenny Steve Jeff Alice Benjamin Yoric Fatima Reem Aya Suha Paul Becca Habiba \
				Mariam Irene Salma Liam Jacob Mohammed Ethan Cohen Jake Landon Elizabeth James John\
				Sophia Olivia Emma Brooklyn Ahmed Yusuf Chih-ming Chun-chieh Ji-hoon Abdullo Berat\
				Jim Catherine Earl Petunia Annabel Emily Nathan Jonathan Dylan Rachel Lucy Hannah\
				Jane Melissa Tabatha Willoughby Zanzibar Alexander Julius Atilla Mary Astrid Kylie\
				Josef Joseph Matilda Vladmir Charles Terence Lucifer Emmeline Elliot'.split()
LASTNAMES  = 'Prifti Loshi Leka Hoxha Gruber Huber Bauer Steiner Moser Jacobs Simon Martin Dupont\
				Dimitrov Trifonov Yanev Blagoev Hristov Yankov Novak Matic Hansen Magi Sepp Ilves\
				Koppel Parn Ilves Ivanov Pertov Putin Johannesen Thomsen Binks Rider Lehtonen Laine\
				David Garcia Morel Haynes Usher Martinez Francois Schmidt Schulz Wagner Hoffmann\
				Papantiniou Papadikas Nagy Toth Varga Mrphy Murray Jakupi Hoxha Sejdiu Borg Olsen\
				Berg Jacobsen Kozlov Kornilov Lenin Bogdanov Trotsky Nikolic Perez Reyes Armas Cruz\
				Smith Jones Wood Jackson Clarke Hall Green Roberts White Thompson Spoon Hall Green\
				Wright Robinson Wilson Taylor Khan Williams Roberts Lewis Cox Moore Kelly Rose Jenkins\
				Rees Driscoll Thomas Davies Edwards Reid MacDonald Robertson Clark Morrison Sanders'.split()