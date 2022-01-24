class Player:
    def __init__(self, n, m, color, x1, x2, y1, y2):
        self.player_color = color  # crni X beli O podrazumevano crni
        self.player_turn = True if color == "black" else False  # podrazumevano X igra prvi
        # self.pawn_one_position = [3, 3] if self.player_color == "black" else [7, 3]
        # self.pawn_two_position = [3, 10] if self.player_color == "black" else [7, 10]
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.pawn_one_position = [x1, x2]
        self.pawn_two_position = [y1, y2]
        self.available_walls = (n - m) * 3  # na pocetku igre svako ima po 9-18 zidova, smanjuje se kad se postavi
        self.symbol = "X" if self.player_color == "black" else "O"
