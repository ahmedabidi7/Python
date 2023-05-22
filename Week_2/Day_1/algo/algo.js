function calc(arr){
    var obj = {}
    for (i=0;i<arr.length;i++){
        if (obj.hasOwnProperty(arr[i])){
            obj[arr[i]]++
        }
        else{
            obj[arr[i]]=1
        }

    }
    return obj
}

console.log(calc(["a","b","a","c","B","c","c"]))