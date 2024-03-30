class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        lst=[]
        while head:
            lst.append(head)
            head=head.next
        l=len(lst)
        k=k%l
        if k!=l:
            lst = lst[-k:]+lst[:l-k]
        i=0
        head = ListNode()
        tmp=head
        while i <l:
            head.next=lst[i]
            head=head.next
            i+=1
        head.next=None
        return tmp.next
