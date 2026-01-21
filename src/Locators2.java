import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.edge.EdgeDriver;
import org.testng.Assert;

public class Locators2 {
	public static void main(String[] args) throws InterruptedException {
		
		//WebDriver driver = new ChromeDriver();
		WebDriver driver= new EdgeDriver();
		String name="Anshuman";
		driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(5));//solves synchronization issues,waits for 5 seconds till all things load up on the page
	    String password=getPassword(driver);
		driver.get("https://rahulshettyacademy.com/locatorspractice/");
	    driver.findElement(By.id("inputUsername")).sendKeys(name);
	    driver.findElement(By.name("inputPassword")).sendKeys(password);
	    driver.findElement(By.className("signInBtn")).click();
	    Thread.sleep(1000);
	    System.out.println(driver.findElement(By.tagName("p")).getText());
	    Assert.assertEquals(driver.findElement(By.tagName("p")).getText(),"You are successfully logged in.");
	    Assert.assertEquals(driver.findElement(By.cssSelector("div[class='login-container'] h2")).getText(),"Hello "+name+",");
	    driver.findElement(By.xpath("//button[text()='Log Out']")).click();
	    driver.close();
	}
	public static String getPassword(WebDriver driver) throws InterruptedException {
	    driver.get("https://rahulshettyacademy.com/locatorspractice/");
	    driver.findElement(By.linkText("Forgot your password?")).click();
	    Thread.sleep(1000);
	    driver.findElement(By.cssSelector(".reset-pwd-btn")).click();
	    String passwordText=driver.findElement(By.cssSelector("form p")).getText();
	    String[] passwordArray=passwordText.split("'");
	    String password=passwordArray[1].split("'")[0];
	    return password;
	}
	

}
