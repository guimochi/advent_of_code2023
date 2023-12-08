import time

start_time = time.time()

START_NODE = 'AAA'
FINAL_NODE = 'ZZZ'

class Noeud:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def give_next(self, char):
        if char == 'L':
            return self.left
        if char == 'R':
            return self.right


def get_start(input, nodes, depart):
    noeud = depart
    for c in input:
        noeud = nodes[noeud].give_next(c)
    return noeud


def get_path(start_node, nodes):
    all_path = [['L', nodes[start_node].left], ['R', nodes[start_node].right]]
    while True:
        new_paths = []
        for path in all_path:
            path_left = path[0] + 'L'
            node_left = nodes[path[1]].left
            if node_left == 'ZZZ':
                return path_left
            new_paths.append([path_left, node_left])
            path_right = path[0] + 'R'
            node_right = nodes[path[1]].right
            if node_right == 'ZZZ':
                return path_right
            new_paths.append([path_right, node_right])
        all_path = new_paths
    return None


def get_length_path(input, start_node, nodes):
    node = start_node
    count = 0
    while True:
        for c in input:
            node = nodes[node].give_next(c)
            count += 1
            if node == FINAL_NODE:
                return count
    return 0


with open('input.txt', 'r') as f:
    lines = f.readlines()
    input = lines[0][:-1]
    nodes = {}
    # create nodes
    for line in lines[2:]:
        node = line.split(' = ')[0]
        left, right = line.split(' = ')[1].strip('(').replace(')', "").strip().split(', ')
        noeud = Noeud(node, left, right)
        nodes[node] = noeud
    # get start
    start_node = get_start(input, nodes, 'AAA')
    length = len(input)
    if start_node == 'ZZZ':
        print(length)
        exit(0)
    final_path = get_length_path(input, start_node, nodes)
    print(length + final_path)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"The code took {elapsed_time} seconds to run.")
