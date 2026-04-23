package snippets.sample5;

/**
 * 	Klasse erbt von abstrakter Klasse AbstractShop 
 *  und implementierung die Interfaces IProductShop und IServiceShop
 */
public class ComplexShop extends AbstractShop implements IProductShop, IServiceShop{

//	Attribute
	private String serviceName;	
	private String productName;

	
//	Der Standardkonstruktor wird automatisch angelegt		
	
	
//	Methodenimplementierung der Interfaces	
	@Override
	public void setServiceName(String serviceName) {
		this.serviceName = serviceName;		
	}

	@Override
	public void setProductName(String productName) {
		this.productName = productName;		
	}

	
//	Methodenimplementierung der abstrakten Klasse
	@Override
	public String getOffers() {
		return 	"The Shop is: " + getOfficeState() + "\n" +
				"Product offer: " + productName + "\n" +
				"Price 42,59 (TAX " + IProductShop.taxInPercant + "%)" + "\n" +
				"Service offer: " + serviceName + "\n" +
				"Price 12.50 (TAX " + IServiceShop.taxInPercant + "%)";
	}

}
