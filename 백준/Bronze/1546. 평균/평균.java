import java.util.*;
public class Main {
	public static void main(String[] args) {
		int n;
		int score;
		double fix;
		double avg = 0;
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		int[] scores = new int[n];
		
		for(int i = 0; i < n; i++) {
			score = sc.nextInt();
			scores[i] = score;
		}
		Arrays.sort(scores);
		for(int i =0; i<scores.length; i++) {
			fix = (double)scores[i]/scores[scores.length-1]*100;
			avg += fix;
		}
		avg = avg / n;
		System.out.println(avg);
	}

}
