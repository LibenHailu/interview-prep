def removeDups(ll):
    hash_map = {}
    node = ll.head
    while  node:
        if node.val in hash_map:
            node.prev.next = node.next
        else:
            hash_map.add(node.val)
    
    return ll.head

def removeDups(ll):
    hash_map = {}
    node = ll.head
    while  node:
        if node.val in hash_map:
            node.prev.next = node.next
        else:
            hash_map.add(node.val)
    
    return ll.head


