import random
import pygame
import glob

pygame.init()

import time
white = (255, 255, 255)
grey = (140, 135, 135)
smallfont = pygame.font.SysFont('Arial',35) #setting up the correct font and size for a score
bigfont = pygame.font.SysFont('Cooper Black',75)
black = (0, 0, 0)
cash = 500
opacity = 350
e1 = 0
textnum = 0



window_width = 1074  # display size --- x
window_height = 788  # display size --- y
game_display = pygame.display.set_mode((window_width, window_height))  # display size
ls_of_img = glob.glob("images/items/*")
ls_of_handle = glob.glob("images/the handle/*")

ShowWinningText = False
ShowWinningText3 = False




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

class MMoney(pygame.sprite.Sprite):  #
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/MinusMoney.png")
        self.size = self.image.get_rect().size
        self.image = pygame.transform.scale(self.image, (int(self.size[1] / 1), int(self.size[0] / 2.5)))
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.old_size = self.size
        self.rect.x = 70.5
        self.rect.y = 30

class Card(pygame.sprite.Sprite):
    def __init__(self, row):
        pygame.sprite.Sprite.__init__(self)

        self.random_index = random.randint(0,len(ls_of_img)-1)


        #if self.rand_img

        self.image = pygame.image.load(ls_of_img[self.random_index])  # ls_of_img[random.randint(0,len(ls_of_img)
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
        global Card_group

        self.card1 = Card(1)
        self.card2 = Card(2)
        self.card3 = Card(3)

        Card_group = pygame.sprite.Group()

        Card_group.add(self.card1)
        Card_group.add(self.card2)
        Card_group.add(self.card3)
        # (len(Card_group))

        self.card1I = (ls_of_img[self.card1.random_index])
        self.card2I = (ls_of_img[self.card2.random_index])
        self.card3I = (ls_of_img[self.card3.random_index])

    def check_win(self):
        global cash,ShowWinningText

        if self.card1I ==self.card2I == self.card3I:
            print("YOU WON!")
            cash += 1000
            ShowWinningText3 = True

        if self.card1I == self.card2I or self.card3I == self.card1I or self.card2I == self.card3I:
            print("you got lucky")
            cash += 100
            ShowWinningText = True



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
        global opacity
        x_mouse = pygame.mouse.get_pos()[0]
        y_mouse = pygame.mouse.get_pos()[1]
        if x_mouse > 820 and x_mouse < 920 and  y_mouse > 250 and y_mouse < 325:
            if pygame.mouse.get_pressed()[0] == True:
                self.animation_start = True



        if self.animation_start == True:
            self.current_tics = pygame.time.get_ticks()
            time_passed = self.current_tics - self.last_ticks
            if time_passed > 150:
                if self.imageNumber == len(ls_of_handle)-1:

                    self.animation_start = False
                    self.score_added = False
                    self.imageNumber = 0
                    cash = cash - 10
                    opacity = 0
                    controller = SpinControler()
                    controller.check_win()






                else:
                    self.imageNumber = self.imageNumber + 1
                    self.image = pygame.image.load(ls_of_handle[self.imageNumber])

                self.last_ticks = pygame.time.get_ticks()

def draw_text(text):
    text = smallfont.render("Cash: " + str(text)+ "$", True, white )
    game_display.blit(text, [0, 0])

def draw_WT():
    text = bigfont.render("YOU WIN!", True, grey)
    game_display.blit(text, [355, 655])
    text = bigfont.render("YOU WIN!", True, white )
    game_display.blit(text, [350, 650])

def draw_WT3():
    text = bigfont.render("Insane WINNER!!!", True, grey)
    game_display.blit(text, [225, 655])
    text = bigfont.render("Insane WINNER!!!", True, white)
    game_display.blit(text, [220, 650])
       # if x of mouse is in boudries of 820 and 920 and on y axis it's between 250 and 450
pygame.mouse.get_pressed()

Card_group = pygame.sprite.Group()


body = Body()
Body_group = pygame.sprite.Group()
Body_group.add(body)


body = Body()
Body_group = pygame.sprite.Group()
Body_group.add(body)


mmoney = MMoney()
MMoney_group = pygame.sprite.Group()
MMoney_group.add(mmoney)


handle = Handle()
handle_group = pygame.sprite.Group()
handle_group.add(handle)

Card_group = pygame.sprite.Group()


def draw_rect(alpha):
    s = pygame.Surface((100, 100))  # the size of your rect
    s.set_alpha(alpha)  # alpha level
    s.fill((0, 50, 150))  # this fills the entire surface
    game_display.blit(s, (50, 40))  # (0,0) are the top-left coordinates

# 536
while True:

    game_display.fill((0, 50, 150))
    x, y = pygame.mouse.get_pos()
    draw_text(cash)
    opacity = opacity + 5


    if ShowWinningText == True:
        draw_WT()
        textnum += 1
        if textnum > 500:
            ShowWinningText = False
            textnum = 0

    if ShowWinningText3 == True:
        draw_WT3()
        textnum += 1
        if textnum > 500:
            ShowWinningText3 = False
            textnum = 0

    #print(x, y)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

            if event.key == pygame.K_e:
                ShowWinningText3 = True

            if event.key == pygame.K_r:
                ShowWinningText = True

            if event.key == pygame.K_t:
                cash = cash + 100






    Card_group.update()
    Body_group.update()
    handle_group.update()
    MMoney_group.update()

    x_mouse = pygame.mouse.get_pos()[0]
    y_mouse = pygame.mouse.get_pos()[1]

    if x_mouse > 820 and x_mouse < 920 and y_mouse > 250 and y_mouse < 325:
        if pygame.mouse.get_pressed()[0] == True:

            '''
            print("generating cards")
            card1 = Card(1)
            card2 = Card(2)
            card3 = Card(3)

            Card_group = pygame.sprite.Group()

            Card_group.add(card1)
            Card_group.add(card2)
            Card_group.add(card3)
            #(len(Card_group))

            card1I = (ls_of_img[card1.random_index])
            card2I = (ls_of_img[card2.random_index])
            card3I = (ls_of_img[card3.random_index])
    try:
        if card1I == card2I == card3I and handle.animation_start == False and handle.score_added == False:
            print("YOU WON!")
            cash += 1000
            handle.score_added = True
        if card1I == card2I or card3I == card1I or card2I == card3I and handle.animation_start == False and handle.score_added == False:
            print("you got lucky")
            cash += 100
            handle.score_added = True

    
    except NameError:
        print("class not defined ")
        
    '''

    Card_group.draw(game_display)
    Body_group.draw(game_display)
    handle_group.draw(game_display)
    MMoney_group.draw(game_display)
    draw_rect(opacity)

    pygame.display.update()



