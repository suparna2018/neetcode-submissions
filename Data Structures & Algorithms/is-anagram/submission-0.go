// import "sort"

func isAnagram(s string, t string) bool {
	if sortString(s)==sortString(t){
		return true
	}
	return false
}

func sortString(s string) string{
	chars := []rune(s)

	sort.Slice(chars, func(i,j int) bool{
		return chars[i]>chars[j]
	})

	return string(chars)
}