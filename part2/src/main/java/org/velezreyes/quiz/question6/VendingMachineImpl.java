package org.velezreyes.quiz.question6;

public class VendingMachineImpl  implements VendingMachine{
	private double money = 0;
	
	public static VendingMachine getInstance() {
		return new VendingMachineImpl();
	}

	@Override
	public void insertQuarter() {
		this.money += 0.25;
	}
	
	@Override
	public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
		if(this.money == 0) throw new NotEnoughMoneyException();
		
		Drinks drink = null;
		if(name.equals("ScottCola")){
				drink = Drinks.SCOTTCOLA;
		}else if(name.equals("KarenTea")) {
				drink = Drinks.KARENTEA;
		}else {
			throw new UnknownDrinkException();
		}
		
		if(this.money < drink.price) throw new NotEnoughMoneyException();
		this.money = 0;
		
		return (Drink) drink;
	}
}
