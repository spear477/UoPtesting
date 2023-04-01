package CS1102;
// import javax.swing.JOptionPane;

public class Quiz {

    // static int nQuestions = 0;
    // static int nCorrect = 0;

    // static String ask( String question){

    //     while(true){

    //         String answer = JOptionPane.showInputDialog(question);
    //         answer = answer.toUpperCase();

    //         boolean valid = (answer.equals("A")||answer.equals("B")||answer.equals("C")||answer.equals("D")||answer.equals("E"));

    //         if(valid){
    //             return answer;
    //         }

    //         JOptionPane.showMessageDialog(null,"Invalid answer.Please enter A,B,C,D or E");
    //     }


    // }
    // static void check(String question, String correctAnswer) { 
    //     nQuestions++;        
    //     String answer = ask(question);        
    //      if (answer.equals(correctAnswer)) {  
    //         JOptionPane.showMessageDialog(null,"Correct!");            
    //         nCorrect++;         
    //     } else {  
    //         JOptionPane.showMessageDialog(null,"Incorrect. The correct answer is "+correctAnswer+"."); 
    //     }   
    //  }



    
    
    public static void main(String[] args) {

        Question question = new MultipleChoiceQuestion(

                "What is a quiz?",
                "a test of knowledge, especially a brief informal test given to students",
                "42",
                "A duck",
                "to get to the other side",
                "To be or not to be, that is the question.",
                "a");

        question.check();

         question = new MultipleChoiceQuestion(

                "What do you tell if someone ask how are you? ",
                "Thanks you",
                "I don't know",
                "Yes, I am",
                "I'm fine",
                "I am happy",
                "d");

                question.check();

        question = new MultipleChoiceQuestion(

                "Are you human?",
                "Neither",
                "Yes, I am.",
                "A duck",
                "Mass",
                "Ar wooooooo",
                "b");

                question.check();

         question = new MultipleChoiceQuestion(

                "What is my favourtie pet?",
                "Duck",
                "Cat",
                "Dog",
                "Bird",
                "Monkey",
                "d");

                question.check();

        
     question = new MultipleChoiceQuestion(

            "How old is my father?",
            "around 10",
            "around 70",
            "around 60",
            "around 30",
            "around 50",
            "e");

            question.check();

         question = new TrueFalseQuestion("Are you 18?", "True");
            question.check();
         question = new TrueFalseQuestion("Are you a student?", "False");
            question.check();
         question = new TrueFalseQuestion("Are you single?", "False");
            question.check();
         question = new TrueFalseQuestion("Is it good to attend at UoPeople?", "True");
            question.check();
            question.showResults();

        
            
        // String question = "What is my name?\n";
        //         question += "A. Aung Ko\n";
        //         question += "B. Kyaw Gee\n";
        //         question += "C. Tun Tun\n";
        //         question += "D. Aung kyaw\n";
        //         question += "E. Kyaw Kyaw \n";

        //         // check(question, "A");
                

        //         question = "Which one is fruit?\n";
        //         question += "A. Doctor\n";
        //         question += "B. Apple \n";
        //         question += "C. Bicycle\n";
        //         question += "D. Pizza\n";
        //         question += "E. Kyaw Kyaw \n";
        //         check(question, "B");


        //         question = "What is my job?\n";
        //         question += "A. Playing\n";
        //         question += "B. Guitar\n";
        //         question += "C. Developer\n";
        //         question += "D. Eating\n";
        //         question += "E. Yangon \n";

        //         check(question, "C");

        //         JOptionPane.showMessageDialog(null,nCorrect+"correct out of"+nQuestions+"questions");
    }
}
