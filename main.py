# Реализация стека с обработкой ошибок
class Stack:
    def __init__(self):
        # Инициализируем стек как пустой список
        self.items = []

    def is_empty(self):
        # Проверяем, пуст ли стек
        return len(self.items) == 0

    def push(self, item):
        # Добавляем элемент в конец списка, что является верхом стека
        self.items.append(item)

    def pop(self):
        # Удаляем и возвращаем элемент с вершины стека
        # Если стек пуст, выбрасываем исключение
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Попытка извлечь элемент из пустого стека")

    def peek(self):
        # Возвращаем элемент на вершине стека, но не удаляем его
        # Если стек пуст, возвращаем None
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        # Возвращаем количество элементов в стеке
        return len(self.items)

# Пример использования стека
stack = Stack()
stack.push(10)  # Добавляем элемент 10
stack.push(20)  # Добавляем элемент 20
stack.push(30)  # Добавляем элемент 30
print("Текущий стек:", stack.items)  # Вывод стека: [10, 20, 30]
print("Вершина стека:", stack.peek())  # Вершина стека: 30
stack.pop()  # Удаляем вершину стека (30)
print("Стек после pop:", stack.items)  # Стек после pop: [10, 20]


# Реализация очереди с обработкой ошибок
class Queue:
    def __init__(self):
        # Инициализируем очередь как пустой список
        self.items = []

    def is_empty(self):
        # Проверяем, пуста ли очередь
        return len(self.items) == 0

    def enqueue(self, item):
        # Добавляем элемент в начало списка (в конец очереди)
        self.items.insert(0, item)

    def dequeue(self):
        # Удаляем и возвращаем элемент с конца списка (начала очереди)
        # Если очередь пуста, выбрасываем исключение
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Попытка извлечь элемент из пустой очереди")

    def size(self):
        # Возвращаем количество элементов в очереди
        return len(self.items)

# Пример использования очереди
queue = Queue()
queue.enqueue("A")  # Добавляем элемент "A"
queue.enqueue("B")  # Добавляем элемент "B"
queue.enqueue("C")  # Добавляем элемент "C"
print("Текущая очередь:", queue.items)  # Вывод очереди: ['C', 'B', 'A']
queue.dequeue()  # Удаляем элемент "A" (FIFO)
print("Очередь после dequeue:", queue.items)  # Очередь после dequeue: ['C', 'B']


# Двоичное дерево поиска: добавление поиска и удаления узлов
class Node:
    def __init__(self, key):
        # Узел дерева содержит значение, а также ссылки на левого и правого потомков
        self.left = None
        self.right = None
        self.val = key

# Функция для вставки нового узла
def insert(root, key):
    # Если дерево пустое, создаем новый узел и возвращаем его
    if root is None:
        return Node(key)
    else:
        # Если значение ключа меньше текущего узла, рекурсивно вставляем в левое поддерево
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            # Если значение ключа больше или равно текущему, вставляем в правое поддерево
            root.left = insert(root.left, key)
    return root

# Функция для обхода дерева в симметричном порядке (in-order traversal)
def inorder(root):
    # In-order обходит дерево в следующем порядке: левое поддерево -> корень -> правое поддерево
    if root:
        inorder(root.left)  # Обход левого поддерева
        print(root.val, end=" ")  # Вывод значения текущего узла
        inorder(root.right)  # Обход правого поддерева

# Функция для поиска узла в дереве
def search(root, key):
    # Базовый случай: дерево пустое или ключ найден
    if root is None or root.val == key:
        return root

    # Если значение ключа меньше текущего узла, продолжаем искать в левом поддереве
    if root.val < key:
        return search(root.right, key)

    # Если значение ключа больше текущего узла, продолжаем искать в правом поддереве
    return search(root.left, key)

# Функция для нахождения минимального значения в дереве
def find_minimum(root):
    # Минимум в двоичном дереве поиска находится в самом левом узле
    while root.left:
        root = root.left
    return root

# Функция для удаления узла из дерева
def delete_node(root, key):
    # Если дерево пустое, возвращаем None
    if root is None:
        return root

    # Если ключ меньше текущего узла, продолжаем удаление в левом поддереве
    if key < root.val:
        root.left = delete_node(root.left, key)
    # Если ключ больше текущего узла, продолжаем удаление в правом поддереве
    elif key > root.val:
        root.right = delete_node(root.right, key)
    # Если ключ совпадает с текущим узлом, удаляем его
    else:
        # Если у узла нет левого поддерева, возвращаем правое
        if root.left is None:
            return root.right
        # Если у узла нет правого поддерева, возвращаем левое
        elif root.right is None:
            return root.left

        # Узел с двумя потомками: находим минимальное значение в правом поддереве
        temp = find_minimum(root.right)
        # Копируем минимальное значение в текущий узел
        root.val = temp.val
        # Удаляем минимальный узел из правого поддерева
        root.right = delete_node(root.right, temp.val)

    return root

# Пример использования дерева
root = Node(50)  # Создаем корень с ключом 50
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 60)
root = insert(root, 80)

print("Обход дерева (in-order):")
inorder(root)  # Вывод значений дерева: 20 30 40 50 60 70 80

print("\nПоиск узла с ключом 60:", search(root, 60))  # Найден узел с ключом 60

root = delete_node(root, 20)  # Удаляем узел с ключом 20
print("\nОбход дерева после удаления узла 20:")
inorder(root)  # Вывод значений после удаления: 30 40 50 60 70 80


# Граф: добавление поиска в глубину (DFS) и поиска в ширину (BFS)
class Graph:
    def __init__(self):
        # Граф представлен как словарь смежности, где ключ — вершина, а значение — список смежных вершин
        self.graph = {}

    def add_edge(self, u, v):
        # Добавляем ребро между вершинами u и v
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_graph(self):
        # Вывод графа в виде списка смежности
        for node in self.graph:
            print(f"{node} -> {', '.join(map(str, self.graph[node]))}")

    # Поиск в глубину (DFS) реализован рекурсивно
    def dfs(self, v, visited=None):
        # Инициализируем множество посещенных вершин
        if visited is None:
            visited = set()
        visited.add(v)
        print(v, end=" ")  # Выводим текущую вершину

        # Рекурсивно посещаем всех соседей текущей вершины
        for neighbor in self.graph.get(v, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    # Поиск в ширину (BFS) реализован с использованием очереди
    def bfs(self, start):
        visited = set()  # Множество для отслеживания посещенных вершин
        queue = [start]  # Инициализируем очередь начальной вершиной
        visited.add(start)

        # Пока очередь не пуста, продолжаем обход
        while queue:
            v = queue.pop(0)  # Извлекаем первую вершину из очереди
            print(v, end=" ")  # Выводим текущую вершину

            # Добавляем всех непосещенных соседей текущей вершины в очередь
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
g.print_graph()  # Вывод списка смежности

print("\nDFS (поиск в глубину) с вершины 2:")
g.dfs(2)  # DFS вывод: 2 0 1 3

print("\nBFS (поиск в ширину) с вершины 2:")
g.bfs(2)  # BFS вывод: 2 0 3 1
