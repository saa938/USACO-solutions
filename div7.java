import java.io.*;
import java.util.*;

public class div7 {
    static String fileBaseName = "div7";
    static Scanner sc;
    static PrintStream out;

    public static void main(String... args) {
        ioSetup();

        int n = sc.nextInt();
		int[] psum = new int[n+1];
		psum[0] = 0;
		for (int i = 0; i < n; i++) {
			psum[i+1] = (sc.nextInt() + psum[i]) % 7;
		}
		
        int s = 0;
        HashMap<Integer, Integer> found = new HashMap<>();
        for (int i = 1; i < n+1; i++) {
            int j = psum[i];
            if (found.containsKey(j)) {
                s = Math.max(s, i - found.get(j));
            } else {
                found.put(j,i);
            }
        }
        out.println(s);
    }

    static void ioSetup() {
        try {
            if (fileBaseName == null || fileBaseName.isBlank()) {
                sc = new Scanner(System.in);
                out = System.out;
            } else {
                sc = new Scanner(new File(fileBaseName+".in"));
                out = new PrintStream(new File(fileBaseName+".out"));
            }
        } catch (IOException ex) {
            
        }
    }
}