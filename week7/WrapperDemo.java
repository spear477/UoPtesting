package week7;

import java.util.ArrayList;

public class WrapperDemo {
   public static void main(String[] args) {
       ArrayList<Integer> myList = new ArrayList<Integer>();
       myList.add(1);  // autoboxing of primitive type int to Integer object
       myList.add(2);
       myList.add(3);
       int x = myList.get(0);  // unboxing of Integer object to primitive type int
       int y = myList.get(1);
       int z = myList.get(2);
       System.out.println(x + y + z);
   }
}
