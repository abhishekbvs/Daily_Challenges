//Daily Challenge
//Question No: 1
//Link: http://codeforces.com/problemsets/acmsguru/problem/99999/123
//Tags: Fibonacci Series, Basic Math 
//Difficulty: Easy 
//Deadline: 19-07-18 11:00pm

import java.util.Scanner;
public class Day1 {
	public static void main(String[] args) {
		Scanner x = new Scanner(System.in);
		int k = x.nextInt();
		int sumfib=0;
		int a = 1, b=1;
		for(int i=1;i<=k;i++) {
			sumfib=sumfib+a;
			int c=b;
			b=a+b;
			a=c;
		}
		System.out.println(sumfib);
		x.close();
	}
}
