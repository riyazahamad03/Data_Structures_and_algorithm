class Stack{
    constructor(){
        this.array = [];
    }
    peek(){
        return this.array[this.array.length - 1];
    }
    push(value){
        this.array.push(value);
        return this;
    }
    pop(){
        this.array.pop();
        return this;
    }
}

const MyStack = new Stack();
MyStack.push("Google");
MyStack.push("Amazon");
MyStack.push("Youtube");
// MyStack.pop()
// MyStack.pop()
// MyStack.pop()
console.log(MyStack.peek());