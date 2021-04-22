from binarytrees.data.Tree import Tree

fifo = []


def breadthFirst(T: Tree, result: list):
    if T is not None and T.data is not None:
        print(T.data)
        result.append(T.data)

    if T.left is not None:
        fifo.append(T.left)

    if T.right is not None:
        fifo.append(T.right)

    if len(fifo) == 0:
        return

    head = fifo.pop(0)
    breadthFirst(head, result)
