import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;

public class Practiceassignemnetui {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		WebDriver driver=new ChromeDriver();
		driver.get("https://rahulshettyacademy.com/angularpractice/");
		driver.findElement(By.name("name")).sendKeys("Anshuman");
		driver.findElement(By.name("email")).sendKeys("anshuman_1234@rediffmail.com");
		driver.findElement(By.id("exampleInputPassword1")).sendKeys("Anshu@1234");
		driver.findElement(By.id("exampleCheck1")).click();
		
		WebElement staticDropdown= driver.findElement(By.id("exampleFormControlSelect1"));
		Select dropdown= new Select(staticDropdown);
		dropdown.selectByIndex(0);
		
		driver.findElement(By.id("inlineRadio1")).click();
		




	}

}
