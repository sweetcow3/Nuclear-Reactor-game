from Reactor_Component_GP_Class import Reactor_Component

class Cooling_Component(Reactor_Component):
    def __init__(self, hull, location) -> None:
        super().__init__(hull, location)
        self.internal_heat = 0
        self.name = 'Cooling Component'
        self.max_heat = 10000
        

    def run(self) -> None:
        super().run()
        if self.internal_heat >= self.max_heat:
            self.self_destruct()

    def add_primary(self, value) -> None:
        self.add_heat(value)

    def add_heat(self, value) -> None:
        self.internal_heat += value