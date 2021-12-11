class Wall:
    def __init__(self):
        self.wall_color = "blue"  # plavi podrazumevano (=) a zeleni(∥)
        self.wall_look = "=" if self.wall_color == "blue" else "∥"
        self.wall_position = []


# uspravni gadja desni zid polja i donji desni zid
# vodoravni zid gadja donji zid polja i desni donji zid