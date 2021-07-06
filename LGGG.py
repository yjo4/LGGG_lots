import pygame

WHITE = (255,255,255)
pad_width = 2048
pad_height = 2048

def runGame():
    global gamepad

    empty = False
    while not empty:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                empty = True

        gamepad.fill(WHITE)
        pygame.display.update()

    pygame.quit()

def initGame():
    global gamepad
    
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('LGGG Lots')

    runGame()

initGame()