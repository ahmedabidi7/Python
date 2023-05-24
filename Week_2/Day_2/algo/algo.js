function removeDup(s){
    var sn = ""
    for (i=0;i<s.length;i++){
        if(sn.includes(s[i])==false){
            sn+=s[i]
        }
    }
    return sn
}

console.log(removeDup("helloo"))