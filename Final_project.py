import arcade

# constants
SCREEN_WIDTH = 990
SCREEN_HEIGHT = 600
PLAYER_SPEED = 10
GAME_RUNNING = 2
BULLET_SPEED = 20
GRAVITY = 1.5
JUMP_SPEED = 22
SCOREBOARD_COLOUR = arcade.color.BLACK
BACKGROUND_COLOUR = arcade.color.BABY_BLUE
GAME_OVER = False
HEALTH_SCALING = 0.05
# state of screens
TITLE_PAGE_1 = 1
INSTRUCTION_PAGE_1 = 2
STORY_PAGE_1 = 3
MAP_1_PAGE = 4
MAP_2_PAGE = 5


# tiles
TILE_SCALING = 0.8


class Enemy(arcade.Sprite):
    def update(self):
        self.center_x = 600
        self.center_x = 650
        self.center_y += self.change_y
        self.update()

class Bullet(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Change so it gets removed after it gets off screen
        if self.center_x > SCREEN_WIDTH:
            self.kill()


class Spike(arcade.Sprite):

    def reset_pos(self):
        self.center_x = self.center_x
        self.center_y = 600

    def update(self):
        self.center_y -= 9
        self.center_x += self.change_x
        if self.center_y < 60:
            self.reset_pos()


class MyGame(arcade.Window):
    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Block adventures")

        # holds sprites
        self.player_list = None
        self.grass_list = None
        self.bullet_list = None
        self.enemy_list = None
        self.checkpoint_list = None
        self.health_pickup_list = None
        self.spike_list = None

        # physics
        self.physics_engine = None
        self.bullet_engine = None
        self.enemy_engine = None

        # set sprites
        self.player_sprite = None
        self.bullet_sprite = None
        self.health_block = None

        # enemy info
        self.enemy_sprite = None

        # screen state
        self.current_state = TITLE_PAGE_1

    def setup(self):

        # sprite lists
        self.player_list = arcade.SpriteList()
        self.grass_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.health_pickup_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.checkpoint_list = arcade.SpriteList()
        self.spike_list = arcade.SpriteList()

        # sprite player
        self.player_sprite = arcade.Sprite("Images/BlueBlock.png", TILE_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_sprite.change_x = 0
        self.player_sprite.change_x = 0
        self.player_sprite.health = 100
        self.player_sprite.score = 0
        self.player_list.append(self.player_sprite)

        self.enemy_sprite = Enemy("Images/EnemyBlock.png", TILE_SCALING)
        self.enemy_sprite.center_x = SCREEN_WIDTH
        self.enemy_sprite.center_y = 90
        self.enemy_sprite.health = 1

        health_coord_list = [[550, 192]]

        for health in health_coord_list:
            self.health_block = arcade.Sprite("Images/heart.png", HEALTH_SCALING)
            self.health_block.center_x = health[0]
            self.health_block.center_y = health [1]
            self.health_pickup_list.append(self.health_block)


        # physics
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.grass_list)
        #self.bullet_engine = arcade.PhysicsEngineSimple(self.enemy_sprite, self.bullet_list)
        #player_hit_lit = arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)


        # map enclosure
        if self.player_sprite.center_x > SCREEN_WIDTH or self.player_sprite.center_x < 0:
            self.player_sprite.center_x = 50

    def draw_title_page(self, page_number):
        arcade.set_background_color(arcade.color.SKY_BLUE)
        arcade.draw_rectangle_filled(495, 50, 990, 100, arcade.color.GREEN)
        block_image = arcade.load_texture("Images/BlueBlock.png")
        scale = 1.7
        arcade.draw_texture_rectangle(315, 410, scale * block_image.width, scale * block_image.height, block_image, 0)
        arcade.draw_text("BL    CK", 80, 340, arcade.color.BLACK, 130)
        arcade.draw_text("ADVENTURES", 50, 200, arcade.color.BLACK, 130)
        arcade.draw_text("PRESS I FOR INSTRUCTIONS", 630, 30, arcade.color.DARK_GRAY, 25)

    def draw_instruction_page(self, page_number):
        arcade.set_background_color(arcade.color.WHEAT)
        arcade.draw_text("INSTRUCTIONS", 30, 515, arcade.color.BLACK, 60)
        arcade.draw_text("YOU ARE A BLOCK... "
                         "\nON AN ADVENTURE..."
                         "\nIT'S IN THE TITLE. "
                         "\nIT'S PRETTY STRAIGHT-"
                         "\nFORWARD. USE W, A, D"
                         "\nTO MOVE AROUND"
                         "\nUSE G TO GURK ENEMIES."
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

    def draw_story_page(self, page_number):
        arcade.set_background_color(arcade.color.SKY_BLUE)
        arcade.draw_rectangle_filled(495, 50, 990, 100, arcade.color.GREEN)
        arcade.draw_text('"HEY THIS IS THE VERY INTERESTING BACK STORY '
                         '\nBEHIND BLOCK ADVENTURE, THIS IS NOT IMPORTANT '
                         '\nAT ALL TO YOUR GAMEPLAY SO YOU CAN SKIP THIS '
                         '\nIF YOU WANT BUT HERE IS THE SAD STORY OF BLUE '
                         '\nBLOCK. BLUE BLOCK WAS A CRACKHEAD. ONE DAY HIS '
                         '\nMOM TOLD HIM TO GET GROCERIES BUT HE WAS ALREADY '
                         '\nINTOXICATED OUT OF HIS MIND. AFTER ARGUING WITH '
                         '\nWHO HE THOUGHT WAS HIS MOM FOR A WHILE (IT WAS '
                         '\nHIS PET HUMAN) HE GOES OUT TO BUY GROCERIES. '
                         '\nUNLUCKILY FOR HIM THERE WAS A WHOLE NEW ADVENTURE '
                         '\nWAITING OUTSIDE FOR HIM. NOT LIKE LORD OF THE RINGS'
                         '\nBUT NONETHELESS AN ADVENTURE WAY MORE ENTERTAINING '
                         '\nTHAN HIS NORMAL INSIDE LIFE."', 150, 250, arcade.color.BLACK, 25)
        arcade.draw_text("PRESS G TO START GAME", 630, 30, arcade.color.DARK_GRAY, 25)
        block_image = arcade.load_texture("Images/RedBlock.png")
        scale = 1.7
        arcade.draw_texture_rectangle(100, 155, scale * block_image.width, scale * block_image.height, block_image, 0)

    def draw_gameover_page(self, page_number):
        arcade.set_background_color(arcade.color.BLACK)

    def draw_map_1(self, page_number):
        self.enemy_sprite.center_x -= 3
        arcade.set_background_color(BACKGROUND_COLOUR)

        # sprite lists
        self.grass_list = arcade.SpriteList()
        self.checkpoint_list = arcade.SpriteList()

        # PUT IN COORD LIST LATER
        coord_list = [[180, 160],
                      [380, 300],
                      [650, 400],
                      [700, 400]]
        for coordinate in coord_list:
            grass = arcade.Sprite("Images/GrassBlock.png", TILE_SCALING)
            grass.center_x = coordinate[0]
            grass.center_y = coordinate[1]
            self.grass_list.append(grass)

        # platform
        for x in range(0, SCREEN_WIDTH, 64):
            grass = arcade.Sprite("Images/GrassBlock.png")
            grass.center_x = x
            grass.center_y = 32
            self.grass_list.append(grass)

        # map_1 checkpoint
        checkpoint_1 = arcade.Sprite("Images/Checkpoint.png", TILE_SCALING)
        checkpoint_1.center_x = 700
        checkpoint_1.center_y = 450
        self.checkpoint_list.append(checkpoint_1)
        self.grass_list.draw()
        self.health_pickup_list.draw()
        self.enemy_sprite.draw()
        self.enemy_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()
        self.checkpoint_list.draw()


    def draw_map_2(self, page_number):
        self.enemy_sprite.center_x -= 3
        arcade.set_background_color(BACKGROUND_COLOUR)
        # sprite list
        self.grass_list = arcade.SpriteList()
        self.checkpoint_list = arcade.SpriteList()

        coord_list = [[180, 160],[425, 300],[650, 400],[700, 400],[700, 400],[900, 250]]

        for coordinate in coord_list:
            grass = arcade.Sprite("Images/GrassBlock.png", TILE_SCALING)
            grass.center_x = coordinate[0]
            grass.center_y = coordinate[1]
            self.grass_list.append(grass)

        for x in range(0, SCREEN_WIDTH, 64):
            grass = arcade.Sprite("Images/GrassBlock.png")
            grass.center_x = x
            grass.center_y = 32
            self.grass_list.append(grass)

        # checkpoint
        checkpoint_2 = arcade.Sprite("Images/Checkpoint.png", TILE_SCALING)
        checkpoint_2.center_x = 900
        checkpoint_2.center_y = 300
        self.checkpoint_list.append(checkpoint_2)

        self.enemy_sprite.draw()

    def setup2(self):

        self.enemy_sprite = Enemy("Images/EnemyBlock.png", TILE_SCALING)
        self.enemy_sprite.center_x = SCREEN_WIDTH
        self.enemy_sprite.center_y = 90
        self.enemy_sprite.health = 100
        self.spike_list = arcade.SpriteList()
        # map_2 spike
        spike_1 = Spike("Images/Spike.png", TILE_SCALING)
        spike_1.center_x = 550
        spike_1.center_y = 550
        self.spike_list.append(spike_1)

        spike_1 = Spike("Images/Spike.png", TILE_SCALING)
        spike_1.center_x = 300
        spike_1.center_y = 550
        self.spike_list.append(spike_1)

        # map_2 enemy
    def on_draw(self):
        arcade.start_render()
        # drawing title page
        if self.current_state == TITLE_PAGE_1:
            self.draw_title_page(1)

        # drawing instruction page
        if self.current_state == INSTRUCTION_PAGE_1:
            self.draw_instruction_page(2)

        # drawing story page
        if self.current_state == STORY_PAGE_1:
            self.draw_story_page(3)

        hit_checkpoint_1_list = arcade.check_for_collision_with_list(self.player_sprite, self.checkpoint_list)

        player_enemy_collision = arcade.check_for_collision_with_list(self.enemy_sprite, self.player_list)

        spike_player_collision = arcade.check_for_collision_with_list(self.player_sprite, self.spike_list)

        bullet_enemy_collision = arcade.check_for_collision_with_list(self.enemy_sprite, self.bullet_list)

        health_player_collision = arcade.check_for_collision_with_list(self.player_sprite, self.health_pickup_list)

        for spike in spike_player_collision:
            self.player_sprite.health -= 5
        for pickup in health_player_collision:
            self.player_sprite.health += 50
            self.health_block.kill()
        for checkpoint_1 in hit_checkpoint_1_list:
            self.current_state = MAP_2_PAGE
            self.player_sprite.center_x = 25
            self.setup2()
        for enemy in bullet_enemy_collision:
            self.enemy_sprite.health -= 5
            if self.enemy_sprite.health == 0:
                self.player_sprite.score += 1
                self.enemy_sprite.center_x = -50
        for player in player_enemy_collision:
            self.player_sprite.health -= 5

        # drawing map_1
        if self.current_state == MAP_1_PAGE:
            self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.grass_list,
                                                                 gravity_constant=GRAVITY)

<<<<<<< HEAD
            self.draw_map_1(3)
            arcade.draw_text("Health: " + str(self.player_sprite.health), 50, 500, SCOREBOARD_COLOUR)
=======
            self.draw_map_1(4)
            arcade.draw_text("Lives: " + str(self.player_sprite.health), 50, 500, SCOREBOARD_COLOUR)
>>>>>>> Chris-dev
            arcade.draw_text("Score: " + str(self.player_sprite.score), 50, 550, SCOREBOARD_COLOUR)


        # draw map 2
        hit_checkpoint_1_list = arcade.check_for_collision_with_list(self.player_sprite, self.checkpoint_list)
        for checkpoint_1 in hit_checkpoint_1_list:
            self.current_state = MAP_2_PAGE
            self.player_sprite.center_x = 25
            self.setup2()
        if self.current_state == MAP_2_PAGE:
            self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.grass_list,
                                                                 gravity_constant=GRAVITY)
            arcade.draw_text("Lives: " + str(self.player_sprite.health), 50, 500, SCOREBOARD_COLOUR)
            arcade.draw_text("Score: " + str(self.player_sprite.score), 50, 550, SCOREBOARD_COLOUR)
            #self.enemy_sprite.draw()
            self.draw_map_2(5)
            self.grass_list.draw()
            self.bullet_list.draw()
            self.player_list.draw()
            self.spike_list.draw()
            self.checkpoint_list.draw()

        if self.current_state == GAME_OVER:
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text("YOU LOSE!", (SCREEN_WIDTH/2 - 100), (SCREEN_HEIGHT/2), arcade.color.WHITE, 100, 100)

        if self.player_sprite.health <= 0:
            self.player_sprite.kill()
            self.current_state = GAME_OVER

    def on_key_press(self, key, modifiers):
        if self.current_state == MAP_1_PAGE or self.current_state == MAP_2_PAGE:

            # player and bullet movement

            if key == arcade.key.G:
                self.bullet_sprite = Bullet("Images/Bullet.png", 0.5)
                self.bullet_sprite.change_x = BULLET_SPEED
                self.bullet_list.append(self.bullet_sprite)
                self.bullet_sprite.center_x = self.player_sprite.center_x
                self.bullet_sprite.center_y = self.player_sprite.center_y
                arcade.load_sound("Sounds/laser.wav")
                arcade.play_sound("Sounds/laser.wav")

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
                self.current_state = STORY_PAGE_1

        if self.current_state == STORY_PAGE_1:
            if key == arcade.key.G:
                self.current_state = MAP_1_PAGE

    def on_key_release(self, key, modifiers):

        if key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0

        if key == arcade.key.W:
            self.player_sprite.change_y = 0

    def update(self, delta_time):

        # update player movement

        # update enemy
        # update sprite lists


        # update sprite lists
        self.bullet_list.update()
        self.spike_list.update()

        # update checkpoints
        self.checkpoint_list.update()

        # update physics
        self.physics_engine.update()

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()