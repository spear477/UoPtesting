class Food {
    Food() { System.out.println(flavor); }
    String flavor = "bland";
}
class Pepper extends Food {
    String flavor = "gg";
}
public class Lunch {
    public static void main(String[] args) {
        Food lunch = new Pepper();
    }
}