import arcade
import time

# defining constants

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOUR = arcade.color.BABY_BLUE
SPRITE_COLOUR = arcade.color.ARTICHOKE
PLAYER_SPEED = 5
GAME_RUNNING = 2
GRAVITY = 5
JUMP_SPEED = 10

# state of screens
TITLE_PAGE_1 = 1
INSTRUCTION_PAGE_1 = 2
MAP_1_PAGE = 3

# tiles
TILE_SCALING = 1

# creating game class

class Player(arcade.Sprite):
    def __init__(self, center_x, center_y, change_x, change_y):
        super().__init__(None, 1, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = change_x
        self.change_y = change_y

    def draw(self):
        size = 50
        arcade.draw_rectangle_filled(self.center_x, self.center_y, size, size, SPRITE_COLOUR)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

class Enemy(Player):
    def __init__(self, center_x, center_y, change_x, change_y):
        super().__init__(center_x, center_y, change_x, change_y)

    def draw(self):
        size = 50
        arcade.draw_rectangle_filled(self.center_x, self.center_y, size, size, SPRITE_COLOUR)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

class Bullet(arcade.Sprite):
    def __init__(self):
        self.speed = 15

    def draw(self):
        width = 10
        arcade.draw_rectangle_filled(self.center_x, self.center_y, width, width//2, SPRITE_COLOUR)

    def update(self):
        self.center_x += self.change_x

        # Change so it gets removed after it gets off screen
        if self.center_x > SCREEN_WIDTH:
            self.kill

class MyGame(arcade.Window):

    # defining constructor

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Our game name TBD")

        self.player = Player(200, 90, 0, 0)
        self.enemy = Enemy(900, 90, -3, 0)

        # defining lists and engines
        self.grass_list = None
        self.physics_engine = None
        self.wall_list = None
        self.player_sprite = None
        self.player_list = None
        self.bullet_list = None
        self.bullet_sprite = None


        # setting background
        arcade.set_background_color(BACKGROUND_COLOUR)

        # screen state
        self.current_state = TITLE_PAGE_1

    def draw_title_page(self, page_number):
        arcade.set_background_color(arcade.color.WHITE)
        arcade.draw_text("TITLE PAGE", 350, 300, arcade.color.BLACK, 20)
        arcade.draw_text("PRESS I FOR INSTRUCTIONS", 275, 200, arcade.color.GRAY, 18)

    def draw_instruction_page(self, page_number):
        arcade.set_background_color(arcade.color.WHITE)
        arcade.draw_text("INSTRUCTIONS", 350, 500, arcade.color.PALATINATE_BLUE, 20)
        arcade.draw_text("PRESS ENTER TO START", 310, 300, arcade.color.ORCHID_PINK, 18)

    def draw_map_1(self, page_number):
        arcade.set_background_color(arcade.color.BABY_BLUE)
        # sprite lists
        self.grass_list = arcade.SpriteList()
        for x in range(0, SCREEN_WIDTH, 64):
            grass = arcade.Sprite("Images/GrassBlock.png")
            grass.center_x = x
            grass.center_y = 32
            self.grass_list.append(grass)
    # defining setup function

    def setup(self):
        # defining lists
        self.player_sprite_list = arcade.SpriteList
        self.wall_list = arcade.SpriteList
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # player sprite settings
        self.player__sprite = arcade.Sprite("images/character1.png", 0.1)
        self.player_sprite_list = arcade.SpriteList()
        self.player_sprite_list.append(self.player_sprite)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.grass_list, gravity_constant=GRAVITY)

    # defining drawing function
    def on_draw(self):
        arcade.start_render()


        # drawing title page
        if self.current_state == TITLE_PAGE_1:
            self.draw_title_page(1)

        # drawing instruction page
        if self.current_state == INSTRUCTION_PAGE_1:
            self.draw_instruction_page(2)

        # drawing map_1
        if self.current_state == MAP_1_PAGE:
            self.draw_map_1(3)
            # self.player_list.draw
            self.player.draw()
            self.enemy.draw()
            self.grass_list.draw()

    # defining key functions
    def on_key_press(self, key, modifiers):
        if self.current_state == MAP_1_PAGE:
            # defining movement functions
            if key == arcade.key.G:
                self.bullet_sprite = Bullet()
                self.bullet_sprite.center_x = self.player.center_x
                self.bullet_sprite.center_y = self.player.center_y
                self.bullet_sprite.change_x = self.bullet_sprite.speed
                self.bullet_list.append(self.bullet_sprite)
            if key == arcade.key.A:
                self.player.change_x = -PLAYER_SPEED
            if key == arcade.key.D:
                self.player.change_x = PLAYER_SPEED
            if key == arcade.key.SPACE:
                self.player.change_y = JUMP_SPEED

        if self.current_state == TITLE_PAGE_1:
            if key == arcade.key.I:
                self.current_state = INSTRUCTION_PAGE_1

        if self.current_state == INSTRUCTION_PAGE_1:
            if key == arcade.key.ENTER:
                self.current_state = MAP_1_PAGE

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.player.change_x = 0
        if key == arcade.key.SPACE:
            self.player.change_y = -JUMP_SPEED

    # defining update function
    def update(self, delta_time):
        self.player.update()
        self.enemy.update()
        super().update(5)

# defining main function

def main():
    window = MyGame()
    arcade.run()


main()