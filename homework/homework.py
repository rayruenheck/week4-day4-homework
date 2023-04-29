from BST import BinarySearchTree


    
def convert_to_bst(func):
    def wrapper(alist):
        node = BinarySearchTree(alist[0])
        for e in alist[1:]:
            node.add_node(e)
        func(node)
    return wrapper

@convert_to_bst
def print_bst_list(alist):     
    alist.print_in_order()
    return

print_bst_list([10,3,4,23,637,8])