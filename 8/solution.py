#!/usr/bin/python3

# read input
input = list(map(int, open('input.txt').readline().split(' ')))


class Node(object):
    def __init__(self, parent=None):
        self.parent = None
        self.children = []
        self.meta = []

    def add_meta(self, meta):
        self.meta = meta

    def add_child(self):
        new_child = Node(parent=self)
        self.children.append(new_child)
        return new_child

    def sum_meta(self):
        return sum(self.meta) + sum(map(Node.sum_meta, self.children))

    def value(self):
        if not self.children:
            return(sum(self.meta))
        val = 0
        for i in [j for j in self.meta if j > 0 and j <= len(self.children)]:
            child = self.children[i - 1]
            val += child.value()
        return val


    def __str__(self):
        if not self.children:
            return str(self.meta)
        return '{meta} <{children}>'.format(meta=self.meta, children=', '.join(map(str, self.children)))


def add_subtree(input, node):
    nc = input[0]
    nm = input[1]
    if nc == 0:
        data = input[2:(2 + nm)]
        node.add_meta(data)
        return 2 + nm
    else:
        off = 0
        for i in range(nc):
            off += add_subtree(input[2 + off:], node.add_child())
        data = input[(2 + off) : (2 + off + nm)]
        node.add_meta(data)
        return 2 + off + nm


if __name__ == '__main__':
    root = Node()
    add_subtree(input, root)
    # part 1
    print(root.sum_meta())
    # part 2
    print(root.value())