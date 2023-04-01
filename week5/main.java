//using super keyword
class Animal{
    public void display(){
        System.out.println("This is animal");
    }
}

class Dog extends Animal{
    public void display(){
        System.out.println("This is Dog");
    }
    public void printMessage(){
        display();
        super.display();
    }
}

public class main {
    public static void main(String[] args) {
        Dog p1 = new Dog();
        p1.printMessage();
    }
}
