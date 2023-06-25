import random
import pygame
import glob



window_width = 1074  # display size --- x
window_height = 788  # display size --- y
game_display = pygame.display.set_mode((window_width, window_height))  # display size



class Enemy(pygame.sprite.Sprite):  #
    def __init__(self,positional_order,row_order):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/main enemy.png")
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
#        print("frames passeed = ",self.frames_passed, "curr frame = ", self.frame, "last frame = ",self.last_frame)
        if self.frames_passed > 60:
            self.rect.x = self.rect.x + self.delta
            self.steps = self.steps + 1
            self.last_frame = self.frame


            if self.steps > self.check_steps:
#                if self.num > 1:
#                    self.rect.y += 20
#                    self.num = self.num + 1
#                else:
                self.rect.y += 40
                self.steps = 0
                self.delta = self.delta * -1
                self.check_steps = 40

#            print("if")
#        else:
#            print("else")


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




while True:
    game_display.blit(bg, (0, 0))


    Enemy_group.update()
    Enemy_group.draw(game_display)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

    pygame.display.update()