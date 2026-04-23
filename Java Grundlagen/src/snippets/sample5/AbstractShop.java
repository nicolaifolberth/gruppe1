package snippets.sample5;

import snippets.sample5.OfficeState;

/**
 * 	Abstrakte Klasse
 */
public abstract class AbstractShop {
	
//	officeState Attribut
	private OfficeState officeState; 

	public OfficeState getOfficeState() {
		return officeState;
	}

	public void setOfficeState(OfficeState officeState) {
		this.officeState = officeState;
	}
	
	
//	ToString-Methode überschreiben
	public String toString(){
		switch (getOfficeState()) {
		case OPEN:			
			return getOffers() + "\n"; 
		case CLOSED:
			return "The Shop is closed." + "\n"; 
		case CLOSING:
			return "Sorry, too late..." + "\n"; 
		default:
			return "Error" + "\n"; 
		}
		
	}


//	Abstrakte Methode
	public abstract String getOffers();

}
