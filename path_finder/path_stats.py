import angr
from angrutils import *
from paths_to_target import PathsToTarget

class PathStats():
    def __init__(self, paths, proj):
        self.paths = paths
        self.proj = proj

    def shortest_path(self):
        self.paths = sorted(self.paths, key=lambda x: len(x['nodes']))
        return self.paths[0]['nodes']

