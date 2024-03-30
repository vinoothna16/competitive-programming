class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        lst1=[]
        lst2=[]
        tmp=head
        while head:
            y=head.val
            if y<x:
                lst1.append(y)
            else:
                lst2.append(y)
            head=head.next
        tmp1=tmp
        head=tmp
        i=0
        l=len(lst1)
        while i<l:
            tmp=ListNode()
            tmp.val=lst1[i]
            head.next=tmp
            head=head.next
            i+=1
        i=0
        l=len(lst2)
        while i<l:
            tmp=ListNode()
            tmp.val=lst2[i]
            head.next=tmp
            head=head.next
            i+=1
        return tmp1.next
        
