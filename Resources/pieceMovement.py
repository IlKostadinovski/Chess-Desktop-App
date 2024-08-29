class PieceMovement:
    def __init__(self, row, col, board, color):
        self.current_position = self.coord_to_index(col, row)
        self.color = color
        self.row = row
        self.col = col
        self.board = board

    def coord_to_index(self, col, row):
        return row * 8 + col

    def index_to_coord(self, index):
        row = index // 8
        col = index % 8
        return row, col

    def is_within_board(self, index):
        return 0 <= index < 64

    def is_opponent_piece(self, board, index):
        row, col = self.index_to_coord(index)
        piece = board.get_board()[row][col]
        return piece != "--" and (piece.startswith("b") if self.color == "white" else piece.startswith("w"))

    def is_square_occupied(self, index):
        row, col = self.index_to_coord(index)
        piece = self.board.get_board()[row][col]
        return piece != "--"
