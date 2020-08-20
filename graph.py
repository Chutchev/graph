import collections


class Graph:

    def __init__(self, *args, graph=None, name='Graph'):
        self.name = name
        self.nodes = list(args)
        if graph:
            for node in graph:
                self.nodes.append(node)
        self.i = 0

    def __repr__(self):
        stroke = ""
        for node in self.nodes:
            stroke += f"{node}, ways: {node.ways()}"
        return f"{self.name}\nNodes: {self.nodes}"

    def __iter__(self):
        while True:
            if self.i < len(self.nodes):
                yield self.nodes[self.i]
                self.i += 1
            else:
                break

    def __next__(self):
        pass

    def BFS(self, context):
        """
        Обход графа в ширину
        :return:
        """
        visited, queue = set(), collections.deque([self.nodes[0]])
        visited.add(self.nodes[0])
        while queue:
            node = queue.popleft()
            print(f'I on {node}, my ways to {node.ways()}')
            for neighbour in node.ways():
                if neighbour not in visited:
                    print(f"I'm going to {neighbour}")
                    visited.add(neighbour)
                    queue.append(neighbour)



