import angr
from angrutils import *
import copy

proj = angr.Project('toy1', arch='X86', auto_load_libs=False)
entry_point = proj.entry

main_symbol = proj.loader.main_object.get_symbol("main")
if main_symbol:
    entry_point = main_symbol.rebased_addr

cfg = proj.analyses.CFGEmulated(starts=[entry_point])

call_list = {} 
#print(dir(cfg.kb.callgraph))
#print(dir(cfg.kb.xrefs))
#print(len(cfg.graph.nodes()))

#print(dir(proj.kb.functions))
for f in cfg.kb.functions.items():
    if f[1].symbol is None or "__" in f[1].symbol.name:
        continue
    if "UnresolvableJumpTarget" in f[1].symbol.name:
        continue
    call_list[str(f[1].symbol.name)] = {
        'info': f, 'freq': 1, 'is_simprocedure': f[1].is_simprocedure
    }
    #print(f[1].get_call_sites()


def find_parent_path(node_predecessors):
    node_predecessors = [node.addr for node in node_predecessors]
    path_index_list = []
    index = 0
    for path in paths_to_goal:
        if path['nodes'][-1].addr in node_predecessors:
            path_index_list.append(index)
        index += 1

    if len(path_index_list) == 0:
        return (False, -1)

    return (True, path_index_list)

paths_to_goal = []

entry_node = None
for node in cfg.graph.nodes():
    entry_node = node
    break
paths_to_goal.append(
    {'nodes': [entry_node]}
)
node_added = 1
while node_added != 0:
    node_added = 0
    #print(paths_to_goal)
    for path in paths_to_goal:
        successors = path['nodes'][-1].successors

        # Check if path has ended (deadend)
        if len(successors) == 0:
            continue
        
        # Add nodes to path
        #print(len(successors))
        if len(successors) == 1:
            path['nodes'].append(successors[0])
            node_added = 1 
        else:
            node_added = 1
            new_path = copy.deepcopy(path)
            for succ in successors[1:]:
                new_path['nodes'].append(succ)
                paths_to_goal.append(
                    new_path
                )
            path['nodes'].append(successors[0])


for path in paths_to_goal:
    print(path)
    print(len(path['nodes']))
    print("\n\n")
quit()

# Goal addr dest = 0x50000c

'''
j = 0
for node in cfg.graph.nodes():
    # Setup starting node in path
    #print(node.addr)
    #print(node.name)
    #print(node.function_address)

    #print(node.predecessors)
    if len(paths_to_goal) == 0:
        paths_to_goal.append(
            {'start': node, 'nodes': []}
        )
        j += 1
        print(node.successors[0].successors)
        continue
    quit()
    # Add more paths based on # of predecessors
    predecessors = node.predecessors
    result = False
    if len(predecessors) == 1:
        result, path_index_list = find_parent_path(predecessors)
        if result:
            # only one parent to update
            paths_to_goal[path_index_list[-1]]['nodes'].append(node)
    else:
        # Multiple parents to update
        result, path_index_list = find_parent_path(predecessors)
        if result:
            print(len(path_index_list))
            print(len(predecessors))
            for path_index in path_index_list:
                paths_to_goal[path_index]['nodes'].append(node)
    
    #print(dir(node))
    #print(hex(node.addr))
    #print(dir(node))
    #print(dir(node.successors))
    #for n in node.successors:
    #    print(dir(n))
    #is_simprocedure, is_syscall
    #print(node.simprocedure_name)
    #print(node.instruction_addrs)
    #print(node.addr)

    #print(dir(node.block))
    #break
    #print(node.block.disassembly)
    #print(node.block.instructions) # COUNT
    #print(node.block.size)
    #print(node.block.disassembly)
'''
print(paths_to_goal)
plot_cfg(cfg, "dynamic", asminst=True, remove_imports=True, remove_path_terminator=True)
