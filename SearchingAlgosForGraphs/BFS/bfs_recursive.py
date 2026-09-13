from collections import deque
from typing import Hashable, Iterable, Mapping, TypeVar


Node = TypeVar("Node", bound=Hashable)


class RecursiveBFS:
    """Traverse a graph breadth-first by recursively processing a queue."""

    def __init__(self, graph: Mapping[Node, Iterable[Node]]):
        self.graph = graph
        self.visited: set[Node] = set()
        self.order: list[Node] = []

    def _print_tree(self, root: Node) -> None:
        print("Tree diagram:")

        def render(node: Node, ancestors: set[Node]) -> tuple[list[str], int, int]:
            label = str(node)
            if node in ancestors:
                label = f"{label} [cycle]"
                return [label], len(label), len(label) // 2

            children = list(self.graph.get(node, []))
            if not children:
                return [label], len(label), len(label) // 2

            rendered_children = [render(child, ancestors | {node}) for child in children[:2]]
            if len(rendered_children) == 1:
                child_lines, child_width, child_center = rendered_children[0]
                root_center = child_center
                width = max(len(label), child_width, root_center + 1)
                lines = [label.center(width), "/".center(width)]
                lines.extend(line.center(width) for line in child_lines)
                return lines, width, root_center

            left_lines, left_width, left_center = rendered_children[0]
            right_lines, right_width, right_center = rendered_children[1]
            gap = 3
            right_offset = left_width + gap
            right_center += right_offset
            width = right_offset + right_width
            root_center = (left_center + right_center) // 2
            root_start = max(0, root_center - len(label) // 2)
            first_line = (" " * root_start + label).ljust(width)
            edge_line = [" "] * width
            edge_line[left_center] = "/"
            edge_line[right_center] = "\\"
            lines = [first_line, "".join(edge_line)]
            child_height = max(len(left_lines), len(right_lines))
            for index in range(child_height):
                left_line = left_lines[index] if index < len(left_lines) else ""
                right_line = right_lines[index] if index < len(right_lines) else ""
                lines.append(left_line.ljust(left_width) + " " * gap + right_line)
            return lines, width, root_center

        for line in render(root, set())[0]:
            print(line.rstrip())

    def bfs_recursive(self, queue: deque[Node]) -> None:
        if not queue:
            return

        current = queue.popleft()
        self.order.append(current)
        print(f"\nCurrent node: {current}")

        neighbors = list(self.graph.get(current, []))
        print(f"Tree being considered: {current} -> {neighbors}")

        for neighbor in neighbors:
            if neighbor not in self.visited:
                self.visited.add(neighbor)
                queue.append(neighbor)
                print(f"Queued {neighbor} for later processing")

        self.bfs_recursive(queue)

    def traverse(self, start: Node) -> list[Node]:
        self.visited = {start}
        self.order = []
        self._print_tree(start)
        print(f"Starting BFS from: {start}")
        self.bfs_recursive(deque([start]))
        print(f"\nTraversal order: {self.order}")
        return self.order


if __name__ == "__main__":
    tree = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": [],
        "F": [],
    }

    RecursiveBFS(tree).traverse("A")