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


def create_tree():
    root = Node("/", None)

    with open("day_7.txt") as file:
        for each_line in file:
            line = each_line.rstrip()

            if line == "$ cd /":
                current_node = root

            elif "$ cd" in line:
                dir_name = re.search("\\$ cd (.*)", line).group(1)

                if dir_name == "..":
                    current_node = current_node.parent
                else:
                    current_node = current_node.get_child(dir_name)

            elif "dir" in line[:3]:
                folder = re.search("dir (.*)", line).group(1)
                current_node.child_dirs.append(Node(folder, current_node))

            elif "$ ls" in line:
                continue

            else:
                file_size = re.findall(r"\d+", line)[0]
                current_node.file_size += int(file_size)

                traverse = current_node.parent
                while traverse is not None:
                    traverse.file_size += int(file_size)
                    traverse = traverse.parent

    return root


def part_1(node):
    rec_sum = 0

    if node.file_size < 100000:
        rec_sum += node.file_size

    for child in node.child_dirs:
        rec_sum += part_1(child)

    return rec_sum


def part_2(node, value, goal):
    if goal <= node.file_size < value:
        value = node.file_size

    for child in node.child_dirs:
        value = part_2(child, value, goal)

    return value


def main():

    # Create a tree structure for the files and folders
    # The same tree will be used for part 1 and 2
    root = create_tree()

    p1 = part_1(root)
    print(p1)

    space_req = root.file_size - 40000000
    p2 = part_2(root, root.file_size, space_req)
    print(p2)


if __name__ == "__main__":
    main()
