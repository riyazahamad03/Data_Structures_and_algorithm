function fibo(n){
    if(n < 2){
        return n;
    }
    // console.log((n-1) + (n-2));
    return  fibo(n-1) + fibo(n-2);
}
// console.log(fibo(60))

function fiboIterative(n){
   let arr=[0,1];
   for (let i=2; i<n+1; i++){
    arr.push(arr[i-1] + arr[i-2]);
   }
   return arr[n];
}
console.log(fiboIterative(5))