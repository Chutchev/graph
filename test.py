from node import Node
from graph import Graph


if __name__ == '__main__':
    # Ниже  просто ноды для графа
    open_programm = Node("Open Programm")
    openned = Node("Openned")
    title = Node("title")
    button = Node("button")
    label = Node("label")
    passed = Node("Scenario passed")
    # Расставляю пути нод
    open_programm.add_ways(openned, title)
    openned.add_ways(title, button, label)
    title.add_ways(button, label)
    button.add_ways(passed)
    label.add_ways(passed)
    # graph - это граф для проверки открытия окна
    graph = Graph(open_programm, openned, title, button, label, passed, name="Проверка открытия окна!")
    # graph1 - сценарий Открываем окно
    graph1 = Graph(title, button, graph=graph, name="Открываем окно")
    # .BFS() - обход графа в Ширину. Пройдет все шаги внутри графа
    graph1.BFS()