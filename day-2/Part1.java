import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Arrays;
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.ArrayList;

public class Part1 {
    public static boolean isSafe(ArrayList<Integer> f) {
        if (f.get(0) > f.get(1)) { // decreasing
            for (int i = 0; i < f.size() - 1; i++) {
                if (f.get(i) <= f.get(i+1)) {
                    return false;
                }
                if (f.get(i) - f.get(i+1) > 3) {
                    return false;
                }
            }
            return true;
        } else if (f.get(0) < f.get(1)) { // increasing
            for (int i = 0; i < f.size() - 1; i++) {
                if (f.get(i) >= f.get(i+1)) {
                    return false;
                }
                if (f.get(i+1) - f.get(i) > 3) {
                    return false;
                }
            }
            return true;
        }
        return false;
    }
    public static void main(String[] args) {
        ArrayList<ArrayList<Integer>> f = new ArrayList<>();
        try {
            File myObj = new File("day-2/input.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                String[] dataSplit = data.split(" ");
                Integer[] temp = new Integer[dataSplit.length];
                for (int i = 0; i < dataSplit.length; i++) {
                    temp[i] = Integer.parseInt(dataSplit[i]);
                }
                f.add(new ArrayList<>(Arrays.asList(temp)));
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        int total = 0;
        for (ArrayList<Integer> f_i : f) {
            if (isSafe(f_i)) {
                total++;
            }
        }
        System.out.printf("a total of %d safe", total);
    }
}