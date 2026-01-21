import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class Locators3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		WebDriver driver = new ChromeDriver();
		driver.get("https://rahulshettyacademy.com/practice-project");
		System.out.println(driver.findElement(By.xpath("//div/h2/following-sibling::div")).getText());//from child to child traversal
		System.out.println(driver.findElement(By.xpath("//div/h2/parent::div/h2")).getText());//from child to parent

	}

}
