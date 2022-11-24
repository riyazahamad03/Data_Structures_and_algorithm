
// 371. Sum of Two Integers
// Given two integers a and b, return the sum of the two integers without using the operators + and -.

class sumOfTwoInteger{
    public int getSum(int a,int b){
        while(b!=0){
            int temp = (a&b) << 1;
            a = (a^b);
            b = temp;
        }
        return a;
    }

    public static void main(String[] args) {
        sumOfTwoInteger myobj = new sumOfTwoInteger();
        System.out.println(myobj.getSum(10, 20));
     }

}


