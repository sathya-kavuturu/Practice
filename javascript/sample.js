// var a = 1;
// var b = 2;
// var c = a+ b;
// console.log(c);


//odd number swith for loop
// myArray = [];
// function oddNumbers(num){
//     for(var i=1; i<num; i+=2){
//         myArray.push(i);
//     }
//     return myArray;
// }

// console.log(oddNumbers(100));


//Count backwards with a for loop

myArray = [];
function backwardOddNumbers(num){
    if(num % 2 == 0){
        num--;
    }
    for(var i=num; i>0; i-=2){
        myArray.push(i);
    }
    return myArray;
}

console.log(backwardOddNumbers(100));
