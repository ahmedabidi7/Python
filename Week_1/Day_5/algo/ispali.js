function isPalindrome(s){
    i=0
    j=s.length-1
    while (i<s.length/2){
        if (s[i]!=s[j]){
            return false
        }
        i++
        j--
    }
    return true
}

console.log(isPalindrome("racecar"))
