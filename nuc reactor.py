from Empty_class import Empty
from Uranium_Cell_Class import Uranium_Cell
from Cooling_Cell_Class import Cooling_Cell
from Integrated_Heat_Disperser import Integrated_Heat_Disperser
from Integrated_Reactor_Plating_Class import Integrated_Reactor_Plating
from Reactor_Component_GP_Class import Reactor_Component

class nuc_reactor:
    """Inside needs to be a 9x6 list"""
    def __init__(self, inside=None, outside=(0,20)) -> None:
        self.category = None
        self.runtime = 0
        self.did_anything_selfdestruct = False

        self.hull_str = 16000
        self.internal_heat = 0
        self.energy_output = 0
        self.total_energy_output = 0

        self.inside_numbers = [[y+x*9 for y in range(9)] for x in range(6)]

        # Check if 
        if len(outside) != 2 or sum(outside) > 20:
            raise ValueError("Must be two numbers whose sum is less than 20")
        self.outside_cooling = 1 + 6 * 2 + outside[0] * .25 + outside[1]

        if not inside:
            self.inside = [[Empty() for y in range(9)] for x in range(6)]
        else:
            self.inside = []
            for y, line in enumerate(inside):
                self.inside.append([])
                for x, obj in enumerate(line):
                    match obj.upper():
                        case 'E':
                            self.inside[-1].append(Empty())
                        case 'U':
                            self.inside[-1].append(Uranium_Cell(self, (x,y)))
                        case 'C':
                            self.inside[-1].append(Cooling_Cell(self, (x,y)))
                        case 'R':
                            self.inside[-1].append(Integrated_Reactor_Plating(self, (x,y)))
                        case 'H':
                            self.inside[-1].append(Integrated_Heat_Disperser(self, (x,y)))

        Uranium_cells = 0
        Sum_of_neighbors = 0
        for col in self.inside:
            for item in col:
                if isinstance(item, Reactor_Component):
                    item.neighbors()
                    if isinstance(item, Uranium_Cell):
                        Uranium_cells += 1
                        Sum_of_neighbors += 1
                        for N in (item.left, item.right, item.up, item.down):
                            if isinstance(N, Uranium_Cell):
                                Sum_of_neighbors += 1
        self.efficency = Sum_of_neighbors / Uranium_cells if Uranium_cells != 0 else 0
                                

    def uranium_check(self):
        if not recursive_check(self.inside, Uranium_Cell):
            if self.internal_heat <= 100:
                self.category = "Mark I"
            else:
                self.category = "Mark II"


    def scan_inside(self) -> None:
        for y in range(len(self.inside)):
            for x in range(len(self.inside[y])):
                if isinstance(self.inside[y][x], Uranium_Cell):
                    self.Uranium.append([x,y])
                elif isinstance(self.inside[y][x], Cooling_Cell):
                    self.Cooling.append([x,y])
                elif isinstance(self.inside[y][x], Integrated_Reactor_Plating):
                    self.Reactor_Plating.append([x,y])
                elif isinstance(self.inside[y][x], Integrated_Heat_Disperser):
                    self.Heat_Disperser.append([x,y])

    def run(self) -> None:
        self.runtime += 1
        for col in self.inside:
            for item in col:
                item.run()
        self.internal_heat -= self.outside_cooling
        # print(f"The hull self cooled itself by: {self.outside_cooling}, heat is now: {self.internal_heat}")
        if self.internal_heat < 0:
            self.internal_heat = 0
        if self.internal_heat >= 8000:
            self.outside_cooling = 18
    
def recursive_check(items, target_class):
    for item in items:
        if isinstance(item, list):
            if recursive_check(item, target_class):
                return True
        elif isinstance(item, target_class):
            return True
    return False

A = nuc_reactor([
    ['C', 'C', 'H', 'C', 'H', 'C', 'H', 'C', 'C'],
    ['H', 'C', 'C', 'C', 'U', 'C', 'C', 'C', 'H'],
    ['C', 'H', 'C', 'H', 'U', 'H', 'C', 'H', 'C'],
    ['C', 'C', 'C', 'H', 'U', 'H', 'C', 'C', 'C'],
    ['H', 'C', 'C', 'C', 'U', 'C', 'C', 'C', 'H'],
    ['C', 'C', 'H', 'C', 'H', 'C', 'H', 'C', 'C']])

for line in A.inside:
    print(line)

while recursive_check(A.inside, Uranium_Cell):
    A.run()
    if A.internal_heat > A.hull_str:
        print("Reactor exploded!")
        if A.runtime < 1000:
            A.category = "Mark V"
        else:
            if A.did_anything_selfdestruct:
                A.category = "Mark IV"
            else:
                A.category = "Mark III"
        break
print(f'Heat: {A.internal_heat}')
print(f'Total Energy Output: {A.total_energy_output}')

for line in A.inside:
    print(line)

print(A.category)
print(A.efficency)