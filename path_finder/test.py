from paths_to_target import PathsToTarget
from path_stats import PathStats

PF = PathsToTarget("0x400827", "/home/djbey/angr_extended/SimProceduresDB/tests/toy1")
if PF.get_target_node():
    PF.recursive_path_finder(0)
    #for path in PF.paths_to_target:
    #    print(path)
    #    print("\n\n")
    print(f"Total paths found: {len(PF.paths_to_target)}")
PS = PathStats(PF.paths_to_target, PF.proj)



print("Shortest Path")
print(PS.shortest_path_by_edges())

print("path stats")
#print(PS.calc_sim_frequency())
#print(PS.calc_instruction_freq())
print(PS.calc_symbolic_score())
quit()
print(PS.paths[0]['nodes'])
print(PS.paths['sim_stats'])

for path in PS.paths:
    print("***********************")
    print(len(path['nodes']))
    print(path['nodes'])
    #print(path.keys())
    #print(path['sim_count'])

