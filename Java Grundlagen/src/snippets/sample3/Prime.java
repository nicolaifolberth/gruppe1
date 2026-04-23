package snippets.sample3;

/** 
 * Arrays
 * Schleifen Do/While/For
 * Bedingungen 
 * Operatoren
 */
public class Prime {
	
	
	/**
	 * Methode zur Berechnung von Primzahlen
	 */
	public static void main(String args[]){
		
		int[] primeNumbers = new int[100];
		int primeCounter = 0;
		
		
		int number = 2;
		int numberMax = 100;
		int factor = 2;
		
		
		do{
			
			factor = 2;
			while(factor < number){
				
				if(number % factor == 0){
					break;
				}
				
				factor++;
			}
			
			
			if(factor == number){
				primeNumbers[primeCounter] = number;
				primeCounter++;
			}
				
			number++;
		} while (number <= numberMax);
		
		
		for(int i=0; i<primeCounter; i++){
			System.out.println(primeNumbers[i]);
		}
	}
	
	

}
