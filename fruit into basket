class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        lst=[]
        lsttmp= []
        max1=0
        max2=0
        val1=-1
        val2=-1
        for i in fruits:
            if val1==-1 and i!= val2:
                val1=i
            elif val2==-1 and i!= val1:
                val2=i
            if i==val1 or i == val2:
                lsttmp.append(i)
            else:
                lst.append(lsttmp.count(val1))
                lst.append(lsttmp.count(val2))
                x=lsttmp[-1]
                lst2=[]
                j=len(lsttmp)-1
                while j>=0:
                    if lsttmp[j] !=x:
                        break
                    lst2.append(x)
                    j-=1
                lsttmp=lst2
                if (prev==val1):
                    val2=i
                    val1=prev
                else:
                    tmp=val2
                    val1=tmp
                    val2=i
                lsttmp.append(i)
            prev = i
        lst.append(lsttmp.count(val1))
        lst.append(lsttmp.count(val2))
        l=len(lst)
        i=0
        m=0
        while i < l-1:
            m=max(m,lst[i]+lst[i+1])
            i+=2
        return m
