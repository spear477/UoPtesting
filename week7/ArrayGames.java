package week7;

import java.util.*;
class ArrayGames {
    public static void main(String[] args) {
        ArrayList<Integer> a = new ArrayList<Integer>();
        for (int i = 1; i <= 5; i++) a.add(i);
        System.out.println(a.get(a.get(2)));
    }
}
