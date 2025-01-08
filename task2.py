def is_connected(graph, n):
    visited = [False] * n

    def dfs(v):
        visited[v] = True
        for i in range(n):
            if graph[v][i] == 1 and not visited[i]:
                dfs(i)

    # Найти первый ненулевой элемент
    start = next((i for i in range(n) if any(graph[i])), None)
    if start is None:
        return True  # Граф пуст

    dfs(start)
    return all(visited[i] or not any(graph[i]) for i in range(n))


def find_eulerian_path(graph, n):
    degree = [sum(row) for row in graph]
    odd_vertices = [i for i in range(n) if degree[i] % 2 == 1]

    if len(odd_vertices) > 2:
        return False, []

    start = 0  # Начнем с любой вершины с ребрами
    if odd_vertices:
        start = odd_vertices[0]  # Если есть вершины с нечетным степенем, начинаем с одной из них

    stack = [start]
    path = []

    while stack:
        v = stack[-1]
        if degree[v] == 0:
            path.append(v)
            stack.pop()
        else:
            for u in range(n):
                if graph[v][u] == 1:
                    stack.append(u)
                    degree[v] -= 1
                    degree[u] -= 1
                    graph[v][u] = graph[u][v] = 0  # Удаляем ребро
                    break

    path.reverse()
    return True, path


def main(n, graph):
    if not is_connected(graph, n):
        print("Нет")
        return

    has_eulerian_circuit = all(sum(row) % 2 == 0 for row in graph)
    is_path, eulerian_path = find_eulerian_path(graph, n)

    if is_path:
        print("Да")
        if has_eulerian_circuit:
            print("Да")
        else:
            print("Нет")
        print(' '.join(str(x + 1) for x in eulerian_path))
    else:
        print("Нет")


n = 11
graph = [[0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
         [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
         [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
         [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
         [0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
         [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
         [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
         [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
         [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0]]
main(n, graph)
