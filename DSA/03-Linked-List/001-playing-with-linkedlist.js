class MyLinkedList{
    constructor(value){
        this.head = {
            value: value,
            next: null
        }
        this.tail = this.head;
        this.length = 1;
    }

    append(value){
        let newNode = {
            value: value,
            next: null
        }
        this.tail.next = newNode;
    }
}
