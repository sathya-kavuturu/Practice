//Reverse of a string

function reverse(str){
    let newArr=[];
    for(let i= str.length-1; i>=0; i--){
        newArr.push(str[i]);
    }
    return newArr.join("");

}

function reverse2(str){
    return str.split("").reverse().join('');
}

const reverse3 = str=> str.split("").reverse().join('');

const reverse4 = str => [...str].reverse().join('');

console.log(reverse("sathya swaroop"));
console.log(reverse2("sathya swaroop"));
console.log(reverse3("sathya swaroop"));
console.log(reverse4("sathya swaroop"));
