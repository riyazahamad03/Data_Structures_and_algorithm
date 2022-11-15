function factorial(x) {
    debugger;
    if(x<2){
        return 1;
    }
    return x + factorial(x-1);
    
}
x=factorial(5)
console.log(x);