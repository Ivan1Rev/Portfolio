import random
import pygame

pygame.init()

window_width = 1074#display size
window_height = 788#display size
game_display = pygame.display.set_mode((window_width, window_height))#display size
gravity = 1.2
GREEN = (0,255,0)
images = ["marioR1.png","marioR2.png","marioR3.png"]
image = ["coin1.png","coin2.png","coin3.png","coin4.png","coin5.png","coin4.png","coin3.png","coin2.png","coin1.png"]
smallfont = pygame.font.SysFont('comicsansms',35)
bigfont = pygame.font.SysFont('OCR A Extended',150)
white = (255, 255, 255)
green = (0, 255, 0)
black = (0,0,0)



def write_H_score():
    f = open("highscore.txt","w")
    f.write(str(Mario.score))
    f.close()

def read_H_score():
    f = open("highscore.txt","r")
    data = f.read()
    f.close()
    return data




class Coin(pygame.sprite.Sprite):#
    def __init__(self):
        self.costume = 0
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/"+image[self.costume])
        self.size = self.image.get_rect().size
        self.image = pygame.transform.scale(self.image, (int(self.size[0] * 0.06), int(self.size[1] * 0.06)))
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.old_size = self.size
        self.rect.x = random.randint(0,1000)
        self.rect.y = -100
        self.next_y = self.rect.y
        self.next_x = self.rect.x
        self.gravity = 1.5
        self.On_the_block = False
        self.Coin_alert = False
        self.animation = False
        self.last_changed = 0






    def update(self):
        self.Coin_alert = pygame.sprite.spritecollide(self, sprite_group, False, False)
        if len(self.Coin_alert) > 0:
            Mario.score = Mario.score + 1
            self.kill()
            spawn_new_coin()


        self.On_the_block = pygame.sprite.spritecollide(self, obsticles_group, False, False)
        if len(self.On_the_block) == 0 and self.rect.y < 639:
            self.next_y = self.next_y + gravity
            self.touchingFloor = False
        self.rect.y = self.next_y


        if self.costume > 7:
            self.costume = 0


        if pygame.time.get_ticks() - self.last_changed > 100:
            self.old_x, self.old_y = self.rect.x, self.rect.y
            self.size = self.image.get_rect().size
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = self.old_x, self.old_y
            self.last_changed = pygame.time.get_ticks()
            self.image = pygame.image.load("images/" + image[self.costume])
            self.image = pygame.transform.scale(self.image, (int(self.old_size[0]), int(self.old_size[1])))
            self.costume = self.costume + 1


#updated
class ExtraMario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((25, 25))
        self.image = pygame.Surface([25, 25], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.center = (window_width / 2, window_height / 2)
        self.size = self.image.get_rect().size


    def update(self):
        self.rect.x = Mario.rect.x+7
        self.rect.y = Mario.rect.y+37


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
        self.rect.x = 600
        self.rect.y = 50
        self.next_y = self.rect.y
        self.next_x = self.rect.x
        self.move = 0
        self.touchingFloor = False
        self.direction = "right"
        self.animation = False
        self.last_changed = 0
        self.score = 0


    def update(self):
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


        self.On_the_block = pygame.sprite.spritecollide(Hitbox, obsticles_group, False, False)
        if len(self.On_the_block)==0 and Mario.rect.y < 620:
            self.next_y=self.next_y+gravity
            self.touchingFloor = False
        else:
            self.touchingFloor = True 
        self.rect.y = self.next_y
        self.rect.x = self.rect.x + self.move
        if self.rect.x > window_width:#Left
            self.rect.x = -85

        if self.rect.x < -100:#Left
            self.rect.x = 1047


    def jump(self):
        if self.touchingFloor == True or self.On_the_block == True:
            self.next_y = self.next_y - 135
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


def draw_score(score):
    text=smallfont.render("Score: "+str(score),True, white)
    game_display.blit(text,[0,0])

def draw_game_over():
    text=bigfont.render("Game Over ",True, GREEN)
    pygame.draw.rect(game_display,black, (130,100,850,150))
    game_display.blit(text, [150, 100])


def create_new_obsticles(possiton):
    obs = Character_obs(possiton[0],possiton[1], False)#550,350
    obsticles_group.add(obs)


obsticles_group = pygame.sprite.Group()

pos = [[350,550],
       [500,250],
       [700,350],
       [550,450],
       [300,150]
       #[100,200]
       ]

for p in pos:
    create_new_obsticles(p)


bg = pygame.image.load("images/Background.png")
bg = pygame.transform.scale(bg, (window_width, window_height))

Mario = Character_Mario()
sprite_group = pygame.sprite.Group()
sprite_group.add(Mario)


def spawn_new_coin():
    global coin, coin_group
    coin = Coin() #object creation
    coin_group = pygame.sprite.Group() #sprite goup creation to store and manipulate (update, draw) sprites
    coin_group.add(coin) #add newly created object to a sprite group


try:
    highscore = int(read_H_score())
except FileNotFoundError:
    print("file not found")
    write_H_score()



spawn_new_coin()
Hitbox = ExtraMario()
ExtraMario = pygame.sprite.Group()
ExtraMario.add(Hitbox)
while True:
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

    if Mario.score<20:
        obsticles_group.update()
        ExtraMario.update()
        coin_group.update()
        sprite_group.update()

        draw_score(Mario.score)
        obsticles_group.draw(game_display)
        ExtraMario.draw(game_display)
        coin_group.draw(game_display)
        sprite_group.draw(game_display)
    else:
        draw_game_over()
        if highscore<Mario.score:
            write_H_score()
            print("score")

    pygame.display.update()





