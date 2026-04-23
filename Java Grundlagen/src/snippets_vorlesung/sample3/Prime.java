package snippets_vorlesung.sample3;

/** 
 * Arrays
 * For Schleife
 * Do Schleife 
 * While Schleife
 * Bedingungen 
 * Operatoren
 */
public class Prime {
	
	
	/**
	 * Methode zur Berechnung von Primzahlen
	 */
	public static void main(String args[]){

		int[] primeNumbers = new int[100];
		int primeCounter = 1;

		int number = 2;

		primeNumbers[0] = 2;

		while(number < 100){
			number++;

			//Prüfung auf mögliche Teiler
			int factor = 2;
			boolean isPrimeNumber = true;
			do{
				if(number % factor == 0){
					isPrimeNumber = false;
					break;
				}

				factor++;
			} while(factor < number);



			//Primzahl ergänzt
			if(isPrimeNumber) {
				primeNumbers[primeCounter] = number;
				primeCounter++;
			}

		}


		//Primzahlen aus array ausgegeben
		for(int i = 0; i < primeCounter; i++){
			System.out.println(primeNumbers[i]);
		}


		
	}
	
	

}
