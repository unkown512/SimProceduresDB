import angr
import claripy

class Scanf2Buffs(angr.SimProcedure):
    def run(self):
        scanf0 = claripy.BVS('scanf0', ???)

        for char in scanf0.chop(bits=8):
            self.state.add_constraints(char >= ???, char <= ???)

        scanf0_address = ???
        self.state.memory.store(scanf0_address, scanf0)

        return 2
