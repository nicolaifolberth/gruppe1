package snippets_vorlesung.sample2;

/**
 * Attribute
 * Variablen  
 * Methoden
 * Getter & Setter
 * Objekte
 */
public class Circle {

	public double getRadius() {
		return radius;
	}

	public void setRadius(double radius) {
		this.radius = radius;
	}

	//radius
	private double radius;
		
	//PI = 3.1416
	public final static double PI = 3.1416;
	
	
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

		Circle myCircle = new Circle();

		myCircle.setRadius(9.2);

		System.out.println(myCircle.getSurfaceArea());
		System.out.println(myCircle.getPeriphery());

		Circle myOtherCircle = new Circle();



		myOtherCircle = myCircle;

		myOtherCircle.setRadius(2);

		System.out.println(myCircle.getSurfaceArea());
		System.out.println(myCircle.getPeriphery());

		System.out.println(myOtherCircle.getSurfaceArea());
		System.out.println(myOtherCircle.getPeriphery());

	}



	





}
