package week2;
import java.util.*;

public class loop1 {
    public static void main(String argu[]){

        //assign variable
        //using scanner to get input value from user
        Scanner user = new Scanner(System.in);

        System.out.print("Type your favourite number:-");
        int countInput = user.nextInt();


        System.out.println("This is for- loop ");
        // //This is looping using for-loop
        for( int count = 0; count <= countInput; count++ ){
             System.out.println("This is count from "+count);
        }
        
         

        System.out.println("This is while- loop ");
        // //assing count value = 0
        int count = 0;
        //while looping 
        while( count <= countInput){
            System.out.println("This is count from "+count);
            //need to increase the count
            count++;
        }


        System.out.println("This is do while - loop ");
        //Scanner input for do while lopping
        int countDo = 0;
        Scanner doInput = new Scanner(System.in);
        System.out.print("Type your favourite number:-");
        int doCount = doInput.nextInt();
        do
        {
            System.out.println("This is count from "+countDo);
            //need to increase the count
            countDo++;
        }while( countDo <= doCount);
    
        
        
    }
}
