from Resources.pieceMovement import PieceMovement

class Knight(PieceMovement):

    def get_possible_moves(self):
        possible_moves = []
        knight_moves = [
            -17, -15, -10, -6, 6, 10, 15, 17  # All possible "L" moves for a knight
        ]

        for move in knight_moves:
            temp_pos = self.current_position + move

            if not self.is_within_board(temp_pos):
                continue

            row, col = self.index_to_coord(temp_pos)
            current_row, current_col = self.index_to_coord(self.current_position)

            if abs(current_row - row) > 2 or abs(current_col - col) > 2:
                continue  # Skip invalid "L" shaped moves that wrap the board


            if not self.board.check_if_box_is_empty(row, col):
                if not self.is_opponent_piece(self.board, temp_pos):
                    continue  # Friendly piece blocks the move
                else:
                    # If it's an opponent piece, the knight can capture it
                    possible_moves.append(temp_pos)
            else:
                # If the position is empty, add it to the possible moves
                possible_moves.append(temp_pos)

        possible_moves_coord = [self.index_to_coord(move) for move in possible_moves]
        return possible_moves_coord
