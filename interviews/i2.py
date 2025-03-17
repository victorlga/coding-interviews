def nth_to_last(head, k):
    p1, p2 = head, head
    for _ in range(k):
        if not p1:
            return None
        p1 = p1.next

    while p1:
        p1, p2 = p1.next, p2.next

    return p2