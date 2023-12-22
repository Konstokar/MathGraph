class MathGraph:

    def __init__(self):
        self.graph = dict()

    def removeGraph(self):
        self.graph.clear()
        return 0

    def addVertex(self, vertex):
        if vertex not in self.graph.keys():
            self.graph[vertex] = []
        else:
            return 1
        return 0

    def removeVertex(self, vertex):
        if vertex in self.graph:
            self.graph.pop(vertex, None)
            keys = self.graph.keys()
            for x in keys:
                for y in self.graph[x]:
                    if vertex in y:
                        self.graph[x].remove(y)
        else:
            return 1
        return 0

    def addEdge(self, vertex1, vertex2, weight):
        try:
            self.graph[vertex1].append((vertex2, float(weight)))
            self.graph[vertex2].append((vertex1, float(weight)))
        except Exception:
            return 1
        return 0

    def removeEdge(self, vertex1, vertex2, weight):
        try:
            self.graph[vertex1].remove((vertex2, float(weight)))
            self.graph[vertex2].remove((vertex1, float(weight)))
        except Exception:
            return 1
        return 0

    def countVertex(self):
        return len(self.graph)

    def countEdges(self):
        new_graph = {}
        for vertex in self.graph.keys():
            new_graph[vertex] = []
            for end in self.graph[vertex]:
                new_graph[vertex].append(end[0])
        return sum(len(new_graph[node]) for node in new_graph) // 2

    def weight(self, vertex1, vertex2):
        edges = self.graph[vertex1]
        for edge in edges:
            if edge[0] == vertex2:
                return edge[1]
        return -1

    def adjacent(self, vertex1, vertex2):
        edges = self.graph[vertex1]
        for edge in edges:
            if edge[0] == vertex2:
                return True
        return False

    def dfs(self, graph, node, visited, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if self.dfs(graph, neighbor, visited, node):
                    return True
            elif parent != neighbor:
                return True
        return False

    def cycle(self):
        new_graph = {}
        for vertex in self.graph.keys():
            new_graph[vertex] = []
            for end in self.graph[vertex]:
                new_graph[vertex].append(end[0])
        visited = set()
        for node in new_graph.keys():
            if node not in visited:
                if self.dfs(new_graph, node, visited, None):
                    return True
        return False

    def writeToFile(self, file_name):
        file = open(file_name, "w")
        file.write(str(len(self.graph.keys())) + "\n")
        for vertex in self.graph.keys():
            file.write(vertex + " : ")
            for end in self.graph[vertex]:
                file.write(str(end[0]) + " " + str(end[1]) + " | ")
            file.write("\n")
        file.close()
        return 0

    def readFile(self, file_name):
        file = open(file_name, "r")
        count = int(file.readline())
        for i in range(count):
            string = file.readline()
            key = string[0]
            values = string[4:].split("|")
            del values[-1]
            self.graph[key] = []
            for val in values:
                val1 = val.split()
                self.graph[key].append((val1[0], float(val1[1])))
        self.show()
        file.close()
        return 0

    def show(self):
        for vertex in self.graph.keys():
            output = vertex + ": "
            for end in self.graph[vertex]:
                output += " ".join([end[0], str(end[1])])
                output += ", "
            print(output[:-2])
        return 0

    def help(self, name):
        match name:
            case "add vertex":
                print("Добавление вершины в граф")
            case "remove vertex":
                print("Удаление вершины из графа")
            case "add edge":
                print("Добавление ребра в граф")
            case "remove edge":
                print("Удаление ребра из графа")
            case "count vertex":
                print("Количество вершин в графе")
            case "count edges":
                print("Количество рёбер в графе")
            case "weight":
                print("Вес ребра")
            case "adjacent":
                print("Смежны ли вершины")
            case "write":
                print("Запись графа в файл")
            case "read":
                print("Чтение графа из файла")
            case "show":
                print("Вывод графа на экран")
            case "cycle":
                print("Есть ли цикл в графе")
            case "remove graph":
                print("Полная очистка графа")
            case "exit":
                print("Завершение работы")