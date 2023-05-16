function reverse(s){
    if (s.length<2){
        return s
    }
    s2=""
    for (var i=s.length-1;i>=0;i--){
        s2=s2+s[i]
    }
    return s2
}

console.log(reverse("hello"))
