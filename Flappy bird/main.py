import pygame, time, random#import
pygame.init()
pygame.init()
window_width = 1024#display size
window_height = 768#display size
game_display = pygame.display.set_mode((window_width, window_height))#display size
red = (255,0,0)#colour
pink = (255, 102, 179)
gravity = 0.5





def drawtext2(text, x, y, color, size): #font 
    myfont = pygame.font.SysFont('Algerian', size)#font
    textsurface = myfont.render(text,False, color)
    game_display.blit(textsurface,(x, y))


class Game():
    def __init__(self):
        self.disp_text = False
        self.score = 0
        


class Character_bird(pygame.sprite.Sprite):#if clicked on it will choose that as waht you want aka rock
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bird.png")
        self.size = self.image.get_rect().size
        self.image=pygame.transform.scale(self.image,(int(self.size[0]*0.1),int(self.size[1]*0.1)))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 300
        self.next_y = self.rect.y
        self.next_x = self.rect.x
        

    def update(self):
        self.next_y=self.next_y+gravity
        self.rect.y = self.next_y
        death = pygame.sprite.spritecollide(self,obsticles_group,False)
        if self.rect.y > 768:
            death = True      
        if death:
            self.kill()
            print("dead")
            game.disp_text = True


    def jump(self):
        self.next_y = self.next_y - 100
        self.rect.y = self.next_y



class Character_obs(pygame.sprite.Sprite):
    def __init__ (self,x,y,flip):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/pipe.png")
        self.size = self.image.get_rect().size
        self.image=pygame.transform.scale(self.image,(65,413))
        self.rect = self.image.get_rect()
        self.score_has_changed = False
        if flip == True:
            self.image = pygame.transform.rotate(self.image, 180)        
        self.rect.x = x
        self.rect.y = y
        self.next_x = self.rect.x


    def update(self):
        self.next_x=self.next_x-0.5
        self.rect.x = self.next_x
        if self.rect.x < 0-self.size[0]:
            self.kill()
        if self.rect.x < bird.rect.x and self.score_has_changed == False:
            #self.score_has_changed = True
            game.score = game.score + ((1/572)/2)#score


def create_new_obsticles():
    y1 = random.randint(350,550)
    obs = Character_obs(1200,y1, False)#550,350
    obsticles_group.add(obs)
    y2 = random.randint(-250,-120)
    obs = Character_obs(1200,y2, True)#-150,-250
    obsticles_group.add(obs)



def right_obs(obs_group):
    coords = []
    for obs in obs_group:
        coords.append(obs.rect.x)
    if len(coords) > 0:
        return max(coords)
    else:
        return 0
        


global obsticles_group

game = Game()
obsticles_group = pygame.sprite.Group()
sprite_group = pygame.sprite.Group()
bird = Character_bird()
sprite_group.add(bird)
bg = pygame.image.load("images/background.png")
while True:
    ran_num = random.randint(0,4000)
    if ran_num >= 0 and ran_num <= 5:
        x_of_last_pipe = right_obs(obsticles_group)
        if x_of_last_pipe < 1000:
            create_new_obsticles()
    game_display.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key==pygame.K_SPACE:
                bird.jump()
                
        if event.type == pygame.QUIT:
            pygame.quit()
    if game.disp_text == True:
        drawtext2("Bro your trash at the game.",450,100,red,30)
    sprite_group.update()
    obsticles_group.update()
    sprite_group.draw(game_display)
    obsticles_group.draw(game_display)
    drawtext2("score="+str(round(game.score,2)),25,25,pink,60)
    pygame.display.update()#
    





