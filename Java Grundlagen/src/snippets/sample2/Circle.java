package snippets.sample2;

/**
 * Attribute
 * Variablen  
 * Methoden
 * Getter & Setter
 * Objekte
 */
public class Circle {	
	
	//PI = 3.1416
	private static final double PI = 3.14;
	
	//radius Attribut
	private double radius;
	
	public double getRadius() {
		return radius;
	}

	public void setRadius(double radius) {
		this.radius = radius;
	}

			
	
	//SurfaceArea = radius * radius * PI
	public double getSurfaceArea(){
		return radius * radius * PI;
	}
	
	//Periphery = radius * 2 * PI
	public double getPeriphery(){
		return radius * 2 * PI;
	}
	
	
	//main
	public static void main(String[] args) {		
		
		//Konstruktor
		Circle myCircle = new Circle();
		
		//Setteraufruf
		myCircle.setRadius(5);
		
		//Methodenaufruf und Ausgabe auf Console
		System.out.println(myCircle.getSurfaceArea());
		System.out.println(myCircle.getPeriphery());
		
	}


}
