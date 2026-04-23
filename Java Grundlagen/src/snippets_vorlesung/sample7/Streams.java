package snippets_vorlesung.sample7;

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
	 * @throws Exception 
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
        } catch (IOException e) {
            e.printStackTrace();
        }

        //Eingabe ausgeben
		System.out.println(myLine);


		//RuntimeException
		System.out.println("Runtime Exception");

		int number = 0;

		System.out.println("12 / 0");

		//number = 12 / 0;

		System.out.println(number);
			
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		//Eigene Exception werfen
		System.out.println("Eigene Exception");

        try {
            huch();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }


    }
	
	//Methode mit Exception
	public static void huch() throws Exception{
		throw new Exception("huch");
	}

}
