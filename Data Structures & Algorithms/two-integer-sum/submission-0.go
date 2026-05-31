func twoSum(nums []int, target int) []int {
    mp :=make(map[int]int)
	res :=[]int{}
	for i,num := range nums{
		val,ok := mp[target-num]
		if !ok{
			mp[num]= i
		}else{
			res =append(res, val)
			res =append(res, i)
			
			return res
		}
	}
	return res
}
