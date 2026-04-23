package snippets.sample7;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Eingabestrom
 * Buffered Stream
 * Explizites behandeln von Exceptions
 * try, catch, finally, throws
 * RunTimeExceptions
 * throw
 */
public class Streams {

	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) {
		
		//Variable für eingelesene Eingabe		
		String myLine = "";
		
		//Streamobjekte erzeugen und verbinden
		InputStreamReader myInputestream = new InputStreamReader(System.in);
		
		BufferedReader myBufferedReader = new BufferedReader(myInputestream);		
		
		
		//Eingabestrom abgreifen			
		System.out.println("Eingabe:");
		
		try {
			myLine = myBufferedReader.readLine();
		} catch (IOException e1) {			
			e1.printStackTrace();
		}
		
		//Eingabe ausgeben
		System.out.println(myLine);					
			
		
		
		
		
		//RuntimeException
		int number;
		
		try {
			System.out.println("12 / 0");
			
			number = 12 / 0;
			
			System.out.println(number);			
			
		} catch(ArithmeticException e) {
			e.printStackTrace();
		} finally {
			System.out.println("done");
		}
		
		
		
		//Eigene Exception werfen
		try {
			System.out.println("Eigene Exception");
			
			huch();			
			
		} catch(Exception e) {
			e.printStackTrace();
		} finally {
			System.out.println("done");
		}
		
		

	}
	
	//Methode mit Exception
	public static void huch() throws Exception{
		throw new Exception("huch");
	}

}
