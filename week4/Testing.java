// class create
class Light{
    //state
    boolean isOn;


    //methods
    void turnOn(){
        isOn = true;
        System.out.println("Light is on");
    }

    void turnOff(){
        isOn = false;
        System.out.println("Light is off");
    }
}


public class Testing {
    public static void main(String[] args) {
        //object creation

        Light On = new Light();
        On.turnOn();
        Light Off = new Light();
        Off.turnOff();
    }
}
