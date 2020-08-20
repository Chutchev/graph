from behave import *


@then("Открыли окно")
def step_impl(context):
    context.open_window_graph.BFS(context)
    print("Открыли окно")


@then("Нашли {element}")
def step_impl(context, element):
    print(f"Нашли {element}")


@then("Нажали на кнопку")
def step_impl(context):
    print("Нашли кнопку")