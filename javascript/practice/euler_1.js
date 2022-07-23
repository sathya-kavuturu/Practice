// Problem 1: Multiples of 3 and 5
// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

// Find the sum of all the multiples of 3 or 5 below the provided parameter value number.

// Tests
// Waiting:multiplesOf3and5(10) should return a number.
// Waiting:multiplesOf3and5(49) should return 543.
// Waiting:multiplesOf3and5(1000) should return 233168.
// Waiting:multiplesOf3and5(8456) should return 16687353.
// Waiting:multiplesOf3and5(19564) should return 89301183.

function multiplesOf3and5(number) {
    const arr =[];
    number=number-1;
    while(number>0){
      if(number%3==0 || number%5==0){
        arr.push(number);
      }
      number--;
    }
    sum(arr);
    return true;
  }
  
function sum(arr){
    var sum=0;
    for(let i=0; i<arr.length; i++){
      sum = sum + arr[i];
    }
    console.log(sum);
    return true;
  }
  
multiplesOf3and5(1000);
