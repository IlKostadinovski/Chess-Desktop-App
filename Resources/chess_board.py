class ChessBoard:
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.last_move = None

    def coord_to_index(self, col, row):
        return row * 8 + col  # Chessboard math, anyone?

    def get_board(self):
        return self.board

    def check_if_box_is_empty(self, row, col):
        return self.board[row][col] == "--"

    def move_piece(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        piece = self.board[start_row][start_col]

        # Handle en passant capture
        if piece[1] == "P" and abs(start_col - end_col) == 1 and self.board[end_row][end_col] == "--":
            if piece[0] == "w" and start_row == 3:
                self.board[end_row + 1][end_col] = "--"
            elif piece[0] == "b" and start_row == 4:
                self.board[end_row - 1][end_col] = "--"

        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = "--"

        self.last_move = (self.coord_to_index(start_col, start_row), self.coord_to_index(end_col, end_row))

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def check_piece_type(self, row, col):
        piece_map = {
            "wB": ("bishop", "white"),
            "bB": ("bishop", "black"),
            "wN": ("knight", "white"),
            "bN": ("knight", "black"),
            "wR": ("rook", "white"),
            "bR": ("rook", "black"),
            "wP": ("pawn", "white"),
            "bP": ("pawn", "black"),
            "wQ": ("queen", "white"),
            "bQ": ("queen", "black"),
            "wK": ("king", "white"),
            "bK": ("king", "black")
        }

        piece = self.board[row][col]
        return piece_map.get(piece, None)
