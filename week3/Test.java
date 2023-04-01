package week3;

public class Test {
    
    /**
     * Declaring the method 
     * @param x is integer value 
     * @param y is the integer value
     * x and y are the formal parameters
     * @return
     */
    static int findArea(int x, int y) {
        return x*y;
    }
    public static void main(String[] args) {
        int length = 12;
        int width = 23;
        //length and widht are the actual parameters
        int area = findArea(length, width);
        System.out.println("The area is -"+area);
   }
}
