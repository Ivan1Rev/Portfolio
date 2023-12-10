import pygame, time
pygame.font.init()

window_width = 1074  # display size --- x
window_height = 788  # display size --- y
game_display = pygame.display.set_mode((window_width, window_height))  # display size
red = (255,0,0)

enemy_count = 0

collnum = 0
tlbc = 0
FPS = 120
clock = pygame.time.Clock()
barrierD = ["barrier.png","barrier_1D.png","barrier_2D.png","barrier_3D.png","barrier_4D.png","barrier_5D.png"]
boom = ["boom1.png","boom2.png","boom3.png","boom4.png","boom5.png","boom5.png","boom6.png","boom7.png","boom8.png",
        "boom9.png"]
#("images/barriers/barrier.png")

def drawtext2(text, x, y, color, size): #font
    myfont = pygame.font.SysFont('Algerian', size)#font
    textsurface = myfont.render(text,False, color)
    game_display.blit(textsurface,(x, y))


class Enemy(pygame.sprite.Sprite):  #
    def __init__(self,positional_order,row_order):
        pygame.sprite.Sprite.__init__(self)
        self.picture = "images/main_enemy_1.png"
        self.image = pygame.image.load(self.picture)

        self.size = self.image.get_rect().size
        self.image = pygame.transform.scale(self.image, (int(self.size[0] / 15), int(self.size[1] / 15)))
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.old_size = self.size
        self.rect.x = 200+(positional_order*70)
        self.rect.y = 0+(row_order*50)
        self.frame = 0
        self.last_frame = 0
        self.x = 0
        self.frames_passed = 0
        self.steps = 0
        self.delta = -7
        self.num = 0
        self.check_steps = 20
        self.pic_1 = pygame.image.load("images/main_enemy_1.png")
        self.pic_2 = pygame.image.load("images/main_enemy_2.png")




    def update(self):
        self.frame += 1
        self.frames_passed = self.frame - self.last_frame
        #print(self.frames_passed)
        if self.frames_passed > 60:
            self.next_constume() #NEXT COST
            self.rect.x = self.rect.x + self.delta
            self.steps = self.steps + 1
            self.last_frame = self.frame

            if self.steps > self.check_steps:
                self.rect.y += 40
                self.steps = 0
                self.delta = self.delta * -1
                self.check_steps = 40


    def next_constume(self):
        if self.picture == "images/main_enemy_1.png":
            self.picture ="images/main_enemy_2.png"
            self.image = self.pic_2 #
            self.size = self.image.get_rect().size
            self.image = pygame.transform.scale(self.image, (int(self.size[0] / 15), int(self.size[1] / 15)))
        else:
            self.picture = "images/main_enemy_1.png"
            self.image = self.pic_1
            self.size = self.image.get_rect().size
            self.image = pygame.transform.scale(self.image, (int(self.size[0] / 15), int(self.size[1] / 15)))

class Player (pygame.sprite.Sprite):
    def __init__(self):
        self.enemy_count = 0
        pygame.sprite.Sprite.__init__(self)
        self.picture = "images/shooter.png"
        self.image = pygame.image.load(self.picture) #
        self.size = self.image.get_rect().size
        self.image = pygame.transform.scale(self.image, (int(self.size[0]), int(self.size[1])))
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.old_size = self.size
        self.rect.x = 450
        self.rect.y = 650


    def right(self):
        self.rect.x = self.rect.x + 2

    def left(self):
        self.rect.x = self.rect.x - 2


#    def update(self):


class Bullet (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.picture = "images/laser.png"
        self.image = pygame.image.load(self.picture)
        self.size = self.image.get_rect().size
        self.image = pygame.transform.scale(self.image, (int(self.size[0]), int(self.size[1])))
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.old_size = self.size
        self.rect.x = player.rect.x + 80
        self.rect.y = player.rect.y



    def update(self):
        global Enemy_group
        global enemy_count
        self.rect.y = self.rect.y - 5
        coll = pygame.sprite.spritecollide(self,Enemy_group,True)
        if coll:
            enemy_count += 1
            print(enemy_count)


            self.kill()

class Boom (pygame.sprite.Sprite):
# todo init boom when barrier dies
    def __init__ (self,x,y,flip):
        pygame.sprite.Sprite.__init__(self)
        self.boomcostume = 0
        self.image = pygame.image.load(f"images/boom/{boom[self.baoomcostume]}")
        self.size = self.image.get_rect().size
        self.image=pygame.transform.scale(self.image,(int(self.size[0]/3),int(self.size[1]/3)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y




class Barrier (pygame.sprite.Sprite):
    def __init__ (self,x,y,flip):
        pygame.sprite.Sprite.__init__(self)
        self.barriercostume = 0
        self.image = pygame.image.load(f"images/barriers/{barrierD[self.barriercostume]}")
        self.size = self.image.get_rect().size
        self.image=pygame.transform.scale(self.image,(int(self.size[0]/3),int(self.size[1]/3)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # self.next_x = self.rect.x
        # self.next_y = self.rect.y
        self.health = 5



    def update(self):
        coll = pygame.sprite.spritecollide(self, bullet_group, False)
        self.image = pygame.image.load(f"images/barriers/{barrierD[self.barriercostume]}")
        self.size = self.image.get_rect().size
        self.image = pygame.transform.scale(self.image, (int(self.size[0] / 3), int(self.size[1] / 3)))
        # self.rect = self.image.get_rect()
        # self.next_x = self.rect.x
        # self.next_y = self.rect.y
        if self.barriercostume >= 5:
            self.kill()
        if coll:
            coll[0].kill()
            self.health = self.health - 1
            if self.health == 0:
                self.barriercostume += 1
                print("Working")
                self.health = 5


Enemy_group = pygame.sprite.Group()


bg = pygame.image.load("images/Background.png")
bg = pygame.transform.scale(bg, (window_width, window_height))

for cat in range(5):
    for i in range(10):
        enemy = Enemy(i,cat)
        Enemy_group.add(enemy)


def create_new_obsticles(possition):
    bar = Barrier(possition[0],possition[1], False)#550,350
    Barrier_group.add(bar)


Barrier_group = pygame.sprite.Group()


obsticles_group = pygame.sprite.Group()

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)


bullet_group = pygame.sprite.Group()

pos = [[150,550],
       [450,550],
       [750,550]]

for p in pos:
    create_new_obsticles(p)


while True:
    #print(enemy_count)
    keys = pygame.key.get_pressed()
    tlbc = tlbc + 1
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
    if keys[pygame.K_d]:
        player.right()
    if keys[pygame.K_a]:
        player.left()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if tlbc >= 150:
            bullet = Bullet()
            bullet_group.add(bullet)
            tlbc = 0





    clock.tick(FPS)
    game_display.blit(bg, (0, 0))


    Enemy_group.update()
    Enemy_group.draw(game_display)

    player_group.update()
    player_group.draw(game_display)

    Barrier_group.update()
    Barrier_group.draw(game_display)

    bullet_group.update()
    bullet_group.draw(game_display)

    drawtext2("score = " + str(round(enemy_count, 2)), 25, 745, red, 60)
    pygame.display.update()


#C:\Users\Revia\Portfolio\Space invaders