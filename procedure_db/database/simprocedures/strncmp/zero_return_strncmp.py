import angr

class zero_extend_strncmp(angr.SimProcedure):
    def run(self):
        return 0
