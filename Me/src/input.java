import java.util.Scanner;

public class input {
    static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("enter *");
        String str = input.next();
        System.out.println("Please enter your name: ");
       String name= input.next();
       System.out.println("Please enter your age: ");
       int age = input.nextInt();
        System.out.println("*******************");
        System.out.println("your name is "+name);
        System.out.println("your age is "+age);
        System.out.println("********************");
    }
}
