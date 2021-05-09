import angr

class strncmp(angr.SimProcedure):
    def run(self):
        eax = self.state.solver.BVS('eax', 1*8)
        self.state.solver.add(eax >= -1)
        self.state.solver.add(eax <= 1)

        return eax

