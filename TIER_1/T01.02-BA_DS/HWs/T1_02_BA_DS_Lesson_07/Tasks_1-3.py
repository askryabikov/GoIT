class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):                # shows tree in string (recursive)
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def get_height(node):                                            # Return 0 for empty subtree, otherwise stored height
    if not node:
        return 0
    return node.height


def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def left_rotate(z):                                              # Perform left rotation around node z
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))  # Update heights
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y


def right_rotate(y):                                             # Perform right rotation around node y
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))  # Update heights
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x


def min_value_node(node):                                        # Return the node with the minimum key in this subtree:
    current = node
    while current.left is not None:
        current = current.left
    return current


def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))  # update height

    balance = get_balance(root)

    # 1. Left Left Case
    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    # 2. Left Right Case
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # 3. Right Right Case
    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    # 4. Right Left Case
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def delete_node(root, key):
    if not root:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:               # Node with one child or no child
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children: get inorder successor (min in right subtree)
        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)

    if root is None:
        return root

    # Update height and rebalance:
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    # 1. Left Left Case
    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)

    # 2. Left Right Case
    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # 3. Right Right Case
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)

    # 4. Right Left Case
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


# Task 1 - Return the maximum key in a BST/AVL tree (the right-most node)

def max_value_node(node):
    current = node
    while current.right is not None:
        current = current.right
    return current

def find_max(root):
    if root is None:
        return None
    return max_value_node(root).key


# Task 2 - Find minimum value in AVL (the left-most node)

def find_min(root):
    if root is None:
        return None
    return min_value_node(root).key


# Task 3 - Sum of all values in AVL

def sum_values(root):            # Recursive
    if root is None:
        return 0
    return root.key + sum_values(root.left) + sum_values(root.right)


# Driver program to test the above functions

root = None
keys = [10, 20, 30, 25, 28, 27, -1]

for key in keys:
    root = insert(root, key)
    print("Inserted:", key)
    print("AVL Tree:")
    print(root)

print("Max value:", find_max(root))
print("Min value:", find_min(root))
print("Sum of all values:", sum_values(root))

# Delete
keys_to_delete = [10, 27]
for key in keys_to_delete:
    root = delete_node(root, key)
    print("Deleted:", key)
    print("AVL Tree:")
    print(root)

print("Max value after deletions:", find_max(root))
print("Min value after deletions:", find_min(root))
print("Sum after deletions:", sum_values(root))