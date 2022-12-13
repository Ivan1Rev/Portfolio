import random
import pygame
import glob

black = (0, 0, 0)
pygame.init()

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
    def __init__(self, number,row):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(random.choice(ls_of_img))  # ls_of_img[random.randint(0,len(ls_of_img)
        self.size = self.image.get_rect().size
        self.number = number
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
        self.rect.y = 200
        self.card_created = False
        self.child_created = False
        self.next_y = self.rect.y
        self.move = True
        self.finish_speed = 0.3


    def update(self):
        if self.move == True:
            self.next_y = self.next_y + controller.first_row_speed
            self.rect.y = self.next_y
        if self.move == False and self.rect.y < 370:
            self.next_y = self.next_y + self.finish_speed
            print(self.image)
            self.rect.y = self.next_y

        #print(controller.first_row_speed)
        if self.number > 0:
            if self.row == 1:
                if self.rect.y > 370 and self.child_created == False and controller.first_row_number > 0:
                    controller.first_row_number = controller.first_row_number - 1
                    card = Card(controller.first_row_number, self.row)
                    Card_group.add(card)
                    self.child_created = True

            elif self.row == 2:
                if self.rect.y > 370 and self.child_created == False and controller.second_row_number > 0:
                    controller.second_row_number = controller.second_row_number - 1
                    card = Card(controller.second_row_number, self.row)
                    Card_group.add(card)
                    self.child_created = True

            elif self.row == 3:
                if self.rect.y > 370 and self.child_created == False and controller.third_row_number > 0:
                    controller.third_row_number = controller.third_row_number - 1
                    card = Card(controller.third_row_number, self.row)
                    Card_group.add(card)
                    self.child_created = True


            if self.rect.y > 530:
                self.kill()


        if self.number == 0 and self.rect.y > 340:
            controller.first_row_speed = 0
            controller.second_row_number = 0
            controller.third_row_speed = 0
            self.move = False


class SpinControler():
    def __init__(self):
        self.first_row_number = 12
        self.first_row_speed = 5
        self.second_row_number = 12
        self.second_row_speed = 5
        self.third_row_number = 12
        self.third_row_speed = 5

        card = Card(self.first_row_number,1)#THIS IS THE CARD LINE____________________
        Card_group.add(card)

        card = Card(self.second_row_number, 2)  # THIS IS THE CARD LINE____________________
        Card_group.add(card)

        card = Card(self.third_row_number, 3)  # THIS IS THE CARD LINE____________________
        Card_group.add(card)

        self.last_frame = pygame.time.get_ticks()
    def update(self):
        self.curr_frame = pygame.time.get_ticks()
        if self.curr_frame - self.last_frame > 100:
            print(self.first_row_speed)
            if self.first_row_speed > 2:
                self.first_row_speed = self.first_row_speed - 0.1
                self.last_frame = pygame.time.get_ticks()
            if self.second_row_speed > 2:
                self.second_row_speed = self.second_row_speed - 0.1
                self.last_frame = pygame.time.get_ticks()
            if self.third_row_speed > 2:
                self.third_row_speed = self.third_row_speed - 0.1
                self.last_frame = pygame.time.get_ticks()







Card_group = pygame.sprite.Group()
controller = SpinControler()

body = Body()
Body_group = pygame.sprite.Group()
Body_group.add(body)





# 536
while True:
    game_display.fill((0, 50, 150))
    x, y = pygame.mouse.get_pos()
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
