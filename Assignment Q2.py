import heapq

def build_graph():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        line = input()
        if line == "0":
            break
        a, b, c = map(int, line.split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    unsafe_times = [[] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        line = input()
        ki, *tij = map(int, line.split())
        unsafe_times[i] = tij
    
    return n, graph, unsafe_times

def shortest_path(n, graph, unsafe_times):
    INF = float('inf')
    dist = [INF] * (n + 1)
    visited = [False] * (n + 1)
    heap = [(0, 1)]  
    dist[1] = 0
    
    while heap:
        time, universe = heapq.heappop(heap)
        
        if visited[universe]:
            continue
        
        visited[universe] = True
        
        for neighbor, travel_time in graph[universe]:
            next_time = time + travel_time
            wait_time = 0
            
            for unsafe_time in unsafe_times[neighbor]:
                if next_time >= unsafe_time:
                    wait_time = max(wait_time, unsafe_time + 1)
                else:
                    break
            
            next_time += wait_time
            
            if next_time < dist[neighbor]:
                dist[neighbor] = next_time
                heapq.heappush(heap, (next_time, neighbor))
    
    return dist[n]

n, graph, unsafe_times = build_graph()
result = shortest_path(n, graph, unsafe_times)

if result == float('inf'):
    print(-1)
else:
    print("Possible central cities:", result)