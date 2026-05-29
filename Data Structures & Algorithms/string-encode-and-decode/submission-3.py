class Solution:

    def encode(self, strs: List[str]) -> str:
        resStr=""
        for ele in strs:
            resStr += str(len(ele))+'#'+ele
        
        return resStr

    def decode(self, s: str) -> List[str]:
        cnt=0
        res=[]
        while cnt<len(s):
            start=cnt
            while s[start] != '#':
                start+=1
            d=int(s[cnt:start])
            start+=1
            res.append(s[start : start+d])
            cnt=start+d
        return res