class Node:
    from_node = list()

    def __init__(self, name, *args, **kwargs):
        self.name = name
        self._ways = list()
        ways = kwargs.get('ways')
        if ways:
            self.add_ways(*ways)

    def add_ways(self, *args):
        self._ways+=args

    def ways(self):
        if self._ways:
            return self._ways
        return []

    def __repr__(self):
        return f"Node {self.name}"
