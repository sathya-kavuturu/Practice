// let string =[3,4,5,6,76,54,"gsdfg", "dgdg"];

// console.log(string.slice(2,5));

class MyArray{
    constructor(){
        this.length = 0;
        this.data= {}; 
    }

    get(index){
        return this.data[index];
    }

    push(item){
        this.data[this.length] = item;
        this.length++;
    }

    unshift(item){
        for(let i=this.length; i>0; i--){
            this.data[i]= this.data[i-1];
        }
        this.data[0] = item;
        this.length++;
    }

    pop(){
        var lastElement = this.data[this.length-1];
        delete this.data[this.length-1];
        this.length--;
        return lastElement;

    }

    shift(){
        for(let i=0; i<this.length-1; i++){
            this.data[i] = this.data[i+1];
        }
        delete this.data[this.length-1];
        this.length--;
    }
    
    delete(index){
        var element = this.data[index];
        this.shiftItems(index);
        return element;
    }

    shiftItems(index){
        for(let i=index; i<this.length-1; i++){
            this.data[i]=this.data[i+1];
        }
        delete this.data[this.length-1];
        this.length--;
    }
    
}

const arr = new MyArray();
arr.push("hifdhsf");
arr.push(23);
console.log(arr);
arr.push(56);
console.log(arr);
arr.push("hi you");
console.log(arr);
arr.pop();
console.log(arr);
console.log(arr.get(1));
arr.push(123);
console.log(arr);
arr.push("sathya");
console.log(arr);
arr.shift();
console.log(arr);
console.log(arr.length);
arr.unshift("swaroop");
console.log(arr);
