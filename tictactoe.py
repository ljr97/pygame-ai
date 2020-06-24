from random import randint
import numpy as np

class Game:
    def __init__(self):
        self.board_state = []
        self.initialize_game()

    
    def initialize_game(self):
        """ Crates new game board """
        self.board_state = [[' ' for i in range(3)] for j in range(3)]
        self.player_turn = 'X'
        self.level = 'Easy'

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print('{}|'.format(self.board_state[i][j]), end=" ")
            print()
        print()

    def get_board(self):
        board = []
        for i in range(3):
            for j in range(3):
                board.append(self.board_state[i][j])
        
        # Debug-
        self.print_board()
        return board

    
    def is_valid(self, x, y):
        """ Determines if a move is valid """
        if x < 0 or x > 2 or y < 0 or y > 2:
            return False
        elif self.board_state[x][y] != ' ':
            return False
        else:
            return True


    def max(self):
        """ 
        Part of MiniMax algorithm
        Try to maximize score

        Output:
        tuple(max_value, x, y)

        Possible values for max_value:
           -1 - loss
            0  - a tie
            1  - win
        """
       
        max_value = -2
        
        x = None
        y = None

        # check if someone has won the game
        result = self.is_won()


        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == ' ':
            return (0, 0, 0)

        for i in range(3):
            for j in range(3):
                if self.board_state[i][j] == ' ':
                    self.board_state[i][j] = 'O'
                    (m, min_i, min_j) = self.min()
                    # Fixing the max_value value if needed
                    if m > max_value:
                        max_value = m
                        x = i
                        y = j
                    # Setting back the field to empty
                    self.board_state[i][j] = ' '
        return (max_value, x, y)

    
    def min(self):
        """ 
        Part of MiniMax algorithm
        Try to minimize score

        Output:
        tuple(min_value, x, y)     

        Possible values for max_value:
           -1 - win
            0  - a tie
            1  - loss
         """
        min_value = 2

        x = None
        y = None

        result = self.is_won()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == ' ':
            return (0, 0, 0)

        for i in range(3):
            for j in range(3):
                if self.board_state[i][j] == ' ':
                    self.board_state[i][j] = 'X'
                    (m, max_i, max_j) = self.max()
                    if m < min_value:
                        min_value = m
                        x = i
                        y = j
                    self.board_state[i][j] = ' '

        return (min_value, x, y)


    def check_vertical(self):
        """ This function is used to check for a winner for each coulmn """
        
        tran_board = np.array(self.board_state).transpose().tolist()

        for i in range(3):
            if tran_board[i] == ['X', 'X', 'X']:
                return 'X'
            elif tran_board[i] == ['O', 'O', 'O']:
                return 'O'

        return False

    def check_horizontal(self):
        """ This function is used to check for a winner for each row """

        for i in range(3):
            if self.board_state[i] == ['X', 'X', 'X']:
                return 'X'
            elif self.board_state[i] == ['O', 'O', 'O']:
                return 'O'

        return False

    def check_diagonal(self):
        """ This function is used to check for a diagonal winner """
        if (self.board_state[0][0] != ' ' and
                self.board_state[0][0] == self.board_state[1][1] and
                self.board_state[0][0] == self.board_state[2][2]):
            return self.board_state[0][0]

    def check_reverse_diagonal(self):
        """ This function is used to check for a reversed diagonal winner """
        if (self.board_state[0][2] != ' ' and
                self.board_state[0][2] == self.board_state[1][1] and
                self.board_state[0][2] == self.board_state[2][0]):
            return self.board_state[0][2]

    def is_won(self):
        """
        This function is used to check for a winner
        Output:
            'X' - X has won
            'O' - O has won
            ' ' - a tie
            None - Game continues
        """
    
        if self.check_vertical():
            return self.check_vertical()
        if self.check_horizontal():
            return self.check_horizontal()
        if self.check_diagonal():
            return self.check_diagonal()
        if self.check_reverse_diagonal():
            return self.check_reverse_diagonal()

        # check tie
        for i in range(0, 3):
            for j in range(0, 3):
                # game continues
                if self.board_state[i][j] == ' ':
                    return None

        # tie
        return ' '

    def set_move(self, n):
        """ Sets move for 'X' player """
        self.result = self.is_won()
        
        # Initializes game if game has ended
        if self.result != None:
            self.initialize_game()
            return

        # Fit values
        x = n//3
        y = n%3

        if self.is_valid(x, y):
            self.board_state[x][y] = 'X'
            self.player_turn = 'O'
            return True
            
        return False
        

    def get_move(self):
        """ Gets move based on MiniMax algorithem/random number(0-8) """
        
        if self.player_turn == 'O':
            if self.level=='Medium':
                (m, x, y) = self.max()
            elif self.level=='Easy':
                x, y = self.random_move()
            
            # set AI move
            if self.is_valid(x, y):
                self.board_state[x][y] = 'O'
                self.player_turn = 'X'
                self.result = self.is_won()
                return True
        
        
        return False

    
    def random_move(self):
        m = randint(0, 8)
        while not self.is_valid(m//3, m%3):
            m = randint(0, 8)
        return m//3, m%3
        

    def get_result(self):
        self.result = self.is_won()
        return self.result
 
    def set_level(self, level):
        self.level = level

    def get_level(self):
        return self.level

