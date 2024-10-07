# Реализация стека с обработкой ошибок
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Попытка извлечь элемент из пустого стека")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

# Пример использования стека
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Текущий стек:", stack.items)  # Вывод: [10, 20, 30]
print("Вершина стека:", stack.peek())  # Вывод: 30
stack.pop()
print("Стек после pop:", stack.items)  # Вывод: [10, 20]


# Реализация очереди с обработкой ошибок
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Попытка извлечь элемент из пустой очереди")

    def size(self):
        return len(self.items)

# Пример использования очереди
queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
print("Текущая очередь:", queue.items)  # Вывод: ['C', 'B', 'A']
queue.dequeue()
print("Очередь после dequeue:", queue.items)  # Вывод: ['C', 'B']


# Двоичное дерево поиска: добавление поиска и удаления узлов
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Функция для вставки нового узла
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# Функция для обхода дерева в симметричном порядке (in-order traversal)
def inorder(root):
    if root:
        # Сначала обходим левое поддерево
        inorder(root.left)
        # Выводим значение текущего узла
        print(root.val, end=" ")
        # Затем обходим правое поддерево
        inorder(root.right)

# Функция для поиска узла в дереве
def search(root, key):
    if root is None or root.val == key:
        return root

    if root.val < key:
        return search(root.right, key)

    return search(root.left, key)

# Функция для нахождения минимального значения в дереве (нужно для удаления)
def find_minimum(root):
    while root.left:
        root = root.left
    return root

# Функция для удаления узла в дереве
def delete_node(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp = find_minimum(root.right)
        root.val = temp.val
        root.right = delete_node(root.right, temp.val)

    return root

# Пример использования дерева
root = Node(50)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 60)
root = insert(root, 80)

print("Обход дерева (in-order):")
inorder(root)  # Вывод: 20 30 40 50 60 70 80

print("\nПоиск узла с ключом 60:", search(root, 60))  # Найденный узел

root = delete_node(root, 20)
print("\nОбход дерева после удаления узла 20:")
inorder(root)  # Вывод: 30 40 50 60 70 80


# Граф: добавление поиска в глубину (DFS) и поиска в ширину (BFS)
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_graph(self):
        for node in self.graph:
            print(f"{node} -> {', '.join(map(str, self.graph[node]))}")

    # Поиск в глубину (DFS)
    def dfs(self, v, visited=None):
        if visited is None:
            visited = set()
        visited.add(v)
        print(v, end=" ")

        for neighbor in self.graph.get(v, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    # Поиск в ширину (BFS)
    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            v = queue.pop(0)
            print(v, end=" ")

            for neighbor in self.graph.get(v, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

# Пример использования графа
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("\nГраф (список смежности):")
g.print_graph()

print("\nDFS (поиск в глубину) с вершины 2:")
g.dfs(2)  # Вывод: 2 0 1 3

print("\nBFS (поиск в ширину) с вершины 2:")
g.bfs(2)  # Вывод: 2 0 3 1
