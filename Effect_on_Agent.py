import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner
import time



class EffectonAgent_1Class(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     service = Service(ChromeDriverManager().install())
    #     cls.driver = webdriver.Chrome(service=service)
    #     cls.driver.maximize_window()

    #     # Fail-fast wait for elements (5 seconds)
    #     cls.fast_wait = WebDriverWait(cls.driver, 5)
    #     # Longer wait for page load/navigation (20 seconds)
    #     cls.long_wait = WebDriverWait(cls.driver, 20)

    #     cls.screenshot_dir = os.path.join(os.getcwd(), "Screenshots")
    #     os.makedirs(cls.screenshot_dir, exist_ok=True)
    @classmethod
    def setUpClass(cls):
        # Chrome options for CI + local execution
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        # Setup driver
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service, options=options)

        # Waits
        cls.fast_wait = WebDriverWait(cls.driver, 5)   # quick checks
        cls.long_wait = WebDriverWait(cls.driver, 20)   # page loads

        # Screenshot directory
        cls.screenshot_dir = os.path.join(os.getcwd(), "Screenshots")
        os.makedirs(cls.screenshot_dir, exist_ok=True)

    def take_screenshot(self, name):
        path = os.path.join(self.screenshot_dir, f"{name}_{int(time.time())}.png")
        self.driver.save_screenshot(path)
        print(f"Screenshot saved: {path}")
        return path

    # # ---------------- CNIC (FAIL FAST) ----------------
    # def fill_cnic_field(self, cnic):
    #     try:
    #         cnic_input = self.fast_wait.until(
    #             EC.element_to_be_clickable(
    #                 (By.XPATH, "//div[@id='non-existing-customer']//input[@formcontrolname='cnic']")
    #             )
    #         )
    #         self.driver.execute_script("arguments[0].value = arguments[1];", cnic_input, cnic)
    #         cnic_input.send_keys(Keys.TAB)
    #     except TimeoutException:
    #         self.take_screenshot("cnic_fail")
    #         self.fail("CNIC field not interactable within 5 seconds")




    def fill_cnic_field(self, cnic):
        try:
            cnic_input = self.fast_wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[@id='non-existing-customer']//input[@formcontrolname='cnic']")
                )
            )
            # Clear first
            self.driver.execute_script("arguments[0].value = '';", cnic_input)
            
            # Set value
            self.driver.execute_script(f"arguments[0].value = '{cnic}';", cnic_input)
            
            # Dispatch Angular events
            self.driver.execute_script("""
                arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
                arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
                arguments[0].dispatchEvent(new Event('blur', { bubbles: true }));
            """, cnic_input)

            # Optional: send TAB for extra safety
            cnic_input.send_keys(Keys.TAB)

        except TimeoutException:
            self.take_screenshot("cnic_fail")
            self.fail("CNIC field not interactable within 5 seconds")


    # ---------------- Checkbox (FAIL FAST) ----------------
    def click_checkbox(self, label_text):
        try:
            label = self.fast_wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//label[normalize-space()='{label_text}']")
                )
            )
            self.driver.execute_script("arguments[0].click();", label)
        except TimeoutException:
            self.take_screenshot(f"checkbox_{label_text}_fail")
            self.fail(f"Checkbox '{label_text}' not clickable within 5 seconds")

    # ---------------- Dropdown (FAIL FAST) ----------------
    def select_dropdown(self, label_text, option_text):
        try:
            label = self.fast_wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//label[normalize-space()='{label_text}']")
                )
            )
            dropdown = label.find_element(By.XPATH, "../following-sibling::div//mat-select")
            self.driver.execute_script("arguments[0].click();", dropdown)

            option = self.fast_wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//mat-option//span[normalize-space()='{option_text}']")
                )
            )
            self.driver.execute_script("arguments[0].click();", option)
        except TimeoutException:
            self.take_screenshot(f"dropdown_{label_text}_fail")
            self.fail(f"Dropdown '{label_text}' failed within 5 seconds")

    # ---------------- Radio (FAIL FAST) ----------------
    def select_radio(self, label_text, option_text):
        try:
            radio = self.fast_wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//label[contains(.,'{option_text}')]")
                )
            )
            self.driver.execute_script("arguments[0].click();", radio)
        except TimeoutException:
            self.take_screenshot(f"radio_{label_text}_fail")
            self.fail(f"Radio '{option_text}' not clickable within 5 seconds")

    # ---------------- MAIN TEST ----------------
    def test_registration(self):
        driver = self.driver

        # ---------------- LOGIN ----------------
        try:
            driver.get("https://pulsevideo.pulsecx.app/login")

            self.fast_wait.until(
                EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='userName']"))
            ).send_keys("rashid.minha")

            self.fast_wait.until(
                EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='password']"))
            ).send_keys("Agent@123")

            self.fast_wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[@type='submit']")
                )
            ).click()

            print("Login successful!")

        except TimeoutException:
            self.take_screenshot("login_fail")
            self.fail("Login failed within 5 seconds")

        # ---------------- NAVIGATION ----------------
        # Online Not Ready
        self.long_wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Online Not Ready')]"))
        ).click()

        # ✅ Raqami Back Office step restored
        self.long_wait.until(
            EC.element_to_be_clickable((By.XPATH, "//label[.//div[contains(.,'Back Office')]]"))
        ).click()

        # SR Buckets
        self.long_wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@routerlink='sr-buckets']"))
        ).click()
        time.sleep(5)


        # Search Customer
        self.long_wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Search Customer')]"))
        ).click()
        time.sleep(3)


        # Switch to new window
        self.long_wait.until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[-1])

        # Non-existing customer tab
        self.fast_wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='#non-existing-customer']"))
        ).click()
        time.sleep(3)

        # -------------------------
        self.fill_cnic_field("4240127884017")
        time.sleep(4)
        
        self.fast_wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='non-existing-customer']//button[.//span[contains(.,'Search')]]"))
        ).click()
        time.sleep(4)

        # Wait for the Service Request link to be clickable and click it
        service_request_link = self.fast_wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[@href='#srmenu' and contains(@class,'sr-link') and span[normalize-space()='Service Request']]")
            )
        )
        # Scroll into view (Angular-safe) and click via JS
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", service_request_link)
        self.driver.execute_script("arguments[0].click();", service_request_link)

        self.fast_wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='SR Registration']"))
        ).click()




        # for service in ["Account Maintenance", "Closed Account", "TEST Mobile Topup 25"]:
        #         elem = self.fast_wait.until(EC.presence_of_element_located((By.XPATH, f"//div[contains(@class,'mat-list-text') and normalize-space()='{service}']")))
        #         driver.execute_script("arguments[0].scrollIntoView({block:'center'});", elem)
        #         time.sleep(0.6)
        #         driver.execute_script("arguments[0].click();", elem)
        #         time.sleep(1.5)
            




        # Step 1: Select required fixed services
        fixed_services = ["Account Maintenance", "Closed Account"]

        for service in fixed_services:
            elem = self.fast_wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//div[contains(@class,'mat-list-text') and normalize-space()='{service}']")
                )
            )
            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", elem
            )
            time.sleep(0.4)
            driver.execute_script(
                "arguments[0].click();", elem
            )
            time.sleep(1)

        # Step 2: Select the last service (dynamic)
        services = self.fast_wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[contains(@class,'mat-list-text')]")
            )
        )

        last_service = services[-1]

        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", last_service
        )
        time.sleep(0.4)
        driver.execute_script(
            "arguments[0].click();", last_service
        )

        time.sleep(1.5)


        # ---------------- FORM ----------------
        
        self.fast_wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='First Name']"))
        ).send_keys("Rashid")

        # # Checkbox
        # self.click_checkbox("Test CheckBox")

        # # Dropdown
        # self.select_dropdown("Test Dropdown", "Business")

        # # Radio
        # self.select_radio("Test RadioButton", "Male")

        # # Remarks
        # remarks = self.fast_wait.until(
        #     EC.element_to_be_clickable((By.XPATH, "//textarea[@formcontrolname='remarks']"))
        # )
        # remarks.send_keys("Fail-fast automation test")

        # Save button
        self.fast_wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@type='submit' and .//span[normalize-space()='Save']]")
            )
        ).click()

        print("Test completed Save attempted")
        time.sleep(10)



       
       

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    os.makedirs("Reports", exist_ok=True)
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="Reports",
            report_title="Fail-Fast Selenium Report",
            combine_reports=True
        ),
        verbosity=2
    )
