import arcade

# constants
SCREEN_WIDTH = 990
SCREEN_HEIGHT = 600
PLAYER_SPEED = 4
GAME_RUNNING = 2
BULLET_SPEED = 20
GRAVITY = 1.5
JUMP_SPEED = 22
SCOREBOARD_COLOUR = arcade.color.BLACK


SPRITE_COLOUR = arcade.color.ORCHID_PINK

# state of screens
TITLE_PAGE_1 = 1
INSTRUCTION_PAGE_1 = 2
MAP_1_PAGE = 3
MAP_2_PAGE = 4

# tiles
TILE_SCALING = 0.8


class Enemy(arcade.Sprite):
    def update(self):
        self.center_x -= 3
        self.center_y += self.change_y


class Bullet(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Change so it gets removed after it gets off screen
        if self.center_x > SCREEN_WIDTH:
            self.kill()


class Spike(arcade.Sprite):

    def reset_pos(self):
        self.center_x = 520
        self.center_y = 600

    def update(self):
        self.center_y -= 10
        self.center_x += self.change_x
        if self.center_y < 60:
            self.reset_pos()


class MyGame(arcade.Window):
    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Our game name TBD")
        # self.enemy = Enemy(900, 90, -3, 0)

        # holds sprites
        self.player_list = None
        self.grass_list = None
        self.bullet_list = None
        self.enemy_list = None
        self.checkpoint_list = None
        self.spike_list = None

        # physics
        self.physics_engine = None
        self.bullet_engine = None
        self.enemy_engine = None

        # player info
        self.player_sprite = None
        self.bullet_sprite = None

        # enemy info
        self.enemy_sprite = None

        # screen state
        self.current_state = TITLE_PAGE_1

    def setup(self):

        # sprite lists
        self.player_list = arcade.SpriteList()
        self.grass_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.checkpoint_list = arcade.SpriteList()
        self.spike_list = arcade.SpriteList()

        # sprite player
        self.player_sprite = arcade.Sprite("Images/BlueBlock.png", TILE_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_sprite.change_x = 0
        self.player_sprite.change_x = 0
        self.player_list.append(self.player_sprite)

        self.enemy_sprite = Enemy("Images/EnemyBlock.png", TILE_SCALING)
        self.enemy_sprite.center_x = 800
        self.enemy_sprite.center_y = 90
        self.enemy_list.append(self.enemy_sprite)

        # map_1 spike
        spike_1 = Spike("Images/Spike.png", TILE_SCALING)
        spike_1.center_x = 550
        spike_1.center_y = 550
        self.spike_list.append(spike_1)

        # physics
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.grass_list)
        self.bullet_engine = arcade.PhysicsEngineSimple(self.enemy_sprite, self.bullet_list)
        #player_hit_lit = arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)


        # map enclosure
        if self.player_sprite.center_x > SCREEN_WIDTH or self.player_sprite.center_x < 0:
            self.player_sprite.center_x = 50

        '''
        player_hp = 1
        for self.player_sprite in player_hit_lit:
            player_hp -= 1
            if player_hp == 0:
                self.player_sprite.kill()

        '''

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
        self.checkpoint_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        # self.spike_list = arcade.SpriteList()

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


    def draw_map_2(self, page_number):
        arcade.set_background_color(arcade.color.WHITE)
        # sprite list
        self.grass_list = arcade.SpriteList()
        # self.spike_list = arcade.SpriteList()
        self.checkpoint_list = arcade.SpriteList()

        coord_list = [[180, 160],
                      [425, 300],
                      [650, 400],
                      [700, 400]]
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

        # spikes
        # spike_1 = Spike("Images/Spike.png", TILE_SCALING)
        # spike_1.center_x = 550
        # spike_1.center_y = 550
        # self.spike_list.append(spike_1)

        # checkpoint
        checkpoint_1 = arcade.Sprite("Images/Checkpoint.png", TILE_SCALING)
        checkpoint_1.center_x = 900
        checkpoint_1.center_y = 200
        self.checkpoint_list.append(checkpoint_1)

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



            #arcade.draw_text("Score: " + player_hp, 50, 700, SCOREBOARD_COLOUR)


            self.draw_map_1(3)
            self.grass_list.draw()
            self.enemy_sprite.draw()
            self.bullet_list.draw()
            self.player_list.draw()
            self.checkpoint_list.draw()

        # draw map_2
        hit_checkpoint_1_list = arcade.check_for_collision_with_list(self.player_sprite, self.checkpoint_list)

        player_enemy_collision = arcade.check_for_collision_with_list(self.enemy_sprite, self.player_list)
        player_hp = 1

        bullet_enemy_collision = arcade.check_for_collision_with_list(self.enemy_sprite, self.bullet_list)
        enemy_hp = 1

        for checkpoint_1 in hit_checkpoint_1_list:
            self.current_state = MAP_2_PAGE
            self.player_sprite.center_x = 25

        for bullet in bullet_enemy_collision:
            enemy_hp -= 1
            if enemy_hp == 0:
                self.enemy_sprite.kill()

        for player in player_enemy_collision:
            player_hp -= 1
            if player_hp == 0:
                self.player_sprite.kill()

        if self.current_state == MAP_2_PAGE:
            self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.grass_list,
                                                                 gravity_constant=GRAVITY)

            self.enemy_sprite.draw()
            self.draw_map_2(4)
            self.grass_list.draw()
            self.bullet_list.draw()
            self.player_list.draw()
            self.spike_list.draw()
            self.checkpoint_list.draw()

    def on_key_press(self, key, modifiers):

        if self.current_state == MAP_1_PAGE or self.current_state == MAP_2_PAGE:

            # player and bullet movement
            if key == arcade.key.G:

                '''
                self.bullet.change_x = BULLET_SPEED
                self.bullet_list.append(self.bullet)
                self.bullet.center_x = self.player_sprite.center_x
                self.bullet.center_y = self.player_sprite.center_y
                self.bullet.update()
                '''

                self.bullet_sprite = Bullet("Images/Bullet.png", 0.5)
                self.bullet_sprite.change_x = BULLET_SPEED
                self.bullet_list.append(self.bullet_sprite)
                self.bullet_sprite.center_x = self.player_sprite.center_x
                self.bullet_sprite.center_y = self.player_sprite.center_y
                self.bullet_list.update()

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

    def update(self, delta_time):

        # update player movement
        self.player_sprite.center_x += self.player_sprite.change_x

        # update enemy
        self.enemy_sprite.update()
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



