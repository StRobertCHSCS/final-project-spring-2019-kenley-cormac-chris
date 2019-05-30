import arcade

# defining constants

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOUR = arcade.color.WHITE
SPRITE_COLOUR = arcade.color.ARTICHOKE
PLAYER_SPEED = 5
GAME_RUNNING = 2

# state of screens
TITLE_PAGE_1 = 1
INSTRUCTION_PAGE_1 = 2
MAP_1_PAGE = 3

# tiles
TILE_SCALING = 1


# creating game class

class Player:
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


class MyGame(arcade.Window):

    # defining constructor

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Our game name TBD")

        self.player = Player(200, 200, 0, 0)

        self.player_sprite = None
        self.player_sprite_list = None
        self.grass_list = None



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
       # map_name = "Map2.tmx"
        #platform_layer_name = "Tile Layer 1"

       # my_map = arcade.read_tiled_map(map_name)
       # map_array = my_map.layers_int_data[platform_layer_name]

        # platform
        #self.wall_list = arcade.generate_sprites(my_map, platform_layer_name)

        arcade.set_background_color(arcade.color.BABY_BLUE)
        # sprite lists
        self.grass_list = arcade.SpriteList()
        #coordinate_list = [[32, 64],
                       #[96, 64],
                       #[160, 64]]
        #for coordinate in coordinate_list:
            #grass = arcade.Sprite("Images/GrassBlock.png")
            #grass.center_x = coordinate[0]
            #grass.center_y = coordinate[1]
            #self.grass_list.append(grass)
        for x in range(0, SCREEN_WIDTH, 64):
            grass = arcade.Sprite("Images/GrassBlock.png")
            grass.center_x = x
            grass.center_y = 32
            self.grass_list.append(grass)






    # defining setup function

    #def setup(self):
        # sprite lists





    # defining drawing function
    def on_draw(self):
        arcade.start_render()

        #self.player.draw()

        # drawing title page
        if self.current_state == TITLE_PAGE_1:
            self.draw_title_page(1)

        # drawing instruction page
        if self.current_state == INSTRUCTION_PAGE_1:
            self.draw_instruction_page(2)

        # drawing map_1
        if self.current_state == MAP_1_PAGE:
            self.draw_map_1(3)
            self.player.draw()
            self.grass_list.draw()



    # defining update function
    def update(self, delta_time):
        self.player.update()


    # defining key functions
    def on_key_press(self, key, modifiers):
        if self.current_state == MAP_1_PAGE:
            if key == arcade.key.A:
                self.player.change_x = -PLAYER_SPEED
            if key == arcade.key.D:
                self.player.change_x = PLAYER_SPEED

        if self.current_state == TITLE_PAGE_1:
            if key == arcade.key.I:
                self.current_state = INSTRUCTION_PAGE_1

        if self.current_state == INSTRUCTION_PAGE_1:
            if key == arcade.key.ENTER:
                self.current_state = MAP_1_PAGE


    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.player.change_x = 0
# defining main function

def main():
    window = MyGame()
    arcade.run()

main()