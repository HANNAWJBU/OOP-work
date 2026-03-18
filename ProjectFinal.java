package mypack;

import java.io.*;
import java.util.UUID;
import java.util.Random;

import java.util.Scanner;
import java.util.function.Function;

public class ProjectFinal{
	Scanner scnr = new Scanner(System.in);
	
	public String password = null;
	public int passLength;
	public int lowercaseLetters;
	public int capitalLetters;
	public int numbers;
	public int symbols;
	public int rating;
	public boolean newPass = false;
	int i;
	
	//module 1 User Inputs
	public void submitPassword() {
		if (newPass == false) {
			System.out.println("Enter your password: ");
			password = scnr.nextLine();
			
			passLength = password.length();
			
			//lower case Letters = 1 point
			//upper case Letters = 2 points
			//numbers = 2 points
			//symbols = 5 points
			
			for (i = 0; i < passLength; ++i) {
				char var = password.charAt(i);
				System.out.println(var);
				if (Character.isLetter(var)) {
					if (Character.isUpperCase(var)) {
						capitalLetters += 1;
					} else {
						lowercaseLetters += 1;			
					} 
				} else if (Character.isDigit(var)) {
					numbers += 1;
				} else {
					symbols += 1;
				}
			}
			//if the password has been resubmitted
		} else if (newPass == true) {
			
			passLength = password.length();
			
			for (i = 0; i < passLength; ++i) {
				char var = password.charAt(i);
				System.out.println(var);
				if (Character.isLetter(var)) {
					if (Character.isUpperCase(var)) {
						capitalLetters += 1;
					} else {
						lowercaseLetters += 1;		
					} 
				} else if (Character.isDigit(var)) {
					numbers += 1;		
				} else {
					symbols += 1;
					
				}
			}
		} else {
			System.out.println("Error");
		}
	} 
		
	
	//module 2 Strength Checker
	public void checkStrength() {
		System.out.println("Lowercase Letters: " + lowercaseLetters);
		System.out.println("Capital Letters: " + capitalLetters);	
		System.out.println("Integers: " + numbers);	
		System.out.println("Symbols: " + symbols);
		rating = (lowercaseLetters + capitalLetters*2 + numbers*2 + symbols*5);
		
		if (rating <= 10) {
			System.out.println("Password strength rating: " + rating);
			System.out.println("Extremely weak password detected. Change your password.");
		} else if (rating <= 25) {
			System.out.println("Password strength rating: " + rating);
			System.out.println("Weak password detected. Consider changing your password.");
		} else if (rating <= 40) {
			System.out.println("Password strength rating: " + rating);
			System.out.println("Average password detected. You may want to change your password.");
		} else if (rating <= 60) {
			System.out.println("Password strength rating: " + rating);
			System.out.println("Strong password detected. Your password is secure.");
		} else if (rating <= 100) {
			System.out.println("Password strength rating: " + rating);
			System.out.println("Extremely strong password detected. You do not need to change your password.");
		} else {
			System.out.println("Password strength rating: " + rating);
			System.out.println("Insanely strong password detected. Your password is unbreakable!.");
		}
	}
	
	public int getRating() {
		return rating;
		
	}
	
 
		public String generateNewPassword(){
			Random r = new Random();
			String l = "abcdefghijklmnopqrstuvwxyz";
			String u = l.toUpperCase();
			String s = "!@#$%^&*()-_=+<>?";
			String password = "";
			boolean lo, up, sym, n;
			lo = false;
			up = false;
			sym = false;
			n = false;
			while(!lo || !up || !sym || !n)
			{
				lo = false;
				up = false;
				sym = false;
				n = false;
				int length = r.nextInt(12, 21);
				for (int i = 0; i < length; i++) {
					int num = r.nextInt(5);
					if (num==1) {
						password += l.charAt(r.nextInt(l.length()));
						lo = true;
					}
					else if (num==2) {
						password += u.charAt(r.nextInt(u.length()));
						up = true;
					}
					else if (num==3) {
						password += s.charAt(r.nextInt(s.length()));
						sym = true;
					}
					else {
						password += r.nextInt(0, 10);
						n = true;
					}
				}
			}
			return password;
		}
	
	
	//module 3 Password Generator
	public void generatePassword() {
		
		if (rating < 60) {
			System.out.println("Would you like to change your password? y/n");		
			
			while (true) {
				String choice = scnr.next();
				if (choice.equals("y")) {

					String generatedPassword = this.generateNewPassword();
					System.out.println(generatedPassword);
					
					newPass = true;
					break;
				} else if (choice == "n") {
					break;
				} else {
					System.out.println("Invalid input detected");
				}
			}
		} else {
			System.out.println("You do not need to change your password.");
		}
	}
	
	//module 4 suggestions
	public void suggestions() {
		if (rating < 60) {
			passLength = password.length();
			
			if (symbols < 3) {
				System.out.println("Consider adding more symbols to your password.");
			} else if (lowercaseLetters < 8) {
				System.out.println("Consider adding more lower-case letters to your password.");
			} else if (capitalLetters < 4) {
				System.out.println("Consider adding more capital letters to your password.");
			} else if (numbers < 4) {
				System.out.println("Consider adding more numbers to your password.");
			} else {
				System.out.println("Consider completely changing your password.");
			}		
		}
	}

	public static void main(String[] args) {
		while (true) {
			Password Var = new Password();
			Var.submitPassword();		
			Var.checkStrength();
			Var.generatePassword();
			Var.suggestions();
			}
		}		
	}
