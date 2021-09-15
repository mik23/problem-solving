from binarytrees.data.Tree import Tree


def preOrderTraversing(T: Tree, result=None):
    if T is None:
        return

    if T.data is not None:
        # print(T.data)
        result.append(T.data)

    preOrderTraversing(T.left, result)
    preOrderTraversing(T.right, result)


def inOrderTraversing(T: Tree, result=None):
    if T is None:
        return

    inOrderTraversing(T.left, result)
    if T.data is not None:
        # print(T.data)
        result.append(T.data)

    inOrderTraversing(T.right, result)


def postOrderTraversing(T: Tree, result=None):
    if T is None:
        return

    postOrderTraversing(T.left, result)
    postOrderTraversing(T.right, result)
    if T.data is not None:
        # print(T.data)
        result.append(T.data)
