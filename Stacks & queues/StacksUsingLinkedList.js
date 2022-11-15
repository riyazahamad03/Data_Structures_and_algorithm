class Node{
    constructor(value){
        this.value = value;
        this.next=null;
    }
}
class Stack{
    constructor(){
        this.top=null;
        this.bottom=null;
        this.length=0;
    }
    peek(){
        return this.top;
    }
    push(value){
        const NewNode= new Node(value);
        if(this.length ===  0){
            this.top=NewNode;
            this.bottom = NewNode;
        }else{
            const holdingPointer = this.top;
            this.top = NewNode;
            this.top.next = holdingPointer;
        }
        this.length++;
        return this;
    }
    pop(){
        if(!this.top){
            return null
        }
        if(this.top === this.bottom){
            this.bottom = null;
        }
        this.top = this.top.next;
        this.length--;
        return this;
        
    }
}
const MyStack = new Stack();
MyStack.push("google");
MyStack.push("Amazon");
MyStack.push("Youtube");
// MyStack.peek()
console.log(MyStack.pop())
console.log(MyStack.pop())
console.log(MyStack.pop())
console.log(MyStack.pop())