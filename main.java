import java.io.FileWriter;
import java.util.Scanner;

public class RoverController {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);
        
        while (true) {
            System.out.print("Enter move (W = Forward, A = Left, S = Backward, D = Right, Q = Quit): ");
            String move = input.nextLine().toUpperCase();
            
            if (move.equals("Q")) break;

            // Overwrite command.txt with the single letter
            FileWriter writer = new FileWriter("command.txt");
            writer.write(move);
            writer.close();
        }
        input.close();
    }
}