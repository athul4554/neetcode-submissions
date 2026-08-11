func isAcceptableChar(c rune)bool{
	return unicode.IsLetter(c) || unicode.IsDigit(c)
}

func isPalindrome(s string)bool{
	s = strings.ToLower(s)
	s = strings.ReplaceAll(s, " ","")
	i:=0
	j:=len(s)-1
	isPalindrome:=true
	for i<j{
	if !isAcceptableChar(rune(s[i])) {
			i++
			continue
		}

		// Skip right non-alphanumeric
		if !isAcceptableChar(rune(s[j])) {
			j--
			continue
		}

		// Compare valid chars
		if s[i] != s[j] {
			return false
		}

		// ✅ Move both pointers forward
		i++
		j--
	}
	return isPalindrome
}