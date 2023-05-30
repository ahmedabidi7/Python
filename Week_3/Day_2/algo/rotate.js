function rotate(s,r){
    var sn=""
    var l=s.length
    for (i=0;i<r;i++){
        sn+=s[l-1]
        sn+=s.slice(0,l-1)
        s=sn
        sn=""
    }
    return s
}

console.log(rotate("Hello World",13))