import arcade

# --- Constants ---
SCREEN_WIDTH = 990
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Game")

    def on_draw(self):
        arcade.set_background_color(arcade.color.WHEAT)
        arcade.start_render()
        arcade.draw_text("INSTRUCTIONS", 30, 520, arcade.color.PALATINATE_BLUE, 50)
        arcade.draw_text("YOU ARE A BLOCK... "
                         "\nON AN ADVENTURE..."
                         "\nIT'S IN THE TITLE. "
                         "\nIT'S PRETTY STRAIGHT-"
                         "\nFORWARD. USE W, A, D"
                         "\nTO MOVE AROUND"
                         "\nUSE G TO GURK ENEMIES"
                         "\nSEE IF YOU CAN MAKE "
                         "\nIT TO THE END!", 30, 150, arcade.color.BLACK, 35)
        block_image = arcade.load_texture("Images/W KEY.png")
        scale = 0.2
        arcade.draw_texture_rectangle(625, 420, scale * block_image.width, scale * block_image.height, block_image, 0)
        arcade.draw_text("- JUMP", 700, 395, arcade.color.BLACK, 40)
        block_image = arcade.load_texture("Images/A KEY.png")
        scale = 0.2
        arcade.draw_texture_rectangle(575, 302.5, scale * block_image.width, scale * block_image.height, block_image, 0)
        block_image = arcade.load_texture("Images/D KEY.png")
        scale = 0.2
        arcade.draw_texture_rectangle(675, 302.5, scale * block_image.width, scale * block_image.height, block_image, 0)
        arcade.draw_text("- SLIDE", 750, 277.5, arcade.color.BLACK, 40)
        block_image = arcade.load_texture("Images/G KEY.png")
        scale = 0.2
        arcade.draw_texture_rectangle(625, 185, scale * block_image.width, scale * block_image.height, block_image, 0)
        arcade.draw_text("- SHOOT", 700, 160, arcade.color.BLACK, 40)
        arcade.draw_text("PRESS ENTER TO START", 660, 30, arcade.color.GRAY, 25)



def main():
    window = MyGame()
    arcade.run()

main()
