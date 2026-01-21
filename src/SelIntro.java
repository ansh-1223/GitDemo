import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.WebDriver;


public class SelIntro {

	public static void main(String[] args) {
		
	//invoking chrome browser
	//Chrome-chromdriver-methods
	//not using chromedriver class bacause it may have personal methods which we may access and it may not work for other web broswers
	//WebDriver driver = new ChromeDriver();
	
	//Firefox driver
	//for firefox there is gecko driver which sits between browser and firefox
	//WebDriver driver= new FirefoxDriver();
		
	//Edge driver	
	WebDriver driver = new EdgeDriver();	
	driver.get("https://www.youtube.com/");
	System.out.println(driver.getTitle());
	System.out.println(driver.getCurrentUrl());
	driver.close();
	}

}
