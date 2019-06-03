import arcade

# constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
GAME_RUNNING = 2
BULLET_SPEED = 20
GRAVITY = 2
JUMP_SPEED = 25

# state of screens
TITLE_PAGE_1 = 1
INSTRUCTION_PAGE_1 = 2
MAP_1_PAGE = 3

# tiles
TILE_SCALING = 1

class MyGame(arcade.Window):
    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Our game name TBD")

        # holds sprites
        self.player_list = None
        self.grass_list = None

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

        grass = arcade.Sprite("Images/GrassBlock.png")
        grass.center_x = 200
        grass.center_y = 150
        self.grass_list.append(grass)

        grass = arcade.Sprite("Images/GrassBlock.png")
        grass.center_x = 400
        grass.center_y = 200
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

        # sprite player
        self.player_sprite = arcade.Sprite("Images/BlueBlock.png")
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_sprite.change_x = 0
        self.player_sprite.change_x = 0
        self.player_list.append(self.player_sprite)

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
            self.player_list.draw()



    def on_key_press(self, key, modifiers):

        if self.current_state == MAP_1_PAGE:
            if key == arcade.key.A:
                self.player_sprite.change_x = -PLAYER_SPEED
            if key == arcade.key.D:
                self.player_sprite.change_x = PLAYER_SPEED
            if key == arcade.key.SPACE:
                self.player_sprite.change_y = JUMP_SPEED

        if self.current_state == TITLE_PAGE_1:
            if key == arcade.key.I:
                self.current_state = INSTRUCTION_PAGE_1

        if self.current_state == INSTRUCTION_PAGE_1:
            if key == arcade.key.ENTER:
                self.current_state = MAP_1_PAGE

    def on_key_release(self, key, modifiers):

        if (key == arcade.key.A or key == arcade.key.D):
            self.player_sprite.change_x = 0

        if key == arcade.key.SPACE:
            self.player_sprite.change_y = -GRAVITY
            self.player_sprite.change_y = -JUMP_SPEED

    def update(self, delta_time):

        # update player movement
        self.player_sprite.center_x += self.player_sprite.change_x

        #collide
        #hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.grass_list)
        #if len(hit_list) > 0:
            #if self.player_sprite.change_y > 0:
                #for item in hit_list:
                    #self.player_sprite.top = min(item.bottom, self.player_sprite.top)
            #elif self.player_sprite.change_y < 0:
                #for item in hit_list:
                    #self.player_sprite.bottom = max(item.top, self.player_sprite.bottom)
        #update physics
        self.physics_engine.update()



def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()




