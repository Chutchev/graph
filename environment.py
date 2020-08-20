from graph import Graph
from node import Node


def before_all(context):
    do = Node("Then Открыли окно")
    result = Node("Then Нажали на кнопку")
    button = Node("Then Нашли кнопку", ways=[result])
    text = Node("Then Нашли текст", ways=[result])
    do.add_ways(button, text)
    graph = Graph(do, button, text, result)
    context.open_window_graph = graph
    print("Тест графа начался")

def before_scenario(context, scenario):
    print("Сценарий пошел")

def after_scenario(context, scenario):
    print("Сценарий кончился")

def adter_all(context):
    print("Тест графа кончился")