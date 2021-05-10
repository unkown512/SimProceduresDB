import angr
from angrutils import *
import copy

class PathsToTarget():
    def __init__(self, target_addr, program_path):
        self.target_addr = target_addr
        self.program_path = program_path
        self.target_node = None
        self.paths_to_target = []

        self.proj = angr.Project(program_path, auto_load_libs=False)
        self.entry_point = self.proj.entry

        main_symbol = self.proj.loader.main_object.get_symbol("main")
        if main_symbol:
            self.entry_point = main_symbol.rebased_addr
        
        self.cfg = self.proj.analyses.CFGEmulated(starts=[self.entry_point])
        self.main_node = None

    def _add_new_path(self, new_path):
        self.paths_to_target.append(new_path)
        return len(self.paths_to_target)-1

    def get_target_node(self):

        # TODO: Check if target node is simprocedure
        i = 0
        for node in self.cfg.graph.nodes():
            if i == 0:
                self.main_node = node
            if node.block is None:
                continue
            if int(self.target_addr, 16) in node.block.instruction_addrs:
                self.target_node = node
                self.paths_to_target.append({'nodes': [node]})
                return True
            i += 1

        return False

    def recursive_path_finder(self, index):
        preds = self.paths_to_target[index]['nodes'][-1].predecessors
        if len(preds) == 0:
            print("MAIN FOUND")
            return 0 

        new_path = copy.deepcopy(self.paths_to_target[index])
        self.paths_to_target[index]['nodes'].append(preds[0])
        for pred in preds[1:]:
            new_path['nodes'].append(pred)
            new_index = self._add_new_path(new_path)
            self.recursive_path_finder(new_index)
        print("index", index)
        return self.recursive_path_finder(index)

