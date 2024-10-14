from Cooling_Component_Parent_class import Cooling_Component

class Integrated_Reactor_Plating(Cooling_Component):
    def __init__(self, hull, location) -> None:
        super().__init__(hull, location)
        self.name = 'Integrated Reactor Plating'
        self.coolants = None

    def run(self):
        super().run()
        if self.internal_heat > 0:
            self.internal_heat -= 0.1

    def add_primary(self, value) -> None:
        if not self.cooling:
            self.coolants = {"left": 0, "right": 0, "up": 0, "down": 0}
            row, col = self.row, self.column
            max_row, max_col = 8, 5

            self.coolants['left'] = 1 if row > 0 and isinstance(self.hull.inside[row - 1][col], Cooling_Component) else 0
            self.coolants['right'] = 1 if row < max_row and isinstance(self.hull.inside[row + 1][col], Cooling_Component) else 0
            self.coolants['up'] = 1 if col > 0 and isinstance(self.hull.inside[row][col - 1], Cooling_Component) else 0
            self.coolants['down'] = 1 if col < max_col and isinstance(self.hull.inside[row][col + 1], Cooling_Component) else 0

        coolant_sum = sum(self.coolants.values())
        if coolant_sum == 0:
            self.hull.internal_heat += value
        else:
            if self.coolants['left']:
                self.hull.inside[row - 1][col].add_heat(value/coolant_sum)
            if self.coolants['right']:
                self.hull.inside[row + 1][col].add_heat(value/coolant_sum)
            if self.coolants['up']:
                self.hull.inside[row][col - 1].add_heat(value/coolant_sum)
            if self.coolants['down']:
                self.hull.inside[row][col + 1].add_heat(value/coolant_sum)

    def __repr__(self) -> str:
        return 'R'