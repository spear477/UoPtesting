package week2;
import java.util.*;


public class loop3 {
    public static void main(String a[]){
        Scanner Name = new Scanner(System.in);
        System.out.print("Type the word you like --  ");
        String TypeName = Name.nextLine();


        System.out.println("This is for- loop ");
        //for looping
        for(int count=0; count < TypeName.length(); count++){
            System.out.println("This is - "+ TypeName.substring(count));
        }

        System.out.println("This is while- loop ");
        //while lopping
        int countWhile = 0;

        while(countWhile < TypeName.length()){
            System.out.println("This is - "+ TypeName.substring(countWhile));
            countWhile++;
        }

        System.out.println("This is do while - loop ");

        //do while looping
        int countDo = 0;
        
        do
        {
            System.out.println("This is - "+ TypeName.substring(countDo));
            countDo++;
        }
        while(countDo < TypeName.length());
    }
}
