package CS1102;
// import  javax.swing.JOptionPane;
import java.awt.*;
import javax.swing.*;

public class MultipleChoiceQuestion extends Question {
    // static int nQuestions = 0;
    // static int nCorrect = 0;

    // String question;
    // String correctAnswer;
    // MultipleChoiceQuestion(String query, String a, String b, String c, String d, String e, String answer) {
    //      question = query+"\n";
    //      question += "A. "+a+"\n";
    //      question += "B. "+b+"\n";
    //      question += "C. "+c+"\n";
    //      question += "D. "+d+"\n";
    //      question += "E. "+e+"\n";


    //      correctAnswer = answer;
    //     correctAnswer = correctAnswer.toUpperCase();

        
        
       
    // }
    MultipleChoiceQuestion(String query, String a, String b, String c, String d, String e, String answer){
        super(query);
        addChoice("A", a);
        addChoice("B", b);
        addChoice("C", c);
        addChoice("D", d);
        addChoice("E", e);
        initQuestionDialog();
        correctAnswer = answer;
        correctAnswer = correctAnswer.toUpperCase();
    
    }
    void addChoice(String name , String label){
        JPanel choice = new JPanel(new BorderLayout());
        JButton button = new JButton(name);
        button.addActionListener(question);
        choice.add(button,BorderLayout.WEST);
        choice.add(new Label(label+" ", JLabel.LEFT), BorderLayout.CENTER);
        question.add(choice);
    }

    // String ask(){
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
    // void check() { 
    //     nQuestions++;        
    //     String answer = ask();        
    //      if (answer.equals(correctAnswer)) {  
    //         JOptionPane.showMessageDialog(null,"Correct!");            
    //         nCorrect++;         
    //     } else {  
    //         JOptionPane.showMessageDialog(null,"Incorrect. The correct answer is "+correctAnswer+"."); 
    //     }   
    //  }

    //  static void showResults(){
    //     JOptionPane.showMessageDialog(null,nCorrect+"correct out of"+nQuestions+"questions");
    //  }


}
