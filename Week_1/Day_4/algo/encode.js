
function encode (s){
    result=""
    enc=false
    for(i=0;i<s.length-2;i++){
        if((s[i]==s[i+1])&&(s[i]==s[i+2])){
            enc=true
        }
    }
    if(enc==true){
        for(i=0;i<s.length-1;i++){
            x=1
            j=i
            while(s[j]==s[j+1]){
                x++
                j++
            }
            if(x==1){
                result+=s[j]
            }
            else{
                result+=s[j]+x
            }
            i=j
        }
    }
    else{
        result=s
    }
    return result
}

function encode2 (s){
    result=""
    for(i=0;i<s.length-1;i++){
        x=1
        j=i
        while(s[j]==s[j+1]){
            x++
            j++
        }
        if(x==1){
            result+=s[j]
        }
        else{
            result+=s[j]+x
        }
        i=j
    }
    if((s.length<3)||(s.length==result.length)){
        return s
    }
    else{
        return result
    }
}

console.log(encode2("aaaabbcddd"))
