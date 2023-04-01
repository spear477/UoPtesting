//using this keyword
class Count{
    int counter;

    void Counting(int counter){

        this.counter = counter;
        System.out.println(counter);
    }
}


public class thisTest {
    public static void main(String[] args) {
        
        Count c1 = new Count();
        c1.Counting(12);
    }
}
