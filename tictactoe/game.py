### object Game and player
from Board import Board
import random

class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Human("X")
        self.player2 = None
        self.winner = None
        self.turn = 0
        self.currentPlayer = random.choice([self.player1, self.player2])
        
    def set_winner(self, player):
        if self.winner == None:
            self.winner = player
        else:
            print("!!!Multiple winner Error!!!")

    def check_winner(self):
        while self.winner == None:
            for i in range(3):
                thisRow = self.board.get_row(i)
                
                player = thisRow[0]
                if player == None:
                    continue
                if thisRow[0] == thisRow[1] and thisRow[0] == thisRow[2]:
                    self.set_winner(player)
                    break
            if self.winner != None: break
                    
            for i in range(3):
                thisCol = self.board.get_col(i)
                player = thisCol[0]
                if player == None:
                    continue
                if thisCol[0] == thisCol[1] and thisCol[0] == thisCol[2]:
                    self.set_winner(player)
                    break
            if self.winner != None: break
           
            player = self.board.get(1,1)
            if player == None:
                break
            diag1 = [self.board.get(0,0), self.board.get(2,2)]
            if diag1[0] == player and diag1[1] == player:
                self.set_winner(player)
                break
            diag2 = [self.board.get(2,0), self.board.get(0,2)]
            if diag2[0] == player and diag2[1] == player:
                self.set_winner(player)
                break
    
    def get_position(self):
        x, y = "", ""
        while x not in [1,2,3]:
            x = int(input("which coloumn? left(1), middle(2), or right(3): "))
        while y not in [1,2,3]:
            y = int(input("Which row? up(1), middle(2), or down(3): "))
        return [x, y]


    
       
class Player():
    def __init__(self, id) :
        self.id = id
    def other_player(self):
        """Given the character for a player, returns the other player."""
        assert self.id == "X" or self.id == "0", "Player must be 'X' or '0'"
        if self.id == "X": 
            self.id = "0" 
        else: 
            self.id = "X"
        
class Human(Player):
    pass
        
class Bot(Player):
    pass

class doubleGame(Game):
    def __init__(self):
        super().__init__()
        self.player2 = Human("0")
    
    def start(self):
        while self.winner is None:
            self.turn += 1
            print(self.board)
            
            print(self.currentPlayer + ", your turn")
            
            positions = self.get_position()
            while self.board.is_filled(positions[0] - 1,positions[1] - 1):
                positions = self.get_position()
            x, y = positions[0], positions[1]
            print(f"{self.currentPlayer} chose {positions[0]}, {positions[1]}")
            
            self.board.set(x - 1, y - 1, self.currentPlayer.id)
            print(self.board)
            
            self.currentPlayer.other_player()
            
            if self.turn > 3:
                self.check_winner()
            if self.turn == 9 and self.winner is None:
                break
        
        if self.winner:
            print("We have a winner, " + self.winner + "!")
        else:
            print("There is a tie")
        
class singleGame(Game):
    def __init__(self):
        super().__init__()
        self.player2 = Bot("0")
        self.human_turn = random.choice([True, False])
    
    def get_empty_spot(self):
        spots = []
        for y in range(3):
            for x in range(3):
                if self.board.get(x,y) is None:
                    spots.append([x,y])
        return spots

    def bot_move(self):
        spots = self.get_empty_spot()
        return random.choice(spots)
    
    def start(self):
        while self.winner is None:
            if not self.human_turn:
                botMove = self.bot_move()
                self.board.set(botMove[0], botMove[1], "0") # Bot.id
                print(f"Bot move to {botMove[0]+1},{botMove[1]+1}") 
                print(self.board)
            else:
                print("Your turn now!")
                
                positions = self.get_position()
                while self.board.is_filled(positions[0] - 1,positions[1] - 1):
                    positions = self.get_position()
                x, y = positions[0], positions[1]
                print(f"You chose {x}, {y}")
            
                self.board.set(x - 1, y - 1, self.currentPlayer.id)
                print(self.board) 
        
            if self.turn > 3:
                    self.check_winner()
            if self.turn == 9 and self.winner is None:
                    break
            self.human_turn = not self.human_turn
            
        if self.winner:
            print("We have a winner, " + self.winner + "!")
        else:
            print("There is a tie")