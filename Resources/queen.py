from Resources.pieceMovement import PieceMovement

class Queen(PieceMovement):

    def get_possible_moves(self):
        possible_moves = []
        directions = [-8, 8, -1, 1, -9, -7, 9, 7]

        for direction in directions:
            temp_pos = self.current_position

            while True:
                temp_pos += direction

                if not self.is_within_board(temp_pos):
                    break

                row, col = self.index_to_coord(temp_pos)
                current_row, current_col = self.index_to_coord(self.current_position)

                if direction in [-1, 1] and row != current_row:
                    break

                if direction in [-9, -7, 9, 7]:
                    if abs(current_row - row) != abs(current_col - col):
                        break

                if not self.board.check_if_box_is_empty(row, col):
                    if not self.is_opponent_piece(self.board, temp_pos):
                        break
                    else:
                        possible_moves.append(temp_pos)
                        break

                possible_moves.append(temp_pos)

        possible_moves_coord = [self.index_to_coord(move) for move in possible_moves]
        return possible_moves_coord
