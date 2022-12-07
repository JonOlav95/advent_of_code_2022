import re


class Node:

    def __init__(self, name, parent):
        self.parent = parent
        self.name = name
        self.child_dirs = []
        self.file_size = 0

    def get_child(self, name):
        for c in self.child_dirs:
            if c.name == name:
                return c

    # Not needed -- never False
    def child_exist(self, name):
        for c in self.child_dirs:
            if c.name == name:
                return True

        return False


def create_tree():
    root = Node("/", None)
    current_node = root

    with open("day_7.txt") as file:
        for each_line in file:
            line = each_line.rstrip()

            if line == "$ cd /":
                continue

            if "$ cd" in line:
                dir_name = re.search("\\$ cd (.*)", line).group(1)

                if dir_name == "..":
                    current_node = current_node.parent
                else:
                    current_node = current_node.get_child(dir_name)

            elif "$ ls" in line:
                continue

            else:
                if "dir" in line[:3]:
                    folder = re.search("dir (.*)", line).group(1)

                    if not current_node.child_exist(folder):
                        current_node.child_dirs.append(Node(folder, current_node))

                else:
                    file_size = re.findall(r"\d+", line)[0]
                    current_node.file_size += int(file_size)

                    tmp = current_node.parent
                    while tmp is not None:
                        tmp.file_size += int(file_size)
                        tmp = tmp.parent

    return root


def part_1(node):
    zum = 0

    if node.file_size < 100000:
        zum += node.file_size

    for child in node.child_dirs:
        zum += part_1(child)

    return zum


def part_2(node, value, goal):

    if goal <= node.file_size < value:
        value = node.file_size

    for child in node.child_dirs:
        value = part_2(child, value, goal)

    return value


def main():
    root = create_tree()

    p1 = part_1(root)
    print(p1)

    space_req = 30000000 - (70000000 - root.file_size)
    p2 = part_2(root, 70000000, space_req)
    print(p2)


if __name__ == "__main__":
    main()
