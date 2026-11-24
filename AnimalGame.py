# Author: Dylan Bishop
# GitHub username: dylanb922
# Date: 12/3/25
# Description: An animal-themed abstract board game built using OOP to define several classes to help the game run.
#              Subclasses of the Piece class contain logic to make sure the rules of those pieces are enforced.
#              The AnimalGame class handles the overarching game, including initializing the board, making moves,
#              turn order, and correctly determining a win.

class Piece:
    """
    A base for each of the specific piece types to work off, containing logic for all of them to use.
    Logic includes color of pieces, piece position, and a template for move verification.
    Each of the piece types will become subclasses of this class.
    It will work with the AnimalGame class to ensure a move is possible, through indirect communication via
    the piece's subclasses.
    """

    def __init__(self, color, pos):
        """
        Initializes a non-specific game piece

        color: "AMETHYST" or "TANGERINE" for each team
        pos: the starting coordinate of the piece
        """
        self._color = color # takes "TANGERINE" or "AMETHYST"
        self._pos = pos

    def get_color(self):
        """Returns the color of the piece"""
        return self._color

    def get_position(self):
        """Returns the position of the piece"""
        return self._pos

    def set_position(self, new_pos):
        """
        Updates the piece's position

        new_pos: the desired new position of the piece
        """
        self._pos = new_pos

    @staticmethod
    def pos_to_coord(position):
        """Converts the algebraic notation to coordinates to easier handle move verification"""
        col = ord(position[0]) - ord('a') # converts the first character (letter) into an integer, ord uses Unicode
        row = int(position[1]) - 1 # converts the second character (number) into an integer
        return row, col

    def is_path_clear(self, start_pos, end_pos, game_board):
        """Helper function to check if the path is clear for sliding pieces"""
        start_row, start_col = self.pos_to_coord(start_pos)
        end_row, end_col = self.pos_to_coord(end_pos)

        row_moves = end_row - start_row
        col_moves = end_col - start_col

        # checks the direction moved (0 means no move, + means downward, - means upward)
        step_row = 0 if row_moves == 0 else (1 if row_moves > 0 else -1)
        step_col = 0 if col_moves == 0 else (1 if col_moves > 0 else -1)

        current_row, current_col = start_row + step_row, start_col + step_col
        while (current_row, current_col) != (end_row, end_col):
            # converts the coordinate back to algebraic notation so we can check the game board (just reverses)
            pos = chr(current_col + ord('a')) + str(current_row + 1)
            if game_board[pos] is not None:  # there's something in the space
                return False
            current_row += step_row
            current_col += step_col

        return True

class Okapi(Piece):
    """
    A subclass (inherited from Piece) for a game piece that can slide up to 4 spaces orthogonally or 1 space diagonally.
    Contains logic to verify if the piece can perform the move asked of it, communicating with AnimalGame class.
    """

    def __init__(self, color, pos):
        """
        Initializes an Okapi piece

        color: "amethyst" or "tangerine" for each team
        pos: the starting coordinate of the piece
        """
        super().__init__(color, pos)
        self._direction = "orthogonal"
        self._distance = 4
        self._locomotion = "sliding"

    def verify_move(self, start_pos, end_pos, game_board):
        """
        Checks if the attempted move is legal according to the Okapi piece rules:
        Up to 4 spaces orthogonal (or 1 space diagonal), sliding

        start_pos: the current position of the piece
        end_pos: the target position of the piece
        game_board: the dictionary of the current game_board

        Returns: True if the move is legal
        Otherwise, False
        """
        start_row, start_col = self.pos_to_coord(start_pos)
        end_row, end_col = self.pos_to_coord(end_pos)

        row_moves = end_row - start_row
        col_moves = end_col - start_col

        # absolute value is helpful for checking diagonal moves
        abs_row_moves = abs(row_moves)
        abs_col_moves = abs(col_moves)

        # checks if a diagonal move of 1 was made
        if abs_row_moves == 1 and abs_col_moves == 1:
            return True

        # check if a valid orthogonal move has been made
        if (row_moves == 0 and 1 <= abs_col_moves <= self._distance) or (
                col_moves == 0 and 1 <= abs_row_moves <= self._distance):
            return self.is_path_clear(start_pos, end_pos, game_board)

        # if every one of the previous tests fail,
        return False


