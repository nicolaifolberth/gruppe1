package snippets.sample6;

/**
 * Klasse String
 * Verwendung und Methoden
 * Foreach Schleife
 * Strings vergleichen mit .equals() Methode der Klasse Object
 */
public class Strings {
	
	
	public static void main(String args[]){
		
		stringMethods();
		
		System.out.println("-------");
		
		stringCompares();
	}
	
	
	//Diverse Operationen der Klasse String
	private static void stringMethods(){
		
		String zeichenkette = "Hallo Welt";
		
		System.out.println(zeichenkette);
		
		System.out.println(zeichenkette.charAt(0));
		
		System.out.println(zeichenkette.substring(0, 5));
		
		System.out.println(zeichenkette.toLowerCase());
		System.out.println(zeichenkette.toUpperCase());
		
		System.out.println(
		        zeichenkette.matches("[A-Za-z]+ [A-Za-z]+"));
		
		String[] teile = zeichenkette.split(" ");
		//Foreach-Schleife
		for (String teil : teile) {
			System.out.println("!" + teil + "!");
		}
		
		int zahl = 123;
		String zahlString = String.valueOf(zahl);
		System.out.println(zahlString);
	}
	
	
	
	//Vorsicht beim Vergleich von Strings mittels Operator ==
	private static void stringCompares(){
		
		String name1 = "Name";
		String name2 = new String("Name");		
		String name3 = "Na" + "me";

		System.out.println(name1);
		System.out.println(name2);
		System.out.println(name3);
		
		System.out.println(name1 == name2);
		System.out.println(name1 == name3);
		System.out.println(name2 == name3);

		System.out.println(name1.equals(name2));
		System.out.println(name1.equals(name3));
		System.out.println(name2.equals(name3));
		
	}

	
}
