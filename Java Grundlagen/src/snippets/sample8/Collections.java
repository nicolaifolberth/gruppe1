package snippets.sample8;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Vector;


/**
 * Collections, Interfaces und Wrapperklassen
 */
public class Collections {
	
	//main
	public static void main(String[] args) {
		
		//Interface List und Zuweisung mit Implementierung LinkedList
		List<Integer> primeNumbers = getPrimeNumbers();
		
		//Interface List und Zuweisung mit Implementierung Vector
		List<Integer> myList = new Vector<Integer>();
		
		
		//Ausgabe Listengröße	
		System.out.println(primeNumbers.size());
		
		//Foreach Schleife über alle Zahlen
		//Nutzung von Wrapperklassen für Foreach
		for( Integer primeNumber : primeNumbers){
			System.out.println(primeNumber + 2);
		}
		
		
	}
	
	
	
	//Primzahlberechnung
	public static LinkedList<Integer> getPrimeNumbers(){
				
		LinkedList<Integer> primeNumbers = new LinkedList<Integer>();
		
		int number = 5;
		int numberMax = 100;
		int factor = 3;
		
		primeNumbers.add(2);
		primeNumbers.add(3);
		
		do{			
			factor = 3;
			
			while (factor < number){
				
				if (number % factor == 0){
					//ganzzahliger Teiler gefunden
					break;
				}
				
				factor++;						
			}			
			
			if(factor >= number){
				//Primzahl gefunden
				primeNumbers.add(number);
			}
			
			number = number + 2;
			
		} while ( number < numberMax );
					
		
		return primeNumbers;		
	}
	
	

}
