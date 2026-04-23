package snippets_vorlesung.sample4;

/**
 * 	Übergabe per Wert vs Übergabe per Referenz
 */
public class ValueReference {
	
	//number attribute
	private int number;

	public int getNumber() {
		return number;
	}

	public void setNumber(int number) {
		this.number = number;
	}
	
		
	//constructor
	public ValueReference(int number){
		this.number = number;
	}
	
	
	//callByValue
	public static void callByValue(int number){
		number = number * 2;
	}
	
	//callByReference
	public static void callByReference(ValueReference myReference){
		myReference.setNumber(myReference.getNumber() * 2);
	}
	
	
	//main
	public static void main(String args[]){
		
		int myNumber = 23;
		
		System.out.println(myNumber);
		callByValue(myNumber);
		System.out.println(myNumber);
		
		System.out.println("-----------");
		
		
		ValueReference myReference = new ValueReference(42);
		
		System.out.println(myReference.getNumber());
		callByReference(myReference);
		System.out.println(myReference.getNumber());
		
	}
	
	

}
