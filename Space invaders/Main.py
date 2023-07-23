import pygame


window_width = 1074  # display size --- x
window_height = 788  # display size --- y
game_display = pygame.display.set_mode((window_width, window_height))  # display size

FPS = 120
clock = pygame.time.Clock()


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
        self.rect.x = self.rect.x + 10

    def left(self):
        self.rect.x = self.rect.x - 10


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
        self.rect.y = self.rect.y - 5
        coll = pygame.sprite.spritecollide(self,Enemy_group,True)
        if coll:
            self.kill()



Enemy_group = pygame.sprite.Group()


bg = pygame.image.load("images/Background.png")
bg = pygame.transform.scale(bg, (window_width, window_height))

for cat in range(5):
    for i in range(10):
        enemy = Enemy(i,cat)
        Enemy_group.add(enemy)



player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)


bullet_group = pygame.sprite.Group()




while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key==pygame.K_d:
              player.right()
            if event.key==pygame.K_a:
              player.left()
            if event.key==pygame.K_SPACE:
                bullet = Bullet()
                bullet_group.add(bullet)





    clock.tick(FPS)
    game_display.blit(bg, (0, 0))


    Enemy_group.update()
    Enemy_group.draw(game_display)

    player_group.update()
    player_group.draw(game_display)


    bullet_group.update()
    bullet_group.draw(game_display)

    pygame.display.update()