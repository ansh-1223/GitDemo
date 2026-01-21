import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;

public class UpdatedDropdown {

	public static void main(String[] args) throws InterruptedException {
		// TODO Auto-generated method stub
		
		WebDriver driver=new ChromeDriver();
		driver.get("https://rahulshettyacademy.com/dropdownsPractise/");
		//assert false will accept a false
		Assert.assertFalse(driver.findElement(By.cssSelector("input[id *= SeniorCitizenDiscount]")).isSelected());
		//selecting check box
		driver.findElement(By.cssSelector("input[id *= SeniorCitizenDiscount]")).click();
		Assert.assertTrue(driver.findElement(By.cssSelector("input[id *= SeniorCitizenDiscount]")).isSelected());
		
		//Counting number of checkboxes
		System.out.println(driver.findElements(By.cssSelector("input[type='checkbox']")).size());
		driver.findElement(By.id("divpaxinfo")).click();
		Thread.sleep(2000L);
		
		
		for(int i =1;i<5;i++) {
			driver.findElement(By.id("hrefIncAdt")).click();
		}
		 driver.findElement(By.id("btnclosepaxoption")).click();
		Assert.assertEquals(driver.findElement(By.id("divpaxinfo")).getText(), "5 Adult");
		
		
		//System.out.println(driver.findElement(By.name("ctl00$mainContent$view_date2")).isEnabled());
		System.out.println(driver.findElement(By.id("Div1")).getDomAttribute("style"));
		driver.findElement(By.id("ctl00_mainContent_rbtnl_Trip_1")).click();
		System.out.println(driver.findElement(By.id("Div1")).getDomAttribute("style"));
		if(driver.findElement(By.id("Div1")).getDomAttribute("style").contains("1")) {
			System.out.println("its enabled");
				Assert.assertTrue(true);
		}
		else {
			Assert.assertTrue(false);

		

	}

}}
