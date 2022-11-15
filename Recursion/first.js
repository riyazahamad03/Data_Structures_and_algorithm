let count=0
function inception(){
    if(count > 3){
        return 'done';
    }
    count++;
    return inception();
}
console.log(inception());