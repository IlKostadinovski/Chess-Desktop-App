from Resources.pieceMovement import PieceMovement

class Pawn(PieceMovement):

    def get_possible_moves(self):
        possible_moves = []

        whiteDirection = -8  # White moves upwards (negative direction)
        blackDirection = +8  # Black moves downwards (positive direction)

        if self.color == "white":
            tempINDEX = self.current_position + whiteDirection

            if self.is_within_board(tempINDEX) and not self.is_square_occupied(tempINDEX):
                possible_moves.append(tempINDEX)
                if self.row == 6 and not self.is_square_occupied(tempINDEX + whiteDirection):
                    possible_moves.append(tempINDEX + whiteDirection)

            if self.is_within_board(tempINDEX - 1) and self.is_opponent_piece(self.board, tempINDEX - 1):
                possible_moves.append(tempINDEX - 1)
            if self.is_within_board(tempINDEX + 1) and self.is_opponent_piece(self.board, tempINDEX + 1):
                possible_moves.append(tempINDEX + 1)

            if self.row == 3:
                if self.is_en_passant_possible(-1):
                    possible_moves.append(self.current_position + whiteDirection - 1)
                if self.is_en_passant_possible(+1):
                    possible_moves.append(self.current_position + whiteDirection + 1)

        elif self.color == "black":
            tempINDEX = self.current_position + blackDirection

            if self.is_within_board(tempINDEX) and not self.is_square_occupied(tempINDEX):
                possible_moves.append(tempINDEX)
                if self.row == 1 and not self.is_square_occupied(tempINDEX + blackDirection):
                    possible_moves.append(tempINDEX + blackDirection)

            if self.is_within_board(tempINDEX - 1) and self.is_opponent_piece(self.board, tempINDEX - 1):
                possible_moves.append(tempINDEX - 1)
            if self.is_within_board(tempINDEX + 1) and self.is_opponent_piece(self.board, tempINDEX + 1):
                possible_moves.append(tempINDEX + 1)

            if self.row == 4:
                if self.is_en_passant_possible(-1):
                    possible_moves.append(self.current_position + blackDirection - 1)
                if self.is_en_passant_possible(+1):
                    possible_moves.append(self.current_position + blackDirection + 1)

        return [self.index_to_coord(move) for move in possible_moves]

    def is_en_passant_possible(self, direction):
        last_move = self.board.last_move
        if last_move:
            start = last_move[0]
            end = last_move[1]

            start_row, start_col = self.index_to_coord(start)
            end_row, end_col = self.index_to_coord(end)
            adjacent_index = self.current_position + direction
            adjacent_row, adjacent_col = self.index_to_coord(adjacent_index)

            # En Passant logic here is kind weird but it works xD
            if (
                    abs(start_row - end_row) == 2
                    and end_col == adjacent_col
                    and self.board.get_board()[end_row][end_col][1] == "P"
                    and self.board.get_board()[end_row][end_col][0] != self.color[0]
            ):
                return True
        return False
