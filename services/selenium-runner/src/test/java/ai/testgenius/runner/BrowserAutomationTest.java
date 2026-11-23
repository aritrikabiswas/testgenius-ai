
package ai.testgenius.runner;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.junit.jupiter.api.extension.ExtensionContext;
import org.junit.jupiter.api.extension.TestWatcher;

import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.safari.SafariDriver;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

@ExtendWith(BrowserAutomationTest.FailureEvidenceExtension.class)
class BrowserAutomationTest {

    private WebDriver driver;

    @BeforeEach
    void setUp() {
        System.out.println("Starting Safari browser...");
        driver = new SafariDriver();
    }

    @Test
    void shouldOpenExampleWebsiteSuccessfully() throws Throwable {

        try {
            driver.get("https://example.com");

            String actualTitle = driver.getTitle();

            System.out.println("================================");
            System.out.println("TESTGENIUS AI - SAFARI TEST");
            System.out.println("================================");

            System.out.println("Browser: Safari");
            System.out.println("Page Title: " + actualTitle);
            System.out.println("Current URL: " + driver.getCurrentUrl());

            assertEquals(
               "Example Domain",
                actualTitle,
                "Website title should match the expected title"
            );

            assertTrue(
                driver.getCurrentUrl().contains("example.com"),
                "Safari should navigate to example.com"
            );

            captureScreenshot("safari-example-test");

            System.out.println("Safari browser test passed!");

        } catch (Throwable failure) {

            System.err.println("TESTGENIUS AI: Capturing failure evidence...");

            try {
                captureScreenshot("safari-test-failure");

                System.out.println(
                    "Failure screenshot captured successfully."
                );

            } catch (Exception screenshotError) {

                System.err.println(
                    "Failure screenshot could not be captured: "
                    + screenshotError.getMessage()
                );

                failure.addSuppressed(screenshotError);
            }

            throw failure;
        }
    }

    private void captureScreenshot(String fileName) throws IOException {

        if (driver == null) {
            throw new IllegalStateException("Safari driver is unavailable.");
        }

        File screenshot = ((TakesScreenshot) driver)
                .getScreenshotAs(OutputType.FILE);

        Path directory = Paths.get("artifacts", "screenshots");

        Files.createDirectories(directory);

        Path destination = directory.resolve(fileName + ".png");

        Files.copy(
            screenshot.toPath(),
            destination,
            StandardCopyOption.REPLACE_EXISTING
        );

        System.out.println("Screenshot saved: " + destination);
    }

    @AfterEach
    void tearDown() {

        if (driver != null) {
            driver.quit();
            driver = null;

            System.out.println("Safari closed successfully.");
        }
    }

    static class FailureEvidenceExtension implements TestWatcher {

        @Override
        public void testFailed(
            ExtensionContext context,
            Throwable cause
        ) {

            System.err.println("================================");
            System.err.println("TESTGENIUS AI - TEST FAILURE");
            System.err.println("================================");

            System.err.println(
                "Failed Test: " + context.getDisplayName()
            );

            System.err.println(
                "Failure Reason: " + cause.getMessage()
            );

            cause.printStackTrace();
        }

        @Override
        public void testSuccessful(ExtensionContext context) {

            System.out.println(
                "TESTGENIUS AI: Test passed - "
                + context.getDisplayName()
            );
        }
    }
}
