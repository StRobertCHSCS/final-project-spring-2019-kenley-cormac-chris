import arcade
import time

# defining constants

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOUR = arcade.color.GREEN
SPRITE_COLOUR = arcade.color.ARTICHOKE
PLAYER_SPEED = 5
<<<<<<< HEAD
BULLET_SPEED = 20
=======
GRAVITY = 5
JUMP_SPEED = 10
>>>>>>> 724d9c029929b040ca7881f0869f94865b715c7c
# creating game class

class Player():
    def __init__(self, center_x, center_y, change_x, change_y):
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = change_x
        self.change_y = change_y
        self.player_sprite_list = arcade.SpriteList()

    def draw(self):
        size = 50
        arcade.draw_rectangle_filled(self.center_x, self.center_y, size, size, SPRITE_COLOUR)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

class Bullet:
    def __init__(self, center_x, center_y, change_x, change_y):
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = change_x
        self.change_y = change_y
        # self.bullet_sprite_list = arcade.SpriteList()

    def draw(self):
        width = 10
        arcade.draw_rectangle_filled(self.center_x, self.center_y, width, width//2, SPRITE_COLOUR)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Change so it gets removed after it gets off screen
        if self.center_x > SCREEN_WIDTH:
            self.center_x = SCREEN_WIDTH

class MyGame(arcade.Window):

    # defining constructor

    def __init__(self):


        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Our game name TBD")
        self.player = Player(200, 200, 0, 0)
<<<<<<< HEAD
        self.bullet = Bullet(200, 200, 0, 0)

        self.player_sprite = None
=======
>>>>>>> 724d9c029929b040ca7881f0869f94865b715c7c
        self.player_sprite_list = None
        self.physics_engine = None
        self.wall_list = None
        self.floor_list = [100]
        arcade.set_background_color(BACKGROUND_COLOUR)

    # defining setup function

    def setup(self):
        self.player_sprite = arcade.Sprite()
        self.player_sprite_list = arcade.SpriteList()
        self.player_sprite_list.append(self.player)
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, GRAVITY)

    # defining drawing function
    def on_draw(self):
        arcade.start_render()
<<<<<<< HEAD

        self.bullet.draw()
        self.player.draw()


    # defining update function
    def update(self, delta_time):
        self.player.update()
        self.bullet.update()

=======
        # self.wall_list.draw()
        # self.player_sprite_list.draw
        self.player.draw()

>>>>>>> 724d9c029929b040ca7881f0869f94865b715c7c
    # defining movement functions
    def on_key_press(self, key, modifiers):
        if key == arcade.key.G:
            self.bullet.change_x = BULLET_SPEED
        if key == arcade.key.A and self.bullet.center_x == self.player.center_x:
            self.player.change_x = -PLAYER_SPEED
            self.bullet.change_x = -PLAYER_SPEED
        elif key == arcade.key.A and self.bullet.center_x != self.player.center_x:
            self.player.change_x = -PLAYER_SPEED
        if key == arcade.key.D and self.bullet.center_x == self.player.center_x:
            self.player.change_x = PLAYER_SPEED
            self.bullet.change_x = PLAYER_SPEED
        elif key == arcade.key.D and self.bullet.center_x != self.player.center_x:
            self.player.change_x = PLAYER_SPEED
        if key == arcade.key.SPACE:
                self.player.change_y = JUMP_SPEED


    def on_key_release(self, key, modifiers):
        if (key == arcade.key.A or key == arcade.key.D) and self.bullet.center_x == self.player.center_x:
            self.player.change_x = 0
            self.bullet.change_x = 0
        elif (key == arcade.key.A or key == arcade.key.D) and self.bullet.center_x != self.player.center_x:
            self.player.change_x = 0
        if key == arcade.key.SPACE:
            self.player.change_y = -JUMP_SPEED

    # defining update function

    def update(self, delta_time):
        # self.physics_engine.update()
        self.player.update()

# defining main function

def main():
    window = MyGame()
    arcade.run()


main()