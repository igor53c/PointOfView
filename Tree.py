from json import dumps
from typing import List


class Tree:
    def __init__(self, label: str, children: List["Tree"] = None):
        self.label = label
        self.children = children if children is not None else []
        self.parent = None
        for child in self.children:
            child.parent = self

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def find(self, label):
        if self.label == label:
            return self
        for child in self.children:
            result = child.find(label)
            if result is not None:
                return result
        return None

    def from_pov(self, from_node: str) -> "Tree":
        node = self.find(from_node)
        if node is None:
            raise ValueError("Tree could not be reoriented")

        new_root = Tree(node.label)

        def transform_tree(current, new_node, visited):
            visited.add(current.label)

            # Add the children of current node to the new node
            for child in current.children:
                if child.label not in visited:
                    child_copy = Tree(child.label)
                    new_node.children.append(child_copy)
                    transform_tree(child, child_copy, visited)

            # If the current node has a parent and it's not the target, transform it
            if current.parent and current.parent.label != from_node and current.parent.label not in visited:
                parent_copy = Tree(current.parent.label)
                new_node.children.append(parent_copy)
                transform_tree(current.parent, parent_copy, visited)

        transform_tree(node, new_root, set())
        return new_root

    def path_to(self, from_node: str, to_node: str) -> List[str]:
        start = self.find(from_node)
        end = self.find(to_node)
        if not start or not end:
            raise ValueError("No path found")

        path = []
        visited = set()

        def dfs(node, target):
            if node.label == target:
                path.append(node.label)
                return True
            visited.add(node.label)
            for child in node.children:
                if child.label not in visited and dfs(child, target):
                    path.append(node.label)
                    return True
            if node.parent and node.parent.label not in visited and dfs(node.parent, target):
                path.append(node.label)
                return True
            return False

        if dfs(start, to_node):
            return path[::-1]
        else:
            raise ValueError("No path found")
