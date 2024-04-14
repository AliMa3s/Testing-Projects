import heapq

def dijkstra(graph, start):
    # The shortest paths are stored in this dictionary
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0

    # Priority queue to store vertices to be examined
    pq = [(0, start)]
    
    while pq:
        # The vertex in pq with the smallest distance
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can only be added once to the queue
        if current_distance > shortest_paths[current_vertex]:
            continue

        # Visit each neighbor of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return shortest_paths

# Example graph as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Calculate shortest path from vertex 'A'
shortest_paths = dijkstra(graph, 'A')
print(shortest_paths)
