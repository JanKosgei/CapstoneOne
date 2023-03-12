import random

from random import randint

class Snakes_Ladders:
    Snakes = {
        17: 7,
        54: 34,
        62: 19,
        64: 60,
        93: 73,
        95: 75,
        87: 36,
        98: 79,}

    Ladders = {
        1: 38,
        4: 14,
        9: 31,
        28: 84,
        21: 42,
        28: 84,
        51: 67,
        72: 91,
        80: 99,}
    
    final_position = 100


    def __init__(self, m_players, verbose = False):
        self.n_players = m_players
        self.verbose = verbose
        self.players = [0] * m_players
        self.turn = 0
        #To keep track of the winner
        self.winner = None 

#Defining the dice roll function(method)
    def dice_roll(self):
        return randint(1,6)

 #Defining the get_position function(method)   
    def get_position(self, player_n):
        prev_pos = self.players[player_n]
        new_pos = prev_pos + self.dice_roll()
        standing=' ~|~ '.join([f"From:{prev_pos},Roll:{self.dice_roll()},To:{new_pos}"])
        #To print out From and to position and the dice rolled
        print(standing)
 #In case of a winner       
        if new_pos >= self.final_position:
            self.winner = player_n
            new_pos = self.final_position
#In case of landing at the mouth of a snake          
        elif new_pos in self.Snakes:
            new_pos = self.Snakes[new_pos]
#In case of landing at the foot of a ladder         
        elif new_pos in self.Ladders:
            new_pos = self.Ladders[new_pos]
        
        self.players[player_n] = new_pos

#Defining the moving player function      
    def move_player(self):
        for player_n in range(self.n_players):
            self.get_position(player_n)
            if self.winner is not None: 
                break

#Consolidating the play function
    def play_game(self):
        while self.winner is None:
            self.turn += 1
            self.move_player()
            if self.verbose:
                self.print_turn()
#To return the result
        return f"Player {self.winner + 1} Wins!"

#To return the result   
    def print_turn(self):
        print(f"Turn {self.turn}:")
        
#To arrange players by position
        pos_of_player_n = [(pos, player_n) for player_n, pos in enumerate(self.players)]
        pos_of_player_n.sort(reverse=True)
        
#To  print players based on position
        player_pos_str = ' ~|~ '.join([f"({player_n + 1}) {pos}" for pos, player_n in pos_of_player_n])
        print(player_pos_str)


game = Snakes_Ladders(m_players = 2,verbose=True)

game.play_game()