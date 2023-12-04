class GameStats:
    # Track statistics for Alien Invasion
    def __init__(self, ai_game):
        # Initialize the stats for the game
        self.settings = ai_game.settings
        self.reset_stats()
        #Start the Alien Invasion game in an active state
        self.game_active = True

        # Store number of ships left
        self.ships_left = 4
        # Store number of aliens destoryed
        self.aliens_destroyed = 0
        # Store boolean value if shit is currently hit
        self.ship_hit = False
        # Store boolean value if the game is over
        self.game_over = False

    def reset_stats(self):
        # Initialize statistics that can change during the game
        self.ships_left = self.settings.ship_limit