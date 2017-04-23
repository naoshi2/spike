package behave;

import static org.junit.Assert.*;

import org.jbehave.core.annotations.Given;
import org.jbehave.core.annotations.When;
import org.jbehave.core.annotations.Then;

public class BehaveSteps {
	int x;
	int y;

	@Given("a variable x with value $x")
	public void testAdd(int x) {
		this.x = x;
	}

	@When("another variable y with value $y")
	public void testDeduct(int y) {
		this.y = y;
	}

	@Then("answer should equal $z")
	public void testMultiply(int z) {
		assertEquals(Behave.multiply(x, y), z);
	}
}
