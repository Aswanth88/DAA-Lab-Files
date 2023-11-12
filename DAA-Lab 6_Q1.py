def is_cycle(graph):
    def dfs(node,visited,recursion_stack):
        visited[node]=True
        recursion_stack[node]=True
        for neighbor in graph.get(node,[]):
            if not visited[neighbor]:
                if dfs(neighbor,visited,recursion_stack):
                    return True
            elif recursion_stack[neighbor]:
                return True
            
        recursion_stack[node]=False
        return False
    
    nodes=graph.keys()
    visited={node:False for node in nodes}
    recursion_stack={node:False for node in nodes}

    for node in nodes:
        if not visited[node]:
            if dfs(node,visited,recursion_stack):
                return True
            
    return False

graph={
    1:[2],
    2:[4],
    4:[1,3],
    3:[2]

}

if is_cycle(graph):
    print('The graph has cycle')
else:
    print('The graph has  no cycle')