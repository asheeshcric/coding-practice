class Node:
    # This represents a node in the graph or grid along with its state
    def __init__(self, position=None, parent=None):
        self.position = position
        self.parent = parent
        # These are the cost functions for the node
        # G: Distance from start node
        # H: Distance from this node to end node (heuristics)
        # F: Total cost -- (G+H)
        self.G = 0
        self.H = 0
        self.F = 0

    def __eq__(self, other):
        return self.position == other.position


def get_euclidean(node1, node2):
    dist = abs(node1.position[0]-node2.position[0]) + \
        abs(node1.position[1]-node2.position[1])
    return dist


def a_star(maze, start_pos, end_pos):
    open_list, closed_list = [], []

    start_node = Node(position=start_pos, parent=None)
    end_node = Node(position=end_pos, parent=None)

    # Add the start node to the open list
    open_list.append(start_node)

    while len(open_list) > 0:
        # Get current node from the open list that has the least f cost (from start node)
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.F < current_node.F:
                current_index, current_index = item, index

        # Remove the current node from open list and add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Check for goal
        if current_node == end_node:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            # Return path in reversed order
            return path[::-1]

        # Look for neighbor nodes
        children = []
        for next_pos in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]:
            node_pos = (
                current_node.position[0]+next_pos[0], current_node.position[1]+next_pos[1])

            # Check if the next node position is within the maze range
            if node_pos[0] not in range(len(maze)) or node_pos[1] not in range(len(maze[0])):
                # i.e. neighbor position indices out of range than the maze
                continue

            # Also, check if the neighbor is a walkable node or node (i.e. not an obstacle (==1))
            if maze[node_pos[0]][node_pos[1]] != 0:
                continue

            next_node = Node(position=node_pos, parent=current_node)
            children.append(next_node)

        # Now, loop through the children and find their distances G, H and F
        for child in children:
            # Make sure child is not in the closed list
            is_closed = any([child == closed for closed in closed_list])
            if is_closed:
                continue

            # G is the actual cost from the current node which is always one greater in an unweighted graph
            child.G = current_node.G + 1
            # H is the heuristic (Euclidean distance from current to end node)
            child.H = get_euclidean(child, end_node)
            # F = G + H
            child.F = child.G + child.H

            # Add child to open list if it does not exist
            is_open = any([child == open_node for open_node in open_list])
            if not is_open:
                open_list.append(child)


if __name__ == '__main__':
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start_pos = (0, 0)
    end_pos = (7, 6)

    path = a_star(maze, start_pos, end_pos)
    print(path)
