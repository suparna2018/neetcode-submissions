class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        cnt=0
        res=[]
        for el in nums:
            if el!=0:
                prod*=el
            else:
                cnt+=1
        if cnt>1:
            return [0]*len(nums)

        for el in nums:
            if el==0:
                res.append(prod)
            else:
                if cnt>0:
                    res.append(0)
                else:
                    res.append(prod//el)
        return res

            
        