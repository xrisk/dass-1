import entity
from colorama import Fore, Back


class Floor(entity.Entity):
    def __init__(self, *args):
        super().__init__(*args)

    def render(self, buf):

        with open("brick.txt") as f:
            texture = f.readlines()

        texture = [s[:-1] for s in texture]

        row_count = self.g.row
        for col in range(self.g.col):
            for k in range(row_count - 5, row_count):
                buf[k][col] = (
                    Fore.MAGENTA
                    + texture[k - (row_count)][col % len(texture[0])]
                    + Fore.RESET
                )
                self.g.backing[(k, col)].append(self)


class Sky(entity.Entity):
    def __init__(self, *args):
        super().__init__(*args)

    def render(self, buf):
        for col in range(self.g.col):
            for k in range(2):
                buf[k][col] = Fore.BLUE + "~" + Fore.RESET
                self.g.backing[(k, col)].append(self)
