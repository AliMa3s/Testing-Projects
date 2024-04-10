import heapq

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def astar(maze, start, end):
    start_node = Node(None, start)
    end_node = Node(None, end)
    open_list = []
    closed_list = []
    heapq.heappush(open_list, (start_node.f, 0, start_node))  # Initial push with tiebreaker 0
    tiebreaker = 1  # Initialize tiebreaker

    while open_list:
        current_node = heapq.heappop(open_list)[2]  # Adjust index to get Node
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node  # Initialize current with current_node for path tracing
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]


        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) - 1) or node_position[1] < 0:
                continue
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            new_node = Node(current_node, node_position)

            for closed_child in closed_list:
                if new_node == closed_child:
                    continue

            new_node.g = current_node.g + 1
            new_node.h = ((new_node.position[0] - end_node.position[0]) ** 2) + ((new_node.position[1] - end_node.position[1]) ** 2)
            new_node.f = new_node.g + new_node.h

            if any(child[2] == new_node and child[0] <= new_node.f for child in open_list):
                continue

            heapq.heappush(open_list, (new_node.f, tiebreaker, new_node))
            tiebreaker += 1  # Increment tiebreaker for next node

maze = [[0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]]

start = (0, 0)
end = (4, 4)

path = astar(maze, start, end)
print(path)
