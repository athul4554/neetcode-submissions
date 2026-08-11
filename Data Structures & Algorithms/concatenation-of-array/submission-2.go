func getConcatenation(nums []int) []int {
    arr:=append(nums,nums...)
    return arr
}
