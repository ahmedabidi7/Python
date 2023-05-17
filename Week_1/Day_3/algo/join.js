function join(arr,separator){
    result = ""
    if(arr==result){
        return result
    }
    for (i=0;i<arr.length-1;i++){
        result+=arr[i]+separator
    }
    result+=arr[i]
    return result
}

console.log(join([1,2,3,4,5],"-"))
