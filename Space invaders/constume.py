if self.frames_passed % 2 == 0:
    self.image = pygame.image.load("images/main_enemy_2.png")
    self.size = self.image.get_rect().size
    self.image = pygame.transform.scale(self.image, (int(self.size[0] / 15), int(self.size[1] / 15)))
else:
    self.image = pygame.image.load("images/main_enemy_1.png")
    self.size = self.image.get_rect().size
    self.image = pygame.transform.scale(self.image, (int(self.size[0] / 15), int(self.size[1] / 15)))

