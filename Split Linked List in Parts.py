class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        noOfElements=0
        tmp=head
        while tmp:
            noOfElements+=1
            tmp=tmp.next
        approxNoOfElementsInResultList=noOfElements//k
        extraElementCount=0
        if (k>noOfElements):
            approxNoOfElementsInResultList=1
        else:
            extraElementCount=noOfElements-approxNoOfElementsInResultList*k
        iteratedCount=0
        tmp=head
        resultList=[]
        while tmp:
            if k==1:
                resultList.append(head)
                k-=1
                break;
            iteratedCount+=1
            if iteratedCount==approxNoOfElementsInResultList:
                if (extraElementCount>0):
                    tmp=tmp.next
                    extraElementCount-=1
                if tmp:
                    tmp2=tmp.next
                    tmp.next=None
                    resultList.append(head)
                    tmp=tmp2
                    head=tmp2
                    iteratedCount=0
                    k-=1
            else:
                tmp=tmp.next
        while k>0:
            k-=1
            resultList.append(ListNode(""))
        return resultList
                    
                    