# noinspection PyUnusedLocal
class Wombat(Piece):
    """
    A subclass (inherited from Piece) for a game piece that can jump only 1 space orthogonally or diagonally.
    Contains logic to verify if the piece can perform the move asked of it, communicating with AnimalGame class.
    """

    def __init__(self, color, pos):
        """
        Initializes a Wombat piece

        color: "amethyst" or "tangerine" for each team
        pos: the starting coordinate of the piece
        """
        super().__init__(color, pos)
        self._direction = "orthogonal"
        self._distance = 1
        self._locomotion = "jumping"

    def verify_move(self, start_pos, end_pos, game_board):
        """
        Checks if the attempted move is legal according to the Wombat piece rules:
        1 space orthogonal (or 1 space diagonal), jumping

        start_pos: the current position of the piece
        end_pos: the target position of the piece
        game_board: the dictionary of the current game_board

        Returns: True if the move is legal
        Otherwise, False
        """
        start_row, start_col = self.pos_to_coord(start_pos)
        end_row, end_col = self.pos_to_coord(end_pos)

        row_moves = end_row - start_row
        col_moves = end_col - start_col

        # absolute value is helpful for checking diagonal moves
        abs_row_moves = abs(row_moves)
        abs_col_moves = abs(col_moves)

        # checks if a diagonal move of 1 was made
        if abs_row_moves == 1 and abs_col_moves == 1:
            return True

        # checks if an orthogonal move of 1 was made
        if (row_moves == 0 and abs_col_moves == self._distance) or (col_moves == 0 and abs_row_moves == self._distance):
            return True

        # if move doesn't fit either of those categories,
        return False


# noinspection PyUnusedLocal
class Kinkajou(Piece):
    """
    A subclass (inherited from Piece) for a game piece that can jump 3 spaces diagonally or 1 space orthogonally.
    Contains logic to verify if the piece can perform the move asked of it, communicating with AnimalGame class.
    """

    def __init__(self, color, pos):
        """
        Initializes a Kinkajou piece

        color: "amethyst" or "tangerine" for each team
        pos: the starting coordinate of the piece
        """
        super().__init__(color, pos)
        self._direction = "diagonal"
        self._distance = 3
        self._locomotion = "jumping"

    def verify_move(self, start_pos, end_pos, game_board):
        """
        Checks if the attempted move is legal according to the Kinkajou piece rules:
        Exactly 3 spaces diagonal (or 1 space orthogonal), jumping

        start_pos: the current position of the piece
        end_pos: the target position of the piece
        game_board: the dictionary of the current game_board

        Returns: True if the move is legal
        Otherwise, False
        """
        start_row, start_col = self.pos_to_coord(start_pos)
        end_row, end_col = self.pos_to_coord(end_pos)

        row_moves = end_row - start_row
        col_moves = end_col - start_col

        # absolute value is helpful for checking diagonal moves
        abs_row_moves = abs(row_moves)
        abs_col_moves = abs(col_moves)

        # checks if a diagonal move of 3 was made
        if abs_row_moves == self._distance and abs_col_moves == self._distance:
            return True

        # checks if an orthogonal move of 1 was made
        if (row_moves == 0 and abs_col_moves == 1) or (col_moves == 0 and abs_row_moves == 1):
            return True

        # if move doesn't fit either of those categories,
        return False

class Cuttlefish(Piece):
    """
    A subclass (inherited from Piece) for a game piece that can slide up to 2 spaces diagonally or 1 space orthogonally.
    Loss of the game is tied to this game piece.
    Contains logic to verify if the piece can perform the move asked of it, communicating with AnimalGame class.
    """

    def __init__(self, color, pos):
        """
        Initializes a Cuttlefish piece

        color: "amethyst" or "tangerine" for each team
        pos: the starting coordinate of the piece
        """
        super().__init__(color, pos)
        self._direction = "diagonal"
        self._distance = 2
        self._locomotion = "sliding"

    def verify_move(self, start_pos, end_pos, game_board):
        """
        Checks if the attempted move is legal according to the Cuttlefish piece rules:
        Up to 2 spaces diagonal (or 1 space orthogonal), sliding

        start_pos: the current position of the piece
        end_pos: the target position of the piece
        game_board: the dictionary of the current game_board

        Returns: True if the move is legal
        Otherwise, False
        """
        start_row, start_col = self.pos_to_coord(start_pos)
        end_row, end_col = self.pos_to_coord(end_pos)

        row_moves = end_row - start_row
        col_moves = end_col - start_col

        # absolute value is helpful for checking diagonal moves
        abs_row_moves = abs(row_moves)
        abs_col_moves = abs(col_moves)

        # checks if an orthogonal move of 1 was made
        if (row_moves == 0 and abs_col_moves == 1) or (col_moves == 0 and abs_row_moves == 1):
            return True

        # check if a valid diagonal move has been made
        if abs_row_moves == abs_col_moves and 1 <= abs_row_moves <= self._distance:
            return self.is_path_clear(start_pos, end_pos, game_board)

        # if every one of the previous tests fail,
        return False

