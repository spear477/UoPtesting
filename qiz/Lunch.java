interface Food {
    public void printFlavor();
}
class Pepper extends Food {
    public void printFlavor() { System.out.println("hh"); }
}
public class Lunch {
    public static void main(String[] args) {
        Food pepper = new Pepper();
        pepper.printFlavor();
    }
}