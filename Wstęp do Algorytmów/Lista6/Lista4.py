from collections import deque


class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def bfs(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        print(node.data, end="->")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def dfs(root):
    if root is None:
        return

    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()
        print(node.data, end="->")

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


#      1
#     / \
#    2   3
#   / \ / \
#  4  5 6  7
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("BFS:")
bfs(root)
print("\nDFS:")
dfs(root)


def is_leaf(node):
    """Sprawdza, czy dany wierzchołek jest liściem."""
    return node.left is None and node.right is None


def create_subtree_from_leaf(leaf):
    """Tworzy nowe drzewo binarne, gdzie zadany liść jest korzeniem."""
    if leaf is None or not is_leaf(leaf):
        return None
    return Node(data=leaf.data)


leaf = root.left.left  # Liść, który będzie korzeniem nowego drzewa

new_tree = create_subtree_from_leaf(leaf)
##########################################################


def print_tree(root, level=0):
    """Funkcja wyświetlająca drzewo binarne w formie poziomej."""
    if root is not None:
        print_tree(root.right, level + 1)
        print("    " * level + str(root.data))
        print_tree(root.left, level + 1)


# Tworzenie drzewa binarnego czteropoziomowego niepełnego
# Poziomy:  1         2           3             4
#          1
#         / \
#        2   3
#       / \   \
#      4   5   6
#     /       / \
#    7       8   9
#               /
#              10
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.left.left = Node(7)
root.right.right.left = Node(8)
root.right.right.right = Node(9)
root.right.right.right.left = Node(10)

# Wyświetlanie drzewa binarnego
print("Drzewo binarne:")


# print_tree(root)
def level_order_traversal(root):
    """Przechodzenie drzewa w porządku poziomowym i wyświetlanie liczby węzłów na każdym poziomie."""
    if root is None:
        return

    queue = [(root, 1)]  # Krotki (węzeł, poziom)
    level_count = {}
    leaf_count = 0

    while queue:
        node, level = queue.pop(0)
        if level not in level_count:
            level_count[level] = 1
        else:
            level_count[level] += 1

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

        if node.left is None and node.right is None:
            leaf_count += 1

    print("Liczba węzłów na każdym poziomie:")
    for level, count in level_count.items():
        print(f"Poziom {level}: {count}")

    print("Liczba liści:", leaf_count)


# Wyświetlanie liczby węzłów na każdym poziomie i liczby liści w drzewie
level_order_traversal(root)


def shortest_path_to_leaf(root):
    """Wyznaczanie długości najkrótszej ścieżki od korzenia do liścia oraz wyświetlanie liści na tej głębokości."""
    if root is None:
        return []

    shortest_path = []

    def dfs(node, path):
        if node is None:
            return
        path.append(node.data)
        if node.left is None and node.right is None:
            shortest_path.append(path.copy())
        else:
            dfs(node.left, path)
            dfs(node.right, path)
        path.pop()

    dfs(root, [])

    print(shortest_path)
    shortest_length = float("inf")
    shortest_leaf_path = None
    for path in shortest_path:
        if len(path) < shortest_length:
            shortest_length = len(path)
            shortest_leaf_path = path

    print("Długość najkrótszej ścieżki od korzenia do liścia:", len(shortest_leaf_path))
    print("Liście na tej głębokości:", shortest_leaf_path)


# Wyznaczanie długości najkrótszej ścieżki od korzenia do liścia oraz wyświetlanie liści na tej głębokości
shortest_path_to_leaf(root)
