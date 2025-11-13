class Component:
    def operation(self):
        pass
class Leaf(Component):
    def __init__(self, name):
        self.name = name
    def operation(self):
        return f"Leaf {self.name}"
class Composite(Component):
    def __init__(self, name):
        self.name = name
        self._children = []
    def add(self, component):
        self._children.append(component)
    def operation(self):
        results = [child.operation() for child in self._children]
        return f"Composite {self.name} ({', '.join(results)})"
# Client code
leaf1 = Leaf("A")
leaf2 = Leaf("B")
composite1 = Composite("C")
composite1.add(leaf1)
composite1.add(leaf2)
print(composite1.operation())
