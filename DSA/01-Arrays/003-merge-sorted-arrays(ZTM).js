function mergeSortedArrays(arr1, arr2){
    const mergedArray = [];
    arr1Item = arr1[0];
    arr2Item = arr2[0];
    let i=1;
    let j=1;

    if(arr1.length == 0) {
        return arr1;
    }
    if(arr2.length ==0){
        return arr2;
    }

    while( arr1Item || arr2Item){
        if(!arr2Item || arr1Item<arr2Item){
            mergedArray.push(arr1Item);
            arr1Item = arr1[i];
            i++;
        }
        else {
            mergedArray.push(arr2Item);
            arr2Item = arr2[j];
            j++;
        }
    }

    return mergedArray;
}

console.log(mergeSortedArrays([0,3,4,31], [3,4,6,30]));
