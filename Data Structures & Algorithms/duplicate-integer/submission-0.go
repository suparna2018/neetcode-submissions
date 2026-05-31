func hasDuplicate(nums []int) bool {
	mp := make(map[int]int)
	var num int
	for _,num = range nums{
		mp[num]+=1
		if mp[num]>1{
			return true
		}
	}
	return false
}
