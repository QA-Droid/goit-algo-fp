import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, highlight_nodes=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_heap_tree(array, index=0):
    """Побудова дерева з масиву."""
    if index >= len(array):
        return None

    node = Node(array[index])
    node.left = build_heap_tree(array, 2 * index + 1)
    node.right = build_heap_tree(array, 2 * index + 2)
    return node

def color_generator(steps):
    for i in range(steps):
        intensity = int(255 * i / steps)
        yield f'#{intensity:02x}{96:02x}{240:02x}'

def dfs(node, colors, step=0):
    if node is None:
        return

    node.color = next(colors)
    draw_tree(heap_root)

    dfs(node.left, colors, step + 1)
    dfs(node.right, colors, step + 1)

def bfs(root):
    queue = deque([root])
    colors = color_generator(len(heap_array))

    while queue:
        node = queue.popleft()

        node.color = next(colors)
        draw_tree(heap_root)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

heap_array = [10, 15, 30, 40, 50, 100, 40]
heap_root = build_heap_tree(heap_array)

print("DFS обхід:")
dfs(heap_root, color_generator(len(heap_array)))

print("BFS обхід:")
bfs(heap_root)
