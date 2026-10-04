class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        curr = head
        ans = []

        while curr != None:
            ans.append(curr.val)
            curr = curr.next

        result = str("".join(map(str, ans)))
        
        return int(result, 2)