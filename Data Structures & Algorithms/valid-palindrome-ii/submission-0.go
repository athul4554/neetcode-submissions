func validPalindrome(s string) bool {
	isPalindrome:=func(s string)bool{
		l:=0
		r:=len(s)-1
		for l<r{
			if s[l]!=s[r]{
				return false
			}
			l++
			r--
		}
		return true
	}
	l:=0
	r:=len(s)-1
	for l<r{
		if s[l] != s[r]{
			skipL:=s[l+1:r+1]
			skipR:=s[l:r]
			return isPalindrome(skipL)||isPalindrome(skipR)
	}
	l++
	r--
	}
return true
}
