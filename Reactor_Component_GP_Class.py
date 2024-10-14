from Empty_class import Empty

class Reactor_Component:
    def __init__(self, hull, location) -> None:
        self.name = 'Reactor Component'
        self.hull = hull
        self.row = location[0]
        self.column = location[1]
        self.left = Empty()
        self.right = Empty()
        self.up = Empty()
        self.down = Empty()

    def neighbors(self):
        """Takes note of what is around the component"""
        row, col = self.row, self.column
        max_row, max_col = len(self.hull.inside[0]) - 1, len(self.hull.inside) - 1

        if row > 0:
            self.left = self.hull.inside[col][row - 1]
        if row < max_row:
            self.right = self.hull.inside[col][row + 1]
        if col > 0:
            self.up = self.hull.inside[col - 1][row]
        if col < max_col:
            self.down = self.hull.inside[col + 1][row]

    def self_destruct(self):
        self.hull.inside[self.column][self.row] = Empty()
        if isinstance(self.left, Reactor_Component):
            self.left.right = Empty()
        if isinstance(self.right, Reactor_Component):
            self.left.left = Empty()
        if isinstance(self.up, Reactor_Component):
            self.left.down = Empty()
        if isinstance(self.down, Reactor_Component):
            self.left.up = Empty()

    def run(self):
        pass