class AnimalGame:
    """
    The primary class that contains the logic to track the entire game state. Also contains logic to begin the game,
    perform player moves, and detect if the game has been won
    Interacts with the other piece classes/subclasses to verify if moves can be legally made.
    """

    def __init__(self):
        """Initializes the game"""
        self._board = {} # only defined for unit tests
        self._player_turn = "TANGERINE"
        self._game_state = "UNFINISHED"
        self.board_builder()

    def get_game_state(self):
        """Returns the current state of the game, either UNFINISHED, TANGERINE_WON, or AMETHYST_WON"""
        return self._game_state

    def make_move(self, start_pos, end_pos):
        """
        Attempts a move from the piece's current position to a new position, only if it is the player's turn
        Move is only made if it is verified through the piece's verify_move method

        start_pos: The piece's current position coordinate on the board
        end_pos: The piece's targeted coordinate position
        """
        moving_piece = self._board[start_pos]
        target_piece = self._board[end_pos]

        # checks if the game has been won already
        if self.get_game_state() != "UNFINISHED":
            return False

        # checks if the position even has a piece
        if moving_piece is None:
            return False

        # checks if it is their turn
        if moving_piece.get_color() != self._player_turn:
            return False

        # checks if target position contains a friendly piece
        if target_piece is not None and target_piece.get_color() == moving_piece.get_color():
            return False

        # checks that verify_move returns correctly
        if not moving_piece.verify_move(start_pos, end_pos, self._board):
            return False

        # checks if a piece is being captured
        if target_piece is not None:
            # checks if the piece being captured is a Cuttlefish
            if isinstance(target_piece, Cuttlefish):
                if target_piece.get_color() == "TANGERINE":
                    self._game_state = "AMETHYST_WON"
                else:
                    self._game_state = "TANGERINE_WON"

        # performs the move
        self._board[end_pos] = moving_piece
        self._board[start_pos] = None
        moving_piece.set_position(end_pos)

        # switches turns if that game hasn't ended yet
        if self._game_state == "UNFINISHED":
            self.switch_turn()

        return True

    def switch_turn(self):
        """Called at the end of a turn. Switches from one player's turn to another."""
        if self._player_turn == "TANGERINE":
            self._player_turn = "AMETHYST"
        else:
            self._player_turn = "TANGERINE"

    def check_turn(self):
        """Returns the player whose turn it is."""
        return self._player_turn

    def board_builder(self):
        """Creates the 7x7 game board dictionary and sets the beginning positions."""
        columns = ["a","b","c","d","e","f","g"]
        rows = ["1","2","3","4","5","6","7"]

        for row in rows:
            for column in columns:
                space = column + row
                self._board[space] = None

        order = [Okapi, Wombat, Kinkajou, Cuttlefish, Kinkajou, Wombat, Okapi]

        # places the Tangerine pieces using enumerate (new function I learned)
        # enumerate allows you to iterate through a list and assign each value an index.
        # index can be used to find the associated column
        # then we can assign each value in the "order" list as a PieceType and use that to initialize the pieces
        for index, PieceType in enumerate(order):
            col = columns[index]
            position = col + "1"
            self._board[position] = PieceType("TANGERINE", position)

        # places the Amethyst pieces using enumerate - same logic as above
        for index,PieceType in enumerate(order):
            col = columns[index]
            position = col + "7"
            self._board[position] = PieceType("AMETHYST", position)