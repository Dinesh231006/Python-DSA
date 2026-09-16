class Solution:
    def firstNonRepeating(self, arr): 
        occ={}
        for i in arr:
            if i not in occ.keys():
                occ[i]=1
                continue
            occ[i]+=1
        for i in occ.keys():
            if occ[i]==1:
                return i
        return 0