from Cooling_Component_Parent_class import Cooling_Component

class Integrated_Heat_Disperser(Cooling_Component):
    def __init__(self, hull, location) -> None:
        super().__init__(hull, location)
        self.name = 'Integrated Heat Disperser'

    def run(self):
        super().run()
        variables = [self.internal_heat, self.hull.internal_heat]
        if max(variables) - min(variables) > 0:
            max_index = variables.index(max(variables))
            min_index = variables.index(min(variables))
            
            # Calculate the difference between the max and min values
            diff = max(variables) - min(variables)
            
            # Transfer half of the smaller of 'step' or 'diff'
            transfer_amount = min(50, diff) / 2
            variables[max_index] -= transfer_amount
            variables[min_index] += transfer_amount

            ### I don't think this is correct
            self.internal_heat, self.hull.internal_heat = variables


        neighbors = [self.left, self.right, self.up, self.down]
        for neighbor in neighbors:
            if isinstance(neighbor, Cooling_Component):
                variables = [self.internal_heat, neighbor.internal_heat]
                if max(variables) - min(variables) > 0:
                    max_index = variables.index(max(variables))
                    min_index = variables.index(min(variables))
                    
                    # Calculate the difference between the max and min values
                    diff = max(variables) - min(variables)
                    
                    # Transfer half of the smaller of 'step' or 'diff'
                    transfer_amount = min(12, diff) / 2
                    variables[max_index] -= transfer_amount
                    variables[min_index] += transfer_amount

                    self.internal_heat, self.hull.internal_heat = variables

    
    def __repr__(self) -> str:
        return 'H'