class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=defaultdict(list)
        res=[]
        for el in strs:
            sorted_el=tuple(sorted(el))
            if sorted_el in mp:
                mp[sorted_el].append(el)
            else:
                mp[sorted_el].append(el)
        
        for k,v in mp.items():
            res.append(v)
        return res
