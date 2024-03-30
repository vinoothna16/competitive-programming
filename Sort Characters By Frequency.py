class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            if i in d:
                x=d[i]
                x+=1
                d[i]=x
            else:
                d[i]=1
        d=dict(sorted(d.items(), key=lambda item: item[1], reverse = True))
        t=""
        for k,v in d.items():
            t=t+v*k
        return t
