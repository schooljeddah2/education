from multiprocessing.reduction import duplicate


class Solution:
    def duplicates(self, arr, n): 
        d={}
        for i in arr:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        sol=[i for i,j in d.items() if j>1]
        if sol:
            return sorted(sol)
        else: 
            return [-1]
        
duplicate()