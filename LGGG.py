import pygame

#1. 뽑기 초기화
pygame.init()

#2. 뽑기 옵션 설정
size = [800, 400]
screen = pygame.display.set_mode(size)
white = (255,255,255)
screen.fill(white)

title = "LGGG lots" #직접 입력 받기
pygame.display.set_caption(title)

nameList = "yoon.german"

#3. 스크린 설정
clock = pygame.time.Clock()

class obj:
    def __init__(self):
        self.x = 0 
        self.y = 0
    def put_img(self,address):
        if address[-3:]== "png":
            self.img = pygame.image.load(address).convert_alpha()
        else:
            self.img = pygame.image.load(address)
            self.sx, self.sy = self.img.get_size()
    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx,sy))
        self.sx, self.sy = self.img.get_size()
    def show(self):
        screen.blit(self.img, (self.x, self.y))

img1 = pygame.image.load("images/IMG1.PNG").convert_alpha()
img1 = pygame.transform.scale(img1,(400,400))

img2 = pygame.image.load("images/IMG2.PNG").convert_alpha()
img2 = pygame.transform.scale(img2,(400,400))

img3 = pygame.image.load("images/IMG3.PNG").convert_alpha()
img3 = pygame.transform.scale(img3,(400,400))

k = 0
space_stop = False

#4. 메인 이벤트 
run = True
while run:

    # 4-1. FPS 설정
    clock.tick(5)

    # 4-2. 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif space_stop  == False and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space_stop  = True
                print(space_stop)
               
        elif space_stop  == False and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                column_index = event.pos[0] 
                row_index = event.pos[1] 
                space_stop  = True

        elif space_stop  == True and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space_stop  = False
                print(space_stop)
               
        elif space_stop  == True and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                column_index = event.pos[0] 
                row_index = event.pos[1] 
                space_stop  = False

    # 4-3. 입력, 시간에 따른 변화
    k += 1
    
    if k % 2 == 0:
        screen.blit(img1,(0,0))
    else:
        screen.blit(img2,(0,0))

    if space_stop == True:
        screen.blit(img3,(0,0))
        
    # 4-4. 그리기
    #screen.fill(white)
    # screen.blit(img1,(0,0))
    # 결과 띄우기
    font = pygame.font.Font("font/DaeHan.app")
    text = font.render("nameList:{}".format(nameList), True, (0,0,255)) #True -> 글자를 매끄럽게
    
    # 4-5. 업데이트
    pygame.display.flip()
    
    # name = 12
    # while name != 0:

    #     #4-1. 뽑기 종료
        
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             name = 0
        
    #     #4-2. 숨기기
        
    #     #4-3. 남은 사람 목록
        
    #     #4-4. 배경
    #     screen.fill(LGGGImg)
        
    #     #4-5. 업데이트
    #     pygame.disply.flip()
    
#5. 종료
pygame.quit()
# import pygame

# WHITE = (255,255,255)
# pad_width = 2048
# pad_height = 2048

# def runGame():
#     global gamepad

#     empty = False
#     while not empty:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 empty = True

#         gamepad.fill(WHITE)
#         pygame.display.update()

#     pygame.quit()

# def initGame():
#     global gamepad
    
#     pygame.init()
#     gamepad = pygame.display.set_mode((pad_width, pad_height))
#     pygame.display.set_caption('LGGG Lots')

#     runGame()

# initGame()