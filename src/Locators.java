
import java.io.File;
import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class Locators {

	public static void main(String[] args) throws InterruptedException {
		// TODO Auto-generated method stub

		WebDriver driver = new ChromeDriver();
		//use $('') in console instead of selectors hub

		driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(5));//solves synchronization issues,waits for 5 seconds till all things load up on the page
	    driver.get("https://rahulshettyacademy.com/locatorspractice/");
	    driver.findElement(By.id("inputUsername")).sendKeys("anshuman");
	    driver.findElement(By.name("inputPassword")).sendKeys("1234");
	    driver.findElement(By.className("signInBtn")).click();
	    System.out.println(driver.findElement(By.cssSelector("p.error")).getText());
	    driver.findElement(By.linkText("Forgot your password?")).click();
	    Thread.sleep(1000);//used to allow objects to load on new page when view is changing
	    driver.findElement(By.xpath("//input[@placeholder='Name']")).sendKeys("Anshuman");
	    driver.findElement(By.cssSelector("input[placeholder='Email']")).sendKeys("anshuman_1999@rediffmail.com");
	    driver.findElement(By.xpath("//input[@type='text'][2]")).clear();
	    driver.findElement(By.cssSelector("input[type='text']:nth-child(3)")).sendKeys("anshuman_1999@rediffmail.com");
	    driver.findElement(By.xpath("//form/input[3]")).sendKeys("12345678");
	    driver.findElement(By.cssSelector(".reset-pwd-btn")).click();
	    System.out.println(driver.findElement(By.cssSelector("form p")).getText());
	    
	    Thread.sleep(1000);
	    driver.findElement(By.xpath("//div[@class='forgot-pwd-btn-conainer']/button[1]")).click();
        driver.findElement(By.cssSelector("#inputUsername")).sendKeys("rahul");
	    driver.findElement(By.cssSelector("input[type*='pass']")).sendKeys("rahulshettyacademy");
	    driver.findElement(By.id("chkboxOne")).click();
	    driver.findElement(By.xpath("//button[contains(@class,'submit')]")).click();
	    

	}
	

}
