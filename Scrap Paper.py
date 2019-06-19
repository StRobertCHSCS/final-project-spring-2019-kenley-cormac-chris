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
        arcade.set_background_color(arcade.color.SKY_BLUE)
        arcade.start_render()
        arcade.draw_rectangle_filled(495, 50, 990, 100, arcade.color.GREEN)
        arcade.draw_rectangle_filled(315, 420, 130, 130, arcade.color.GRAY)
        arcade.draw_text("BL    CK", 80, 340, arcade.color.BLACK, 130)
        arcade.draw_text("ADVENTURES", 50, 200, arcade.color.BLACK, 130)
        arcade.draw_text("PRESS I FOR INSTRUCTIONS", 700, 30, arcade.color.DARK_GRAY, 25)

def main():
    window = MyGame()
    arcade.run()

main()
