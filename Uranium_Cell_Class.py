from Cooling_Component_Parent_class import Reactor_Component, Cooling_Component

class Uranium_Cell(Reactor_Component):
    def __init__(self, hull, location:tuple) -> None:
        super().__init__(hull, location)
        self.name = "Uranium Cell"
        self.health = 10000

    def heat_calc(self) -> None:
        U = 0
        coolant_sum = 0

        # Check uranium cells around the current cell
        if isinstance(self.left, Uranium_Cell):
            U += 1
        if isinstance(self.right, Uranium_Cell):
            U += 1
        if isinstance(self.up, Uranium_Cell):
            U += 1
        if isinstance(self.down, Uranium_Cell):
            U += 1

        # Check cooling components around the current cell
        if isinstance(self.left, Cooling_Component):
            coolant_sum += 1
        if isinstance(self.right, Cooling_Component):
            coolant_sum += 1
        if isinstance(self.up, Cooling_Component):
            coolant_sum += 1
        if isinstance(self.down, Cooling_Component):
            coolant_sum += 1

        # Calculate coolant value C
        C = 1 if coolant_sum == 0 else coolant_sum

        # Calculate heat H
        H = (U + 1) * (10 - (C - 1) * 2)

        # Distribute heat accordingly
        if coolant_sum == 0:
            self.hull.internal_heat += H
            print(f"I'm adding {H} heat to the hull here, it is currently {self.hull.internal_heat}")
        else:
            if isinstance(self.left, Cooling_Component):
                self.left.add_primary(H/C)
            if isinstance(self.right, Cooling_Component):
                self.right.add_primary(H/C)
            if isinstance(self.up, Cooling_Component):
                self.up.add_primary(H/C)
            if isinstance(self.down, Cooling_Component):
                self.down.add_primary(H/C)
        
    def energy_calc(self) -> int:
        sides = (self.left, self.right, self.up, self.down)
        U = 5
        for side in sides:
            if isinstance(side, Uranium_Cell):
                U += 5
        return U

    def run(self):
        self.heat_calc()
        self.hull.total_energy_output += self.energy_calc()
        self.health -= 1
        if self.health == 0:
            self.self_destruct()

    def __repr__(self) -> str:
        return 'U'
