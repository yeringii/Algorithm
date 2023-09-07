import java.util.*;
public class Main {
	public static void main(String[] args) {
		String word;
		Scanner sc = new Scanner(System.in);
		word = sc.nextLine();
		word = word.trim();
		String[] words = word.split(" ");
		if(word.isEmpty()) {
			System.out.println(0);
		}
		else System.out.println(words.length);
	
		
	}

}
