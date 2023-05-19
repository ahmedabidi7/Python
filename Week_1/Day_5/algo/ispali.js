function isPalindrome(s){
    r=true
    i=0
    j=s.length-1
    while (i<s.length/2){
        if (s[i]!=s[j]){
            r=false
        }
        i++
        j--
    }
    return r
}

console.log(isPalindrome("racecar"))
