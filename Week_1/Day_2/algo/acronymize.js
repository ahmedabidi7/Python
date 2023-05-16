function acronymize(s){
    a=""
    if(s[0]!=" "){
        a=a+s[0].toUpperCase()
    }
    for(var i=0;i<s.length;i++){
        if((s[i]==" ")&&(s[i+1]!=" ")){
            a=a+s[i+1].toUpperCase()
        }
    }
    return a
}

console.log(acronymize("object oriented programming"))
