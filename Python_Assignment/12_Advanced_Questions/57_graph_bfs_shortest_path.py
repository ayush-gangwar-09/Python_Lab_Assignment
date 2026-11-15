# Question 7: Find the shortest path in an unweighted graph using BFS.


from collections import deque


def shortest_path(graph, start, target):
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        current_node = path[-1]

        if current_node == target:
            return path

        for neighbour in graph.get(current_node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                new_path = path + [neighbour]
                queue.append(new_path)

    return None


# Example graph.
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

start = input("Enter starting node (A-F): ").upper()
target = input("Enter destination node (A-F): ").upper()

path = shortest_path(graph, start, target)

if path:
    print("Shortest path:", " -> ".join(path))
    print("Number of edges:", len(path) - 1)
else:
    print("No path found.")
