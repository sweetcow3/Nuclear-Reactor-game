from Cooling_Component_Parent_class import Cooling_Component

class Cooling_Cell(Cooling_Component):
    def __init__(self, hull, location) -> None:
        super().__init__(hull, location)
        self.name = 'Cooling Cell'

    def run(self):
        super().run()
        if self.internal_heat > 0:
            self.internal_heat -= 1

    def __repr__(self) -> str:
        return 'C'