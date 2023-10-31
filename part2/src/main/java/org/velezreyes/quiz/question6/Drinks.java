package org.velezreyes.quiz.question6;

public enum Drinks implements Drink {
	SCOTTCOLA("ScottCola", true, 0.75), 
	KARENTEA("KarenTea", false, 1);

	private String name;
	private boolean fizzy; 
	public double price;
	
	private Drinks(String name, boolean fizzy, double price) {
		this.name = name;
		this.fizzy = fizzy;
		this.price = price;
	}
	
	@Override
	public String getName() {
		// TODO Auto-generated method stub
		return this.name;
	}

	@Override
	public boolean isFizzy() {
		// TODO Auto-generated method stub
		return this.fizzy;
	}

}
