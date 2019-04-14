import pygame
  
# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
# Telinha
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 650
 
 
class Player(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        width = 40
        height = 40
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
 
        
        self.rect = self.image.get_rect()
 
        
        self.change_x = 0
        self.change_y = 0
 
        
        self.level = None
 
    def update(self):
        
        self.calc_grav()
 
        self.rect.x += self.change_x
 
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
  
                self.rect.left = block.rect.right
 
        self.rect.y += self.change_y
 
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
           
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
           
            self.change_y = 0
 
            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x
 
    def calc_grav(self):
       
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 

        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
 
    def jump(self):

        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
 
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10
 
    def go_left(self):
        self.change_x = -6
 
    def go_right(self):

        self.change_x = 6
 
    def stop(self):

        self.change_x = 0
 
 
class Platform(pygame.sprite.Sprite):
     def __init__(self, width, height):

        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(YELLOW)
 
        self.rect = self.image.get_rect()
 
class Platform2(pygame.sprite.Sprite):
 
    def __init__(self, width, height):
        
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()


class MovingPlatform(Platform):
    change_x = 0
    change_y = 0
 
    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0
 
    player = None
 
    level = None

    
    def update(self):
   
        self.rect.x += self.change_x
 
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:

            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
   
                self.player.rect.left = self.rect.right

        self.rect.y += self.change_y

        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:

            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom
 
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
 
        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1



class FallingPlatform(Platform2):
    change_x = 0
    change_y = 0
 
    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0
 
    player = None
 
    level = None


    def update(self):
        
        self.rect.y += self.change_y

 
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            
            
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom
            
                
 
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
 
        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1


class Level(object):
 
    def __init__(self, player):

        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
         

        self.background = None
     
  
        self.world_shift = 0
        self.level_limit = -1000

    def update(self):
 
        self.platform_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):
  
 
        screen.fill(BLACK)
 
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
 
    def shift_world(self, shift_x):
 
        self.world_shift += shift_x
 
        for platform in self.platform_list:
            platform.rect.x += shift_x
 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
 
 
class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 

        Level.__init__(self, player)
 
        self.level_limit = -1700
 

        level = [[210, 60, 500, 500],
                 [500, 30, 400, 220],
                 [200, 50, 800, 400],
                 [300, 60, 1000, 500],
                 [160, 70, 1120, 280],
                 ]

        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
 
        # Add a custom moving platform
        block = MovingPlatform(50, 20)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = MovingPlatform(50, 20)
        block.rect.x = 1600
        block.rect.y = 180
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = MovingPlatform(50, 20)
        block.rect.x = 1850
        block.rect.y = 380
        block.boundary_left = 1450
        block.boundary_right = 1900
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = MovingPlatform(50, 20)
        block.rect.x = 1890
        block.rect.y = 480
        block.boundary_left = 1450
        block.boundary_right = 2100
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = MovingPlatform(50, 20)
        block.rect.x = 1550
        block.rect.y = 560
        block.boundary_left = 1550
        block.boundary_right = 2100
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        #FAll
        block = FallingPlatform(200, 60)
        block.rect.x = 200
        block.rect.y = 450
        block.boundary_top = 200
        block.boundary_bottom = 550
        block.boundary_left = 100
        block.boundary_right = 300
        block.change_y = 1
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        
# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """
 
    def __init__(self, player):
        """ Create level 1. """

        Level.__init__(self, player)
 
        self.level_limit = -1500
 
        level = [[40, 70, 500, 550],
                 [40, 70, 600, 450],
                 [40, 70, 700, 350],
                 [300, 50, 770, 210],
                 [1000, 800, 2100, 300],
                 ]

        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
 
        block = MovingPlatform(70, 70)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
 
        block = MovingPlatform(70, 70)
        block.rect.x = 1700
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = MovingPlatform(70, 70)
        block.rect.x = 1900
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = FallingPlatform(200, 10)
        block.rect.x = 1120
        block.rect.y = 280
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
def main():
    """ Main Program """
    pygame.init()
 
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Platformer with moving platforms")
 
    player = Player()
 
    level_list = []
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))
 
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
 
    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
 
    done = False

    clock = pygame.time.Clock()
 
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
 
  
        active_sprite_list.update()
 
        current_level.update()
 
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)
 
 
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)

        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            if current_level_no < len(level_list)-1:
                player.rect.x = 120
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
            else:
 
                done = True

        current_level.draw(screen)
        active_sprite_list.draw(screen)
 

        clock.tick(60)
 

        pygame.display.flip()
  
    pygame.quit()
 
if __name__ == "__main__":
    main()
