from rich.tree import Tree
from rich import print as rprint
from os import getcwd, listdir

tree = Tree(":file_folder: Rich Tree")
tree.add("foo")
tree.add(":white_heavy_check_mark:bar")
rprint(tree)
rprint(getcwd())
rprint(listdir())
