#Anenome image attributed to vecteezy.com <a href="https://www.vecteezy.com/free-vector/fish">Fish Vectors by Vecteezy</a>
import pygame
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
# from pygame.locals import *
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
game_state = "start_menu"

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("./images/fish.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Move the sprite based on keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keeps player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        # Randomly generates the enemy fish or hook sprite image
        enemies = ["./images/enemy1.png", "./images/enemy2.png"]
        self.surf = pygame.image.load(random.choice(enemies)).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # Randomly generates the starting position and speed
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Constantly moves the Enemy sprite right to left until reaching end of screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Friend(pygame.sprite.Sprite):
    def __init__(self):
        super(Friend, self).__init__()
        friends = ["./images/friend1.png", "./images/friend2.png", "./images/friend3.png", "./images/friend4.png"]
        picture = random.choice(friends)
        self.surf = pygame.image.load(picture).convert()
        # Corrects the sprite color key to match the background
        if picture != "./images/friend4.png" and picture != "./images/friend2.png":
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        else:
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)
    # Constantly move the Friend sprite right to left until reaching end of screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

class Home(pygame.sprite.Sprite):
    def __init__(self):
        super(Home, self).__init__()
        self.surf = pygame.image.load("./images/home.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                (SCREEN_WIDTH + 80),
                (SCREEN_HEIGHT - 100),
            )
        )
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

def start_menu():
    screen.blit(pygame.image.load("./images/bg.png"), (0,0))
    font = pygame.font.SysFont('arial', 80)
    title = font.render('Fishy Run', True, (255, 255, 255))
    font = pygame.font.SysFont('arial', 20)
    instructions = font.render("Use the arrow keys to move and find your way home.  Avoid the dangerous hooks and evil fish!", True, (255, 255, 255))
    start_button = font.render("Press spacebar to start", True, (255, 255, 255))
    screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, SCREEN_HEIGHT/4 - title.get_height()/2))
    screen.blit(instructions, (SCREEN_WIDTH/5.5 - start_button.get_width()/2, SCREEN_HEIGHT/2))
    screen.blit(start_button, (SCREEN_WIDTH/2 - start_button.get_width()/2, SCREEN_HEIGHT/2 + 100))
    pygame.display.update()

def game_over_menu():
    screen.blit(pygame.image.load("./images/bg.png"), (0,0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('Game Over', True, (255, 255, 255))
    restart_button = font.render('R - Restart', True, (255, 255, 255))
    quit_button = font.render('Q - Quit', True, (255, 255, 255))
    screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, SCREEN_HEIGHT/2 - title.get_height()/3))
    screen.blit(restart_button, (SCREEN_WIDTH/2 - restart_button.get_width()/2, SCREEN_HEIGHT/1.9 + restart_button.get_height()))
    screen.blit(quit_button, (SCREEN_WIDTH/2 - quit_button.get_width()/2, SCREEN_HEIGHT/2 + quit_button.get_height()/2))
    pygame.display.update()

def winner_menu():
    screen.blit(pygame.image.load("./images/bg.png"), (0,0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('Congrats you made it home!', True, (255, 255, 255))
    restart_button = font.render('R - Restart', True, (255, 255, 255))
    quit_button = font.render('Q - Quit', True, (255, 255, 255))
    screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, SCREEN_HEIGHT/2 - title.get_height()/3))
    screen.blit(restart_button, (SCREEN_WIDTH/2 - restart_button.get_width()/2, SCREEN_HEIGHT/1.9 + restart_button.get_height()))
    screen.blit(quit_button, (SCREEN_WIDTH/2 - quit_button.get_width()/2, SCREEN_HEIGHT/2 + quit_button.get_height()/2))
    pygame.display.update()
    
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create custom events for adding a new enemy, friend, or home
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 2000)
ADDFRIEND = pygame.USEREVENT + 2
pygame.time.set_timer(ADDFRIEND, 1000)
ADDHOME = pygame.USEREVENT + 3
pygame.time.set_timer(ADDHOME, 60000)

# Creates and stores all sprites
player = Player()
enemies = pygame.sprite.Group()
friends = pygame.sprite.Group()
homes = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # Quits if user presses escape key
            if event.key == K_ESCAPE:
                running = False

        # Quits if user clicks the x in the top right corner of window
        elif event.type == QUIT:
            running = False

        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == ADDFRIEND:
            new_friend = Friend()
            friends.add(new_friend)
            all_sprites.add(new_friend)

        elif event.type == ADDHOME:
            new_home = Home()
            homes.add(new_home)
            all_sprites.add(new_home)

    if game_state == "start_menu":
        start_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_state = "game"
            game_over = False

    # Resets sprites if it is game over
    elif game_state == "game_over":
        for entity in all_sprites:
            all_sprites.remove(entity)
        player = Player()
        enemies = pygame.sprite.Group()
        friends = pygame.sprite.Group()
        homes = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)
        game_over_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_state = "start_menu"
        if keys[pygame.K_q]:
            pygame.quit()
            quit()

    elif game_state == "winner":
        for entity in all_sprites:
            all_sprites.remove(entity)
        player = Player()
        enemies = pygame.sprite.Group()
        friends = pygame.sprite.Group()
        homes = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)
        winner_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_state = "start_menu"
        if keys[pygame.K_q]:
            pygame.quit()
            quit()

    elif game_state == "game":
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        enemies.update()
        friends.update()
        homes.update()

        # Player collided with enemy. Game over!
        if pygame.sprite.spritecollideany(player, enemies):
            game_over = True
            game_state = "game_over"

        # Player made it home safe!
        if pygame.sprite.spritecollideany(player, homes):
            game_over = True
            game_state = "winner"

        #Display background
        screen.blit(pygame.image.load("./images/bg.png"), (0,0))

        # Draw all our sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        tick = pygame.time.get_ticks()

        # Flip everything to the display
        pygame.display.flip()

        # Ensure we maintain a 30 frames per second rate
        clock.tick(30)

    elif game_over:
        game_state = "game_over"
        game_over = False
