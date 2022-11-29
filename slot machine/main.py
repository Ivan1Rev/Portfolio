import random
import pygame
import glob
import time



black = (0, 0, 0)

speed = 5

window_width = 1074  # display size --- x
window_height = 788  # display size --- y
game_display = pygame.display.set_mode((window_width, window_height))  # display size
ls_of_img = glob.glob("images/items/*")


class Body(pygame.sprite.Sprite):  #
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/body.png")
        self.size = self.image.get_rect().size
        self.image = pygame.transform.scale(self.image, (int(self.size[0] * 1), int(self.size[1] * 1)))
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.old_size = self.size
        self.rect.x = 275
        self.rect.y = 100


class Card(pygame.sprite.Sprite):
    def __init__(self, first,last):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(random.choice(ls_of_img))  # ls_of_img[random.randint(0,len(ls_of_img)
        self.size = self.image.get_rect().size
        self.first = first
        self.last = last
        self.image = pygame.transform.scale(self.image, (int(self.size[0] * 0.9), int(self.size[1] * 0.9)))
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.old_size = self.size
        self.rect.x = 315
        if self.first == True:
            self.rect.y = 370
        else:# not the first card
            self.rect.y = 200  # top
        self.card_created = False

    def update(self):
        self.rect.y = self.rect.y + controller.first_speed
        print(self.last)
        if self.last == False:
            if self.rect.y > 542 and self.last != True:
                self.kill()
            if self.rect.y > 370 and self.card_created == False and self.first == False: #Flag
                card = Card(False,False)
                Card_group.add(card)
                self.card_created = True
        else:
            if self.rect.y > 540:
                self.rect.y = 540







class SpinControler():
    def __init__(self):
        self.first_speed = random.randint(20,25)
        self.first_row_last_card_created = False
        card = Card(True,False)
        Card_group.add(card)
        card = Card(False,False)
        Card_group.add(card)

    def update(self):
       #print(self.first_speed)
        if self.first_speed < 3:
            card = Card(False, True)
            Card_group.add(card)
            self.first_row_last_card_created = False
        if self.first_speed > 0:
            self.first_speed = self.first_speed - 0.03
        else:
            self.first_speed = 0







Card_group = pygame.sprite.Group()

controller = SpinControler()

body = Body()
Body_group = pygame.sprite.Group()
Body_group.add(body)





# 536
while True:
    game_display.fill((0, 50, 150))
    x, y = pygame.mouse.get_pos()
    # print(x, y)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
    controller.update()

    Card_group.update()
    Body_group.update()


    Card_group.draw(game_display)
    Body_group.draw(game_display)


    pygame.display.update()
