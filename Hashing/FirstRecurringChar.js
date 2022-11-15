function FirstRecurringChar(input){
    for(let i=0;i<input.length;i++){
      for(let j=i+1;j<input.length;j++){
        if(input[i] === input[j]){
          return input[i];
          // break;
        }
      }
    }
    console.log(undefined);
  }
  
//   console.log(FirstRecurringChar([1,2,1,3,13,13,11,3]));
function FirstRecurringCharUsingHashTable(input){
    let map={};
    for(let i=0;i<input.length;i++){
        if(map[input[i]] !== undefined){
            return input[i];
        }else{
            map[input[i]] = i;
        }
    }
}
console.log(FirstRecurringCharUsingHashTable([1,2,1,3,13,13,11,3]));