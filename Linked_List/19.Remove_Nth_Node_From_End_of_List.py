def removeNthFromEnd(head, n):
    curr = head
    count = 0

    while curr != None:
        curr = curr.next
        count += 1

    if count == 1:
        return None

    if n == count:
        return head.next

    curr = head

    for i in range(count - n - 1):
        curr = curr.next

    curr.next = curr.next.next

    return head