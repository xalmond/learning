import pygame
import random
import math


# Initial settings
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Invasión Espacial')
icon = pygame.image.load('ovni.png')
pygame.display.set_icon(icon)
background = pygame.image.load('fondo.jpg')
_font = pygame.font.Font('Arcade.ttf', 32)

# Background sound settings
pygame.mixer.music.load('MusicaFondo.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
# Element sounds settings
sound_bullet = pygame.mixer.Sound('disparo.mp3')
sound_enemy_destroyed = pygame.mixer.Sound('Explosion.mp3')


class Element():
    def __init__(self, filename, status, axis_x, axis_y, axis_x_gap, axis_y_gap):
        self.image = pygame.image.load(filename)
        self.status = status
        self.axis_x = axis_x
        self.axis_y = axis_y
        self.axis_x_gap = axis_x_gap
        self.axis_y_gap = axis_y_gap

    def place(self):
        screen.blit(self.image, (self.axis_x, self.axis_y))


def new_enemy():
    return Element('enemigo.png', True,
                   random.randint(1, 800 - 64), random.randint(1, 200),
                   0.5, 25)


def there_is_contact(axis_x_1, axis_y_1, axis_x_2, axis_y_2):
    distance = math.sqrt(math.pow(axis_x_1 - axis_x_2, 2) + math.pow(axis_y_1 - axis_y_2, 2))
    if distance < 27:
        return True
    else:
        return False


# Init elements
score = 0
player = Element('cohete.png', True, 800 / 2 - 64 / 2, 600 - 64, 0, 0)
enemies_qty = 8
enemy = []
for i in range(enemies_qty):
    enemy.append(new_enemy())
bullets = []


# Gestionar los eventos hasta el quit
game_over = False
end = False
while not end:

    screen.blit(background, (0, 0))

    for event in pygame.event.get():

        # End Game
        if event.type == pygame.QUIT:
            end = True

        # Press arrow keys to move player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.axis_x_gap = -0.3
            elif event.key == pygame.K_RIGHT:
                player.axis_x_gap = 0.3
            # Press Space to shoot a bullet
            elif event.key == pygame.K_SPACE:
                sound_bullet.play()
                bullets.append(Element('bala.png', True,
                                       player.axis_x + 64 / 2 - 32 / 2, player.axis_y - 32,
                                       0, 0.6))

        # Release arrow keys to stop player
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.axis_x_gap = 0

    # Place player
    player.axis_x += player.axis_x_gap
    # Limit of position of player
    if player.axis_x < 0:
        player.axis_x = 0
    elif player.axis_x > 800 - 64:
        player.axis_x = 800 - 64

    # Place enemies
    for i in range(enemies_qty):
        enemy[i].axis_x += enemy[i].axis_x_gap
        # Limit of enemies position
        if enemy[i].axis_x < 0:
            enemy[i].axis_x = 0
            enemy[i].axis_y += enemy[i].axis_y_gap
            enemy[i].axis_x_gap = 0.5
        elif enemy[i].axis_x > 800 - 64:
            enemy[i].axis_x = 800 - 64
            enemy[i].axis_y += enemy[i].axis_y_gap
            enemy[i].axis_x_gap = -0.5

    # Place bullet
    for bullet in bullets:
        if bullet.status:
            bullet.axis_y -= bullet.axis_y_gap
            # Limit of bullet position
            if bullet.axis_y < 0:
                bullets.remove(bullet)
            else:
                for i in range(enemies_qty):
                    if enemy[i].status:
                        if there_is_contact(enemy[i].axis_x, enemy[i].axis_y, bullet.axis_x, bullet.axis_y):
                            sound_enemy_destroyed.play()
                            bullet.status = False
                            enemy[i] = new_enemy()
                            score += 1
                            break

    # Place elements
    for i in range(enemies_qty):
        if enemy[i].status:
            # End Game because player destroyed
            if there_is_contact(enemy[i].axis_x, enemy[i].axis_y, player.axis_x, player.axis_y):
                sound_enemy_destroyed.play()
                player.status = False
                bullets = []
                for j in range(enemies_qty):
                    enemy[j].status = False
                game_over = True
    if player.status:
        player.place()
    for bullet in bullets:
        if bullet.status:
            bullet.place()
    for i in range(enemies_qty):
        if enemy[i].status:
            enemy[i].place()
    # Place score
    score_text = _font.render(f'The score is {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    # Place Game Over
    if game_over:
        game_over_text = _font.render('GAME OVER', True, (255, 255, 255))
        screen.blit(game_over_text, (315, 300))

    pygame.display.update()

