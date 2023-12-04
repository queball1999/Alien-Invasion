import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    #Overall class to manage game assets and behavior
    def __init__(self):
        #Initialize the game, and create game resources
        pygame.init()
        self.settings = Settings()
        # Tell pygame to determine the size of the screen and set the screen width and height based on the players screen size
        self.screen = pygame.display.set_mode ((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption ("Sharons Alien Invasion")
        # Set the background color - colors are RBG colors: amix of red, green, and blue. Each color range is 0 to 255
        self.bg_color = (200, 230, 230)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        # Add in the alien
        self.aliens = pygame.sprite.Group()
        self._create_fleet()


    def run_game(self):
        #Start the main loop for the game
        while True:
            # call a method to check to see if any keyboard events have occurred
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()


    def _check_events(self):
        #Respond to keypresses and mouse events.
        # Did the player quit the game?
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                sys.exit()
            # Did the player press the right or left arrow key?
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # Did the player stop holding down the arrow key?
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        # Is the key the right arrow or is it the left arrow
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # Did the player hit the Q key to quite the game?
        elif event.key == pygame.K_q:
            sys.exit()
        # Did the player hit the space bar to shoot a bullet?
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event):
        # Did the player stop holding down the arrow keys?
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key ==pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):
        #Create a new bullet and add it to the bullets group
        #Limited the number of bullets a player can have at a time by adding a constant to the settings file
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        #Update positions of the bullets and get rid of old bullets.
        self.bullets.update()
        # Get rid of bullets that have disappeared off the screen because they are still there in the game and take up memory and execution time
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)
            # Determine how many bullets still exist in the game to verify they are being deleted
            # print(len(self.bullets))
            # Add a method to create a fleet of Aliens

    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Make a single alien.
        aliens = Alien(self)
        alien_width = aliens.rect.width
        # Determine how much space you have on the screen for aliens
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # Create the first row of aliens
        for alien_number in range (number_aliens_x):
            # Create an alien and place it in the row.
            aliens = Alien(self)
            aliens.x = alien_width + 2 * alien_width * alien_number
            aliens.rect.x = aliens.x
            self.aliens.add(aliens)


    def _update_screen(self):
        #Update images on the screen, and flip to the new screen.
        # Redraw the screen each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Draw bullets on the screen
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #Draw the alien
        self.aliens.draw(self.screen)
        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
    quit()