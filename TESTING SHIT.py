import arcade

# constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 4
GAME_RUNNING = 2
BULLET_SPEED = 20
GRAVITY = 1.5
JUMP_SPEED = 22


SPRITE_COLOUR = arcade.color.ORCHID_PINK

# state of screens
TITLE_PAGE_1 = 1
INSTRUCTION_PAGE_1 = 2
MAP_1_PAGE = 3

# tiles
TILE_SCALING = 0.8

class Bullet(arcade.Sprite):

    #def __init__(self, center_x, center_y, change_x, change_y):
        #self.center_x = center_x
        #self.center_y = center_y
        #self.change_x = change_x
        #self.change_y = change_y
        # self.bullet_sprite_list = arcade.SpriteList()

    def draw(self):
        width = 10
        arcade.draw_rectangle_filled(self.center_x, self.center_y, width, width//2, SPRITE_COLOUR)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Change so it gets removed after it gets off screen
        if self.center_x > SCREEN_WIDTH:
            self.kill()


class MyGame(arcade.Window):
    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Our game name TBD")

        # holds sprites
        self.player_list = None
        self.grass_list = None
        self.bullet_list = None

        # physics
        self.physics_engine = None

        # player info
        self.player_sprite = None

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

        # sprite lists
        self.grass_list = arcade.SpriteList()
        # PUT IN COORD LIST LATER
        grass = arcade.Sprite("Images/GrassBlock.png", TILE_SCALING)
        grass.center_x = 180
        grass.center_y = 160
        self.grass_list.append(grass)

        grass = arcade.Sprite("Images/GrassBlock.png", TILE_SCALING)
        grass.center_x = 380
        grass.center_y = 300
        self.grass_list.append(grass)

        grass = arcade.Sprite("Images/GrassBlock.png", TILE_SCALING)
        grass.center_x = 650
        grass.center_y = 400
        self.grass_list.append(grass)

        grass = arcade.Sprite("Images/GrassBlock.png", TILE_SCALING)
        grass.center_x = 700
        grass.center_y = 400
        self.grass_list.append(grass)



        # platform
        for x in range(0, SCREEN_WIDTH, 64):
            grass = arcade.Sprite("Images/GrassBlock.png")
            grass.center_x = x
            grass.center_y = 32
            self.grass_list.append(grass)


    def setup(self):

        # sprite lists
        self.player_list = arcade.SpriteList()
        self.grass_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # sprite player
        self.player_sprite = arcade.Sprite("Images/BlueBlock.png", TILE_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_sprite.change_x = 0
        self.player_sprite.change_x = 0
        self.player_list.append(self.player_sprite)

        self.bullet = Bullet("Images/Bullet.png", 0.5)
        self.bullet.center_x = 100
        self.bullet.center_y = 100

        # physics
        #self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.grass_list,
                                                             #gravity_constant=GRAVITY)



        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.grass_list)

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
            self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.grass_list,
                                                                 gravity_constant=GRAVITY)
            self.draw_map_1(3)
            self.grass_list.draw()
            self.bullet_list.draw()
            self.player_list.draw()




    def on_key_press(self, key, modifiers):

        if self.current_state == MAP_1_PAGE:

            # player and bullet movement
            # bullet movement
            if key == arcade.key.G:
                #bullet = Bullet("Images/Bullet.png", 0.5)
                #bullet.center_x = 100
                #bullet.center_y = 100
                self.bullet.change_x = BULLET_SPEED
                self.bullet_list.append(self.bullet)
                self.bullet_list.change_x = BULLET_SPEED
                self.bullet.center_x = self.player_sprite.center_x
                self.bullet.center_y = self.player_sprite.center_y
                self.bullet.update()
            if key == arcade.key.A:
                self.player_sprite.change_x = -PLAYER_SPEED
            if key == arcade.key.D:
                self.player_sprite.change_x = PLAYER_SPEED
            if key == arcade.key.W:
                if self.physics_engine.can_jump():
                    self.player_sprite.change_y = JUMP_SPEED

        # map states
        if self.current_state == TITLE_PAGE_1:
            if key == arcade.key.I:
                self.current_state = INSTRUCTION_PAGE_1

        if self.current_state == INSTRUCTION_PAGE_1:
            if key == arcade.key.ENTER:
                self.current_state = MAP_1_PAGE

    def on_key_release(self, key, modifiers):

        if key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0

        if key == arcade.key.W:
            self.player_sprite.change_y = 0
            #self.player_sprite.change_y = -JUMP_SPEED

    def update(self, delta_time):

        # update player movement
        self.player_sprite.center_x += self.player_sprite.change_x


        # update sprite lists
        self.bullet_list.update()

        #update physics
        self.physics_engine.update()



def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()




