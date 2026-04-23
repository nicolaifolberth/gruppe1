package snippets.sample5;

/**
 * 	Testklasse für die beiden Shops
 */
public class ShopExecute {


	public static void main(String[] args) {
			
		//SimpleShop
		SimpleShop mySimpleshop = new SimpleShop("Apple", 23.42);	
		mySimpleshop.setOfficeState(OfficeState.OPEN);	
		
			
		//Complex Shop		
		ComplexShop myComplexShop = new ComplexShop();				
		myComplexShop.setProductName("Banana");
		myComplexShop.setServiceName("peel");
		
		myComplexShop.setOfficeState(OfficeState.OPEN);	
		
		
		//Offers
		System.out.println(mySimpleshop);
		System.out.println(myComplexShop);
		
		
		
		
	}
	
	
	
	

}
