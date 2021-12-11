class Player:
    def __init__(self, n, m, color):
        self.player_color = color  # crni X beli O podrazumevano crni
        self.player_turn = True if color == "black" else False  # podrazumevano X igra prvi
        self.pawn_one_position = [3, 3] if self.player_color == "black" else [7, 3]
        self.pawn_two_position = [3, 10] if self.player_color == "black" else [7, 10]
        self.available_walls = (n - m) * 3  # na pocetku igre svako ima po 9-18 zidova, smanjuje se kad se postavi
        self.symbol = "X" if self.player_color == "black" else "O"
