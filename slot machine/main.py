import random
import pygame
import glob
pygame.init()

import time
white = (255, 255, 255)
smallfont = pygame.font.SysFont('Arial',35) #setting up the correct font and size for a score
black = (0, 0, 0)
cash = 500

window_width = 1074  # display size --- x
window_height = 788  # display size --- y
game_display = pygame.display.set_mode((window_width, window_height))  # display size
ls_of_img = glob.glob("images/items/*")
ls_of_handle = glob.glob("images/the handle/*")



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
    def __init__(self, row):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(random.choice(ls_of_img))  # ls_of_img[random.randint(0,len(ls_of_img)
        self.size = self.image.get_rect().size
        self.image = pygame.transform.scale(self.image, (int(self.size[0] * 0.9), int(self.size[1] * 0.9)))
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.old_size = self.size
        self.row = row
        if self.row == 1 :
            self.rect.x = 315
        elif self.row == 2:
            self.rect.x = 479
        elif self.row == 3:
            self.rect.x = 644
        self.rect.y = 370
        self.card_created = False
        self.child_created = False
        self.next_y = self.rect.y
        self.move = True
        self.finish_speed = 0.3




class SpinControler():
    def __init__(self):
        pass

class Handle(pygame.sprite.Sprite):
    def __init__(self):
        self.imageNumber = 0
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(ls_of_handle[self.imageNumber])  # ls_of_img[random.randint(0,len(ls_of_img)
        self.size = self.image.get_rect().size
        self.image = pygame.transform.scale(self.image, (int(self.size[0] * 0.9), int(self.size[1] * 0.9)))
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.rect.x =814
        self.rect.y =240
        self.animation_start = False
        self.last_ticks = 0
        self.current_tics = 0

    def update(self):
        global cash
        x_mouse = pygame.mouse.get_pos()[0]
        y_mouse = pygame.mouse.get_pos()[1]
        if x_mouse > 820 and x_mouse < 920 and  y_mouse > 250 and y_mouse < 325:
            #print(pygame.mouse.get_pressed())
            if pygame.mouse.get_pressed()[0] == True:
                self.animation_start = True

        if self.animation_start == True:
            self.current_tics = pygame.time.get_ticks()
            time_passed = self.current_tics - self.last_ticks
            #print("last animation:", self.last_ticks, "current ticks",self.current_tics,"Difference",time_passed)
            if time_passed > 150:
                if self.imageNumber == len(ls_of_handle)-1:
                    self.animation_start = False
                    print("last time animation finished at :",pygame.time.get_ticks())
                    self.imageNumber = 0
                    cash = cash - 50

                else:
                    self.imageNumber = self.imageNumber + 1
                    self.image = pygame.image.load(ls_of_handle[self.imageNumber])

                self.last_ticks = pygame.time.get_ticks()

def draw_text(text):
    text = smallfont.render("Cash: " + str(text)+ "$", True, white )
    game_display.blit(text, [0, 0])


       # if x of mouse is in boudries of 820 and 920 and on y axis it's between 250 and 450
pygame.mouse.get_pressed()

Card_group = pygame.sprite.Group()


body = Body()
Body_group = pygame.sprite.Group()
Body_group.add(body)


handle = Handle()
handle_group = pygame.sprite.Group()
handle_group.add(handle)


# 536
while True:

    game_display.fill((0, 50, 150))
    x, y = pygame.mouse.get_pos()
    draw_text(cash)

    #print(x, y)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()



    Card_group.update()
    Body_group.update()
    handle_group.update()

    x_mouse = pygame.mouse.get_pos()[0]
    y_mouse = pygame.mouse.get_pos()[1]

    if x_mouse > 820 and x_mouse < 920 and y_mouse > 250 and y_mouse < 325:
        if pygame.mouse.get_pressed()[0] == True:

            card1 = Card(1)
            card2 = Card(2)
            card3 = Card(3)

            Card_group = pygame.sprite.Group()

            Card_group.add(card1)
            Card_group.add(card2)
            Card_group.add(card3)
            print(len(Card_group))

    Card_group.draw(game_display)
    Body_group.draw(game_display)
    handle_group.draw(game_display)

    pygame.display.update()



