import java.util.InputMismatchException;
import java.util.Scanner;

public class exception {

       public static void main(String[] args) {
           try{
               Scanner input = new Scanner(System.in);
            System.out.println("Enter the first number");
            int num1 = input.nextInt();
            System.out.println("Enter the second number");
            int num2 = input.nextInt();
            System.out.println(num1/num2);
    }catch (ArithmeticException e){
               System.out.println(" this is Arithmetic Exception");
           }catch (InputMismatchException e){
               System.out.println(" this is Input Mismatch");
           }

    }
}
