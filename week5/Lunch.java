class Food {
    String flavor = "bland";
    void printFlavor() { System.out.println(flavor); }
}
class Pepper extends Food {
    String flavor = "spicy";
    void printFlavor() { System.out.println(flavor); }
}
public class Lunch {
    public static void main(String[] args) {
        Food lunch = new Pepper();
        lunch.printFlavor();
    }
}

