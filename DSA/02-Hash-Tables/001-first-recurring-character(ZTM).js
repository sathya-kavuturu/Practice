function firstRecurringCharacter(arr){
    let map ={};
    for(let i=0; i<arr.length; i++){
        if(map[arr[i]] !== undefined){
            return arr[i];
        }else{
            map[arr[i]] = i;
        }
    }
    return undefined;
}

console.log(firstRecurringCharacter([1,5,5,1,3,4,6]));
