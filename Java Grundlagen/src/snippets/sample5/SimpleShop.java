package snippets.sample5;

/**
 * 	Klasse erbt von abstrakter Klasse AbstractShop 
 *  und implementierung das Interfaces IProductShop
 */
public class SimpleShop extends AbstractShop implements IProductShop{

//	Private Attribute
	private double productPrice;
	private String productName;
	
//	Konstruktor	
	public SimpleShop(String productName, double price){
		this.productPrice = price;
		setProductName(productName);
	}
	
//	Methodenimplementierung der Interfaces		
	@Override
	public void setProductName(String productName) {
		this.productName = "Best " + productName;		
	}

	
//	Methodenimplementierung der abstrakten Klasse	
	@Override
	public String getOffers() {
		return	"The Shop is: " + getOfficeState() + "\n" +
				"The product " + productName + " will cost: " + productPrice * (100 + taxInPercant) / 100;
	}		

}
