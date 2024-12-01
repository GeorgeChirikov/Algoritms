import heapq

def dijkstra_shortest_path(source_vertex, destination_vertex, graph):
    """
    Calculate the shortest path (in distance value) between given vertices.

    Parameters:
    - source_vertex: The source vertex
    - destination_vertex: The destination vertex
    - graph: The graph in question

    Returns: a tuple containing the minimum distance between vertices and a list of
             vertices that form the minimum path from one vertex to the other.
    """
    # Initialize the distances dictionary, all set to infinity except the source
    distances = {v: float('inf') for v in graph.get_vertices()}
    distances[source_vertex] = 0

    # Initialize the predecessors dictionary to reconstruct the path
    predecessors = {v: None for v in graph.get_vertices()}

    # Min-heap for priority queue to get the vertex with the smallest distance
    priority_queue = [(0, source_vertex)]  # (distance, vertex)

    while priority_queue:
        # Get the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If we've reached the destination vertex, stop early
        if current_vertex == destination_vertex:
            break

        # If the current distance is greater than the known shortest distance, skip it
        if current_distance > distances[current_vertex]:
            continue

        # Relax edges
        for neighbor in graph.get_adjacent_vertices(current_vertex):
            edge = graph.get_edge(current_vertex, neighbor)
            if edge:
                new_distance = current_distance + edge.get_weight()
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (new_distance, neighbor))

    # Reconstruct the shortest path from destination to source using predecessors
    path = []
    current_vertex = destination_vertex
    while current_vertex is not None:
        path.insert(0, current_vertex)
        current_vertex = predecessors[current_vertex]

    # If the path is empty, there is no path
    if not path or path[0] != source_vertex:
        return (float('inf'), [])

    # Return the total minimum distance and the path
    return (distances[destination_vertex], path)


