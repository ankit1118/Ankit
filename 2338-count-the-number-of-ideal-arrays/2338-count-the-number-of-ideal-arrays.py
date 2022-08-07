class Solution:
    def idealArrays(self, n, maxValue):
        r,m=0,[[None]*(n+1) for _ in range(15)]
        def g(o):
            v , t=o,[]
            for i in range(2,int(sqrt(o))+1):
                c=1
                while not v % i:
                    v,c=v/i,c+1
                if c>0:
                    t.append(c)
            if v>1:
                t.append(2)
            return t
        def s(o,p):
            if o==1 or p==1:
                return 1
            elif m[o][p]==None:
                m[o][p]=0
                for i in range(1,o+1):
                    m[o][p]=(m[o][p]+ s(i,p-1))% 1000000007
            return m[o][p]
        def h(o,p):
            if o==1 or p==1:
                return 1
            t=1
            for v in g(o):
                t = t*s(v,p)% 1000000007
            return t
            c = g(o)
        for i in range(1,maxValue+1):
            r=(r+h(i,n))%1000000007
        return r