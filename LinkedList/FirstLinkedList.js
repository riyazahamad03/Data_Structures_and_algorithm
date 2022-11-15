class Node{
    constructor(value){
        this.head={
            value:value,
            next:null
        }
    }
}
class MyFirstLinkedList{
    constructor(value){
        this.head={
            value:value,
            next:null 
        }
        this.tail=this.head
        this.length=1;
    }
    append(value){
        // const NewNode = new Node(value);
        const NewNode={
            value:value,
            next:null
        }
        this.tail.next = NewNode;
        this.tail=NewNode;
        this.length+=1;
        return this;
    }
    prepend(value){
        const NewNode={
            value:value,
            next:null
        }
        NewNode.next = this.head;
        this.head = NewNode;
        this.length+=1;
        return this;

    }
    printList(){
        const arr=[];
        let currentNode=this.head;
        while(currentNode!=null){
            arr.push(currentNode.value);
            currentNode=currentNode.next;
        }
        return arr;
    }
    insert(index,value){
        if(index>=this.length){
            return this.append(value);
        }
        const newNode={
            value:value,
            next:null
        };
        const leader = this.traverseToIndex(index-1);
        const holdingPointer  = leader.next;
        leader.next = newNode;
        newNode.next=holdingPointer;
        this.length++;
        return this.printList();
    }
    traverseToIndex(index){
        let counter=0;
        let currentNode=this.head;
        while(counter!=index){
            currentNode=currentNode.next;
            counter++
        }
        return currentNode;
    }
    remove(index){
        const leader = this.traverseToIndex(index-1);
        const UnwantedNode=leader.next;
        leader.next = UnwantedNode.next;
        this.length--;
        return this.printList();
    }
    reverse(){
        if(!this.head){
            return this.head;
        }
        let first=this.head;
        this.tail=this.head;
        let second=first.next;
        while(second){
            const temp = second.next;
            second.next=first;
            first=second;
            second=temp;
        }
        this.head.next=null;
        this.head=first;
        return this;
    }
}
const LinkedLists = new MyFirstLinkedList(10);
LinkedLists.append(1);
LinkedLists.append(15)
LinkedLists.append(12)
LinkedLists.prepend(100);
LinkedLists.remove(1);
console.log(LinkedLists.printList());
