import java.util.*;
public class Main {
	public static void main(String[] args) {
		int test;
		int score = 0;
		int sum = 0;
		String quiz;
		Scanner sc = new Scanner(System.in);
		test = sc.nextInt();
		for(int i = 0; i<test; i++) {
			quiz = sc.next();
			sum=0;
			score = 0;
			for(int j = 0; j<quiz.length(); j++) {
				
				if(quiz.charAt(j) == 'O') {
					score+=1;
					sum += score;
				}else if(quiz.charAt(j) == 'X'){
					score = 0;
					sum+=score;
				}	
			}
			System.out.println(sum);
		}

		
		
	}

}
