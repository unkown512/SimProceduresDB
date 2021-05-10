import angr
from angrutils import *
from paths_to_target import PathsToTarget

class PathStats():
    def __init__(self, paths, proj):
        self.paths = paths
        self.proj = proj
        self.path_rank = []

    def shortest_path_by_edges(self):
        self.paths = sorted(self.paths, key=lambda x: len(x['nodes']))
        return self.paths[0]['nodes']

    def calc_sim_frequency(self):
        for path in self.paths:
            for node in path['nodes']:
                if node.is_simprocedure == True:
                    if node.simprocedure_name not in path.keys():
                        path['sim_count'] = 1
                        path[node.simprocedure_name] = {'freq': 1}
                    else:
                        path[node.simprocedure_name]['freq'] += 1
                        path['sim_count'] += 1

    def calc_instruction_freq(self):
        for path in self.paths:
            path['ins_freq'] = 0
            for node in path['nodes']:
                if node.block is not None:
                    path['ins_freq'] += node.block.instructions
                else:
                    # syscall or SimProcedure...Needs sperate evalutation
                    path['ins_freq'] += 1

    def calc_symbolic_score(self):
        for path in self.paths:
            path['mov_score'] = 0
            path['lea_score'] = 0
            path['call_score'] = 0
            for node in path['nodes']:
                if node.block is not None:
                    for instruction in node.block.disassembly.insns:
                        if "mov" == instruction.mnemonic:
                            path['mov_score'] += 1
                        elif "lea" == instruction.mnemonic:
                            path['lea_score'] += 1
                        elif "call" == instruction.mnemonic:
                            path['call_score'] += 1


