from hilo import hilo


class Director:

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.score = 0
        self.total_score = 300
        

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        player_guess = 'h'
        while self.is_playing and self.total_score > 0:
            self.get_inputs(player_guess)
            self.do_updates(player_guess)
            self.do_outputs()

    def get_inputs(self, player_guess):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        card = hilo.draw_card(self)
        drawn = hilo.draW_new(self)
        print(f'\nThe card is: {card}')
        player_guess = input('Higher or lower? [h/l] ')
        print(f'Next card was: {drawn}')
        
        

       
    def do_updates(self, player_guess):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if hilo.draw_card(self) > hilo.draW_new(self) and player_guess == 'h':
            self.score = -75
        elif hilo.draw_card(self) > hilo.draW_new(self) and player_guess == 'l':
            self.score = 100
        elif hilo.draw_card(self) < hilo.draW_new(self) and player_guess == 'h':
            self.score = 100
        elif hilo.draw_card(self) < hilo.draW_new(self) and player_guess == 'l':
            self.score = -75


    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        self.total_score += self.score
        print(f'Your score is: {self.total_score}')
        play_again = input('Play again? [y/n] ')
        if play_again == 'y':
            self.is_playing = True
        else:
            self.is_playing = False