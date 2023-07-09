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




    def update(self):
        self.frame += 1
        self.frames_passed = self.frame - self.last_frame
        print(self.frames_passed)
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
            self.image = pygame.image.load(self.picture)
            self.size = self.image.get_rect().size
            self.image = pygame.transform.scale(self.image, (int(self.size[0] / 15), int(self.size[1] / 15)))
        else:
            self.picture = "images/main_enemy_1.png"
            self.image = pygame.image.load(self.picture)
            self.size = self.image.get_rect().size
            self.image = pygame.transform.scale(self.image, (int(self.size[0] / 15), int(self.size[1] / 15)))

class Player (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.picture = "images/shooter.png"
        self.image = pygame.image.load(self.picture)
        self.size = self.image.get_rect().size
        self.image = pygame.transform.scale(self.image, (int(self.size[0] / 15), int(self.size[1] / 15)))
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.old_size = self.size
        self.rect.x = 100
        self.rect.y = 100

board = [
    [0,0,0],
    [0,1,0],
    [0,0,1]
]
x = [1,1,1,1,1,1,1,1,1,1,1,1,0]
y = [0,0,0,0,0,0,0,0,0,0,0,0,-1]




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

while True:



    clock.tick(FPS)
    game_display.blit(bg, (0, 0))


    Enemy_group.update()
    Enemy_group.draw(game_display)

    player_group.update()
    Enemy_group.draw(game_display)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

    pygame.display.update()