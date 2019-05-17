import arcade

# defining constants

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOUR = arcade.color.WHITE

# creating game class

class MyGame(arcade.Window):

    # defining constructor

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Our game name TBD")

        arcade.set_background_color(BACKGROUND_COLOUR)


    # defining drawing function

    def on_draw(self):
        arcade.start_render()


    # defining update function



# defining main function

def main():
    window = MyGame()
    arcade.run()

main()