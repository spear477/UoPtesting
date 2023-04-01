package week2;
import java.util.*;

public class loop2 {
    public static void main(String a[]){

        //string array 

        String[] typeOfJob = {"Student","Postman","Actor","Teacher"};

        System.out.println("This is for- loop ");
        //loop through string array with for
        for(int i=0; i < typeOfJob.length;i++){
            System.out.println("This a "+typeOfJob[i]+".");
        }


        System.out.println("This is while- loop ");

        //while lopping for string array
        
        //first No variable is declared with value 0
        int No = 0;
        while( No < typeOfJob.length){
            System.out.println("This a "+typeOfJob[No]+".");
            No++;
        }



        System.out.println("This is do while - loop ");
        //do while looping for string array
        //no variable is delacred with value 0
    int no = 0;
       do{
            System.out.println("This a "+typeOfJob[no]+".");
            no++;
       }
       while(No < typeOfJob.length);
    }
}
