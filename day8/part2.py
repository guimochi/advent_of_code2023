import time

start_time = time.time()

START_NODE_LETTER = 'A'
FINAL_NODE_LETTER = 'Z'

# Create noeud with left right attribute
class Noeud:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


    # Gives the corresponding node depending on the letter provided
    def give_next(self, char):
        if char == 'L':
            return self.left
        if char == 'R':
            return self.right

def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def ppcm(a, b):
    return a * b // pgcd(a, b)

def ppcm_liste(nombres):
    resultat = nombres[0]
    for nombre in nombres[1:]:
        resultat = ppcm(resultat, nombre)
    return resultat

# return the number of chr in input used and the last node it was on
def get_length_path(input, start_nodes, map_node_noeud):
    current_nodes = start_nodes
    count = 0
    i = 0
    while True:
        for c in input:
            reached = 0
            new_nodes = []
            for node in current_nodes:
                new_node = map_node_noeud[node].give_next(c)
                if new_node[2] == FINAL_NODE_LETTER:
                    reached += 1
                new_nodes.append(new_node)
            count += 1
            if reached == 5 or reached == 6:
                print(reached)
            if reached == len(new_nodes):
                return count, new_node
            current_nodes = new_nodes

    return 0

# in the code, I will refer the class as Noeud and the 3 letter as node
def get_cycle(input, node, map_node_noeud):
    first_find, node = get_length_path(input, [node], map_node_noeud)
    cycle_len = get_length_path(input, [node], map_node_noeud)
    return first_find
    # return first_find, cycle_len[0]
    pass


def get_cycles(input, start_nodes, map_node_noeud):
    return [get_cycle(input,node, map_node_noeud) for node in start_nodes]


with open('input.txt', 'r') as f:
    lines = f.readlines()
    input = lines[0][:-1]
    map_node_noeud = {}
    start_nodes = []
    # create map and get all starting nodes
    for line in lines[2:]:
        node = line.split(' = ')[0]
        left, right = line.split(' = ')[1].strip('(').replace(')', "").strip().split(', ')
        noeud = Noeud(node, left, right)
        map_node_noeud[node] = noeud
        if node[2] == START_NODE_LETTER:
            start_nodes.append(node)


    cycles = get_cycles(input, start_nodes, map_node_noeud)

    print(ppcm_liste(cycles))


    # final_path = get_length_path(input, start_nodes, map_node_noeud)
    # print(final_path)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"The code took {elapsed_time} seconds to run.")
