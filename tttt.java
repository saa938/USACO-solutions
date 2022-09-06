

import java.io.*;
import java.util.*;

public class tttt {
    static String fileBaseName = "tttt";
    static Scanner sc;
    static PrintStream out;

    public static void main(String... args) {
        ioSetup();
			  char[][] input = new char[3][3];
        
        for (int i = 0; i < 3; i++) {
            String curLine = sc.next();
					  input[i] = curLine.toCharArray();
				}

			 

				Set<String> cows = new HashSet<>();
        for (int i = 0; i < 3; i++){
					  //ROW
            Set <Character> row = new HashSet<>();
						Set <Character> col = new HashSet<>();
					  for(int j = 0; j< 3; j++) {
							row.add(input[i][j]);
							col.add(input[j][i]);
						}
					  cows.add(String.join("", row.toString()));
						cows.add(String.join("", col.toString()));
				}
				
				Set <Character> diag1 = new HashSet<>();
				diag1.add(input[0][0]); diag1.add(input[1][1]); diag1.add(input[2][2]);
				Set <Character> diag2 = new HashSet<>();
				diag2.add(input[0][2]); diag2.add(input[1][1]); diag2.add(input[2][0]);
				cows.add(String.join("", diag1.toString())); 
				cows.add(String.join("", diag2.toString()));
         // System.out.println(cows);

				int indiv = 0;
				int team = 0;
			  Iterator<String> it = cows.iterator();
				 while (it.hasNext()) {
					String curString = it.next();
					// System.out.println(curString); 
					int curLen = curString.length();
					// System.out.println(curLen);
					if (curLen == 3) {
						indiv++;
					} 
					if (curLen == 6) {
						team++;
					}
				}
			out.println(indiv);
			out.println(team);
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