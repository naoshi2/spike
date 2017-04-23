package behave;

public class Behave {
	public static void main(String[] args) {
		int x = 3;
		int y = 5;

		System.out.println("x: " + x + ", y: " + y + "\n");
		System.out.println(add(x,y));
		System.out.println(deduct(x, y));
		System.out.println(multiply(x, y));
		System.out.println(power(x, y));
	}
	
	public static int add(int x, int y){
		System.out.println("Add");
		return x + y;
	}
	
	public static int deduct(int x, int y){
		System.out.println("Deduct");
		return x - y;
	}
	
	public static int multiply(int x, int y){
		System.out.println("Multiply");
		return x * y;
	}
	
	public static double power(int x, int y){
		System.out.println("Power");
		return Math.pow((double)x, (double)y);
	}
}
