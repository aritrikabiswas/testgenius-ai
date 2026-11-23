
package ai.testgenius.runner;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.safari.SafariDriver;

public class BrowserAutomation {

    public static void main(String[] args) {

        WebDriver driver = null;

        try {

            // Launch Safari
            driver = new SafariDriver();

            // Open the example website
            driver.get("https://example.com");

            System.out.println("================================");
            System.out.println("TESTGENIUS AI - SAFARI RUNNER");
            System.out.println("================================");

            System.out.println("Browser: Safari");
            System.out.println("Page Title: " + driver.getTitle());
            System.out.println("Current URL: " + driver.getCurrentUrl());

            if ("Example Domain".equals(driver.getTitle())) {
                System.out.println("Browser automation successful!");
            } else {
                throw new RuntimeException("Page title verification failed.");
            }

        } catch (Exception exception) {

            System.err.println("Browser automation failed!");
            exception.printStackTrace();

        } finally {

            if (driver != null) {
                driver.quit();
                System.out.println("Safari closed successfully.");
            }
        }
    }
}
