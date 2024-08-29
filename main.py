import pygame
import sys
from Resources.chess_board import ChessBoard
from Resources.bishop import Bishop
from Resources.pawn import Pawn
from Resources.rook import Rook
from Resources.knight import Knight
from Resources.queen import Queen
from Resources.king import King



pygame.init()


WIDTH, HEIGHT = 800, 800
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15


def load_images():
    pieces = ['bBishop', 'bKing', 'bKnight', 'bPawn', 'bQueen', 'bRook', 'wBishop', 'wKing', 'wKnight', 'wPawn', 'wQueen', 'wRook']
    images = {}
    for piece in pieces:
        images[piece] = pygame.transform.scale(pygame.image.load(f"graphics/{piece}.png"), (70, 70))
    images['board'] = pygame.transform.scale(pygame.image.load("graphics/chessBoard.jpg"), (WIDTH, HEIGHT))
    return images


def draw_game_state(screen, board, images, possible_moves=None):
    draw_board(screen, images)
    if possible_moves:
        highlight_moves(screen, possible_moves)
    draw_pieces(screen, board, images)

def draw_board(screen, images):
    screen.blit(images['board'], (0, 0))

def draw_pieces(screen, board, images):
    piece_name_mapping = {
        "bR": "bRook", "bN": "bKnight", "bB": "bBishop", "bQ": "bQueen", "bK": "bKing", "bP": "bPawn",
        "wR": "wRook", "wN": "wKnight", "wB": "wBishop", "wQ": "wQueen", "wK": "wKing", "wP": "wPawn"
    }
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board.board[r][c]
            if piece != "--":
                x = c * 101 + 10
                y = r * 101 + 10
                screen.blit(images[piece_name_mapping[piece]], pygame.Rect(x, y, SQ_SIZE, SQ_SIZE))

def highlight_moves(screen, possible_moves):
    green_color = (0, 255, 0)
    fade = 100
    highlight_surface = pygame.Surface((SQ_SIZE, SQ_SIZE))
    highlight_surface.set_alpha(fade)
    highlight_surface.fill(green_color)
    for move in possible_moves:
        row, col = move
        screen.blit(highlight_surface, (col * SQ_SIZE, row * SQ_SIZE))


def handle_piece_selection(selected_square, board, turn):
    row, col = selected_square
    piece_type, piece_color = board.check_piece_type(row, col)
    if piece_color == turn:
        print(f"Valid selection: {piece_type} ({piece_color})")
        return selected_square, piece_type
    else:
        print(f"Invalid selection: It's {turn}'s turn, but you selected a {piece_color} piece.")
        return None, None


def get_moving_options(selected_square, board, piece_type, color):
    row, col = selected_square
    possible_moves = []

    if piece_type == "bishop":
        bishop = Bishop(row, col, board, color)
        possible_moves = bishop.get_possible_moves()

    elif piece_type == "pawn":
        pawn = Pawn(row, col, board, color)
        possible_moves = pawn.get_possible_moves()

    elif piece_type == "rook":
        rook = Rook(row, col, board, color)
        possible_moves = rook.get_possible_moves()

    elif piece_type == "knight":
        knight = Knight(row, col, board, color)
        possible_moves = knight.get_possible_moves()

    elif piece_type == "queen":
        queen = Queen(row, col, board, color)
        possible_moves = queen.get_possible_moves()

    elif piece_type == "king":
        king = King(row, col, board, color)
        possible_moves = king.get_possible_moves()

    return possible_moves


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    board = ChessBoard()
    images = load_images()
    running = True
    selected_square = None
    piece_type = None
    turn = "white"
    possible_moves = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE

                if selected_square is None:
                    if not board.check_if_box_is_empty(row, col):
                        selected_square, piece_type = handle_piece_selection((row, col), board, turn)
                        if selected_square:
                            possible_moves = get_moving_options(selected_square, board, piece_type, turn)
                    else:
                        selected_square = None
                else:
                    if (row, col) in possible_moves:
                        board.move_piece(selected_square, (row, col))
                        turn = "black" if turn == "white" else "white"
                    selected_square = None
                    possible_moves = []

        draw_game_state(screen, board, images, possible_moves)
        clock.tick(MAX_FPS)
        pygame.display.flip()

if __name__ == "__main__":
    main()
