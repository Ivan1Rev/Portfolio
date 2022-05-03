import pygame
pygame.init()
pygame.init()
window_width = 1074#display size
window_height = 788#display size
game_display = pygame.display.set_mode((window_width, window_height))#display size
gravity = 0.5
images = ["marioR1.png","marioR2.png","marioR3.png"]


#updated

class Character_Mario(pygame.sprite.Sprite):#if clicked on it will choose that as waht you want aka rock
    def __init__(self):
        self.costume = 0
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/"+images[self.costume])
        self.size = self.image.get_rect().size
        self.image=pygame.transform.scale(self.image,(int(self.size[0]*0.15),int(self.size[1]*0.15)))
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.old_size = self.size
        self.rect.x = 100
        self.rect.y = 300
        self.next_y = self.rect.y
        self.next_x = self.rect.x
        self.move = 0
        self.touchingFloor = False
        self.direction = "right"
        self.animation = False
        self.last_changed = 0
        
        


    def update(self):
        self.On_the_block = pygame.sprite.spritecollide(Mario, obsticles_group, False, False)


        if self.costume > 2:
            self.costume = 0



        #animation

        if self.animation == True:
            if pygame.time.get_ticks() - self.last_changed > 60:
                self.old_x, self.old_y = self.rect.x, self.rect.y
                self.size = self.image.get_rect().size
                self.rect = self.image.get_rect()
                self.rect.x, self.rect.y = self.old_x, self.old_y
                self.last_changed = pygame.time.get_ticks()
                if self.direction == "right":
                    self.image = pygame.image.load("images/"+images[self.costume])
                    self.image=pygame.transform.scale(self.image,(int(self.old_size[0]),int(self.old_size[1])))
                    self.direction = "right"
                else:
                    self.image = pygame.image.load("images/" + images[self.costume])
                    self.image = pygame.transform.scale(self.image, (int(self.old_size[0]), int(self.old_size[1])))
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.direction = "left"
                self.costume = self.costume + 1




        if len(self.On_the_block)>0:
            print(len(self.On_the_block))
            self.next_y=self.next_y+gravity
            self.touchingFloor = False
        else:
            self.touchingFloor = True 
        self.rect.y = self.next_y
        self.rect.x = self.rect.x + self.move
        if self.rect.x > window_width:#Left
            self.rect.x = -85
            print(self.rect.x)
        if self.rect.x < -100:#Left
            self.rect.x = 1047


    def jump(self):
        if self.touchingFloor == True or self.On_the_block == True:
            self.next_y = self.next_y - 90
            self.rect.y = self.next_y

    def forward(self):
        self.animation = True
        if self.direction != "right":
            self.image = pygame.transform.flip(self.image, True, False)
            self.direction = "right"
        self.move = 1


    def backwards(self):
        self.animation = True
        if self.direction != "left":
            self.image = pygame.transform.flip(self.image, True, False)
            self.direction = "left"
        self.move = -1


class Character_obs(pygame.sprite.Sprite):
    def __init__ (self,x,y,flip):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/Brick1.png")
        self.size = self.image.get_rect().size
        self.image=pygame.transform.scale(self.image,(int(self.size[0]*0.55),int(self.size[1]*0.55)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.next_x = self.rect.x

def create_new_obsticles(possiton):
    obs = Character_obs(possiton[0],possiton[1], False)#550,350
    obsticles_group.add(obs)


obsticles_group = pygame.sprite.Group()

pos = [[400,550],
       [500,250],
       [700,350],
       [550,450]
       ]

for p in pos:
    create_new_obsticles(p)

'''
i = 0
while i < len(pos):
    create_new_obsticles(pos[i])
    i = i + 1
'''




bg = pygame.image.load("images/Background.png")
bg = pygame.transform.scale(bg, (window_width, window_height))
sprite_group = pygame.sprite.Group()
Mario = Character_Mario() 
sprite_group.add(Mario)
while True:
    #print(Mario.touchingFloor)
    game_display.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key==pygame.K_w:
                Mario.jump()
            if event.key==pygame.K_d:
                Mario.forward()
            if event.key==pygame.K_a:
                Mario.backwards()
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_a or event.key==pygame.K_d:
                Mario.move = 0
                Mario.animation = False
    obsticles_group.update()
    obsticles_group.draw(game_display)
    sprite_group.update()
    sprite_group.draw(game_display)
    pygame.display.update()

