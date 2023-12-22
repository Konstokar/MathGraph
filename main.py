from MathGraph import *

graph = MathGraph()
print("Приступайте к работе")
while True:
    command = input("Введите команду: ")
    if command == "add vertex":
        graph.addVertex(input("Имя вершины: "))
    if command == "remove vertex":
        graph.removeVertex(input("Имя вершины: "))
    if command == "add edge":
        one = input("Имя первой вершины: ")
        two = input("Имя второй вершины: ")
        weight = float(input("Вес ребра (0 - если без веса): "))
        graph.addEdge(one, two, weight)
    if command == "remove edge":
        one = input("Имя первой вершины: ")
        two = input("Имя второй вершины: ")
        weight = float(input("Вес ребра (0 - если без веса): "))
        graph.removeEdge(one, two, weight)
    if command == "count vertex":
        print(graph.countVertex())
    if command == "count edges":
        print(graph.countEdges())
    if command == "weight":
        one = input("Имя первой вершины: ")
        two = input("Имя второй вершины: ")
        print(graph.weight(one, two))
    if command == "adjacent":
        one = input("Имя первой вершины: ")
        two = input("Имя второй вершины: ")
        print(graph.adjacent(one, two))
    if command == "cycle":
        print(graph.cycle())
    if command == "write":
        graph.writeToFile(input("Имя файла.расширение: "))
    if command == "read":
        graph.readFile(input("Имя файла.расширение: "))
    if command == "show":
        graph.show()
    if command == "remove graph":
        graph.removeGraph()
    if command == "help":
        graph.help(input("Название команды: "))
    if command == "exit":
        break
