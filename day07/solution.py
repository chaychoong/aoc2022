from typing import List


class Node:
    def __init__(self, name: str, parent: "Node"):
        self.name = name
        self.parent = parent
        self.size = None

    def add_child(self, _) -> None:
        raise NotImplementedError

    def get_size(self):
        raise NotImplementedError

    def get_path(self):
        if self.parent is None:
            return self.name

        return self.parent.get_path() + "/" + self.name


class File(Node):
    def __init__(self, name: str, parent: "Directory", size: int):
        super().__init__(name, parent)
        self.size = size

    def get_size(self):
        return self.size


class Directory(Node):
    def __init__(self, name: str, parent: "Directory"):
        super().__init__(name, parent)
        self.children = []

    def add_child(self, child: Node) -> None:
        self.children.append(child)

    def get_size(self):
        if len(self.children) == 0:
            return 0

        if self.size is not None:
            return self.size

        # loop through all children and add their size
        return sum(child.get_size() for child in self.children)

    def traverse_and_get_all_directories_in_child(self) -> List["Directory"]:
        directories = []
        for child in self.children:
            if isinstance(child, Directory):
                directories.append(child)
                directories.extend(child.traverse_and_get_all_directories_in_child())

        return directories


def create_node(context: Directory, description: str) -> None:
    node_type, node_name = description.split(" ")

    # directories are in the form "dir <name>"
    if node_type == "dir":
        context.children.append(Directory(node_name, context))

    # files are in the form "<size> <name>"
    else:
        size = int(node_type)
        context.children.append(File(node_name, context, size))


def build_tree(input: List[str]) -> int:
    # create a root directory
    root = Directory("", None)

    current_directory = root
    ls_dir = None
    for line in input:
        split_input = line.split(" ")
        if split_input[0] != "$":
            create_node(ls_dir, line)

        # each instruction line starts with "$"
        else:
            # implement cd
            # each line is in the form "$ cd <dir_name>"
            # use python's new match statement
            match split_input[1]:
                case "cd":
                    match split_input[2]:
                        # cd ..
                        case "..":
                            current_directory = current_directory.parent

                        # cd /
                        case "/":
                            current_directory = root

                        # cd <dir_name>
                        case _:
                            for child in current_directory.children:
                                if child.name == split_input[2]:
                                    current_directory = child
                                    break

                # implement ls
                # each line is in the form "$ ls"
                case "ls":
                    if len(split_input) == 2:
                        ls_dir = current_directory
                    else:
                        ls_dir = split_input[2]

    return root


def solution_p1(input: List[str]) -> int:
    root = build_tree(input)

    # traverse root and return a list of all directories
    dir_list = root.traverse_and_get_all_directories_in_child()

    # return the sum of all directories, filtered by size < 100000
    return sum(dir.get_size() for dir in dir_list if dir.get_size() < 100000)


def solution_p2(input: List[str]) -> int:
    root = build_tree(input)

    # get total size of root
    total_size = root.get_size()

    size_required = total_size - 40000000

    # traverse root and return a list of all directories
    dir_list = root.traverse_and_get_all_directories_in_child()

    # find the directory with the min size, above size_required
    return min(dir.get_size() for dir in dir_list if dir.get_size() > size_required)
