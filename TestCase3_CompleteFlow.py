import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner
from uuid import uuid4
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver import ActionChains




class TestCase3_CompleteFlowFunction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 30)
        cls.fast_wait = WebDriverWait(cls.driver, 10)  # Fast wait for campaign assignment & quick clicks


        cls.screenshot_dir = os.path.join(os.getcwd(), "Screenshots")
        if not os.path.exists(cls.screenshot_dir):
            os.makedirs(cls.screenshot_dir)

    def take_screenshot(self, name):
        path = os.path.join(self.screenshot_dir, f"{name}.png")
        self.driver.save_screenshot(path)
        return path

    def safe_js_click(self, element):
        """Scroll into view and click element via JavaScript to avoid interception."""
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        time.sleep(0.5)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)

    def test_registration(self):
        driver = self.driver
        wait = self.wait

    # ---------------- Safe JS Click Method ----------------
    def safe_js_click(self, element):
        """Clicks an element using JavaScript safely."""
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
            self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            self.take_screenshot("js_click_failure")
            raise Exception(f"JS click failed on element: {e}")

 # ----------------------- helper function for Angular Material dropdowns -------------------
    def select_mat_dropdown(self, dropdown_text, option_text):
        wait = self.wait
        # 1️⃣ Click the dropdown to open
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//span[normalize-space()='{dropdown_text}']")
        )).click()
        # 2️⃣ Wait for the option to appear in overlay
        wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//span[@class='mat-option-text' and normalize-space()='{option_text}']")
        ))
        # 3️⃣ Click the option
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//span[@class='mat-option-text' and normalize-space()='{option_text}']")
        )).click()
   
    def test_registration(self):
        driver = self.driver
        wait = self.wait

        # ----------------- Variables -----------------
        calendar_name = "OutBound Test Calender"
        description_text = "This is a sample OutBound Test Calender"
        start_date = "01-02-2026"  #mm/dd/yyyy
        end_date = "01-29-2026"
        
         # -----------------------variables---------------------------
        Department_1 = "HBL Backend Team"
        Department_2 = "HBL Onboarding"
        Department_3 = "HBL ADC"
        Department_4 = "HBL Onboarding Complaint"
        department_names = [Department_1, Department_2, Department_3, Department_4]


        organization_name_negative = f"789789vhgvchgvh-=-=-=0__)%5%&!!@@$$&&||_{uuid4().hex[:4]}"
        Department_1_negative = "7878ugyufyu++__)((%%#$#4"
        Department_2_negative = "###@@@@@%%^^&&**((!!!!!!"
        Department_3_negative = " "
        department_names_negative = [Department_1_negative, Department_2_negative, Department_3_negative, Department_4]
        # -----------------------variables---------------------------
        username="rashid.minha"
        password="Agent@123"
        Business_Unit = f"Backend Team"
        product_name_in_Reason_first = f"Staff Behaviour"
        product_name = "Staff Behaviour"
        reason_name_in_Reason = "AML Screening New"
        product_name_in_sub_Reason_first = f"Staff Behaviour"
        reason_name_in_sub_Reason_second = f"AML Screening New"
        sub_reason = "Money Laundring Issue"
         # -----------------------variables---------------------------
        organization_name = f"HBL Bank {uuid4().hex[:4]}"
        Department_1 = "HBL Backend Team"
        Department_2 = "HBL Onboarding"
        Department_3 = "HBL ADC"
        Department_4 = "HBL Onboarding Complaint"
        department_names = [Department_1, Department_2, Department_3, Department_4]


        organization_name_negative = f"789789vhgvchgvh-=-=-=0__)%5%&!!@@$$&&||_{uuid4().hex[:4]}"
        Department_1_negative = "7878ugyufyu++__)((%%#$#4"
        Department_2_negative = "###@@@@@%%^^&&**((!!!!!!"
        Department_3_negative = " "
        department_names_negative = [Department_1_negative, Department_2_negative, Department_3_negative, Department_4]
        # -----------------------variables---------------------------
        # Dynamic resolution owner names
        resolution_owner_name = f"MBL Customer Onboarding Test {uuid4().hex[:4]}"
        SECOND_resolution_owner_name = f"HBL ADC TEST {uuid4().hex[:4]}"
        negative_resolution_owner_name1 = f"test7687++__))(**%%^^$$##@@!!@~~ {uuid4().hex[:4]}"
        owner_email = "test1.mbl@mbl.com"
        negative_owner_email = f"test456-++_)(**&&^^%%$$##{uuid4().hex[:4]}@gmail.com"
        escalation_level1_email = "test1.mbl@mbl.com"
        escalation_level2_email = "test2.mbl@mbl.com"
        escalation_level3_email = "test3.mbl@mbl.com"
        Select_an_Organization = "Select an Organization"
        Organization_name1 = "Meezan Bank"

        Select_a_Department = "Select a Department"
        Department_name1 = "Meezan Onboarding"
        Select_an_Organization_second_RO = "Select an Organization"
        Organization_name1_second_RO= "HBL Bank"
        Select_a_Department_second_RO = "Select a Department"
        Department_name1_second_RO = "HBL ADC"
        negative_escalation_level1_email = "ewew4$$%^&*())}|@gmail.com"
        negative_escalation_level2_email = "ewew4$$%^&*())}|uug09090-9-00"
        negative_escalation_level3_email = " "
        # -----------------------variables---------------------------
        SR_NAME = f"TEST Mobile Topup {uuid4().hex[:4]}"
        product_option = "Account Maintenance Test"
        reason_option = "Test Reason"
        # collection_option = "Collection"
        collection_option = "Service Request"
        sub_reason = "Sub Test Reason"
        internal_tat = "30"
        reopen_tat = "30"
        routing_method = "Automatic"
        priority_option = "High"
        brief_summary = "This is test service"
        resolution_owner = "ADC"
        tat1_value = "10"
        tat2_value = "20"
        tat3_value = "30"
        sr_stage = "InProgress"
        label_value_text = "First Name"
        label_value_checkBox = "Test CheckBox"
        label_value_dropdown = "Test Dropdown"
        label_value_radiobutton = "Test RadioButton"
        field_type_text = "TextBox"
        data_format_text = "Text"
        screen_position_1 = "1"
        screen_position_2 = "2"
        screen_position_3 = "3"
        screen_position_4 = "4"
        field_type_checkbox = "CheckBox"
        field_type_dropdown = "Dropdown"
        field_type_radiobutton = "Radio Button"
        data_format_checkbox = "Boolean"
        data_format_dropdown = "Text"
        data_format_radiobutton = "Text"
        Enter_dropdown_options = "Business,Individual"
        Enter_radiobutton_options = "Male,Female"

        # -----------------------variables---------------------------
       
        





        # -------------------------- LOGIN ---------------------------------------------------
        try:
            driver.get("https://pulsevideo.pulsecx.app/login")
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='userName']"))).send_keys("rashid.minha")
            wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='password']"))).send_keys("Agent@123")
            wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='loginAsSupervisor']"))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and span[text()='Login']]"))).click()
            print("Login successful!")
            time.sleep(5)
        except Exception as e:
            self.take_screenshot("login_failure")
            self.fail(f"Login failed: {e}")




        # ----------------------------------- Make New Calender Test Case -----------------
                            
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@routerlink='/supervisor/configuration' and span[text()='Configuration']]"))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@routerlink='management' and text()='Management']"))).click()
            time.sleep(2)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@routerlink='calendar' and text()='Calendar']"))).click()
            time.sleep(2)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Add New'] or contains(text(),'Add New')]"))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='calendarName']"))).send_keys(calendar_name)
            time.sleep(1)
            
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='description']"))).send_keys(description_text)
            time.sleep(1)
            
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='startDate']"))).send_keys(start_date)
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='endDate']"))).send_keys(end_date)
            time.sleep(1)

            # Start Time value
            start_time_value = "09:00"  # 9 AM in 24-hour format

            # Locate the input
            start_time_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='startTime']")))

            # Set value via JS
            driver.execute_script("arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input')); arguments[0].dispatchEvent(new Event('change'));", start_time_input, start_time_value)

            # Optional: verify
            print("Start Time set to:", start_time_input.get_attribute("value"))


            # End Time 5:00 PM
            end_time = "17:00"  # 5:00 PM in 24-hour format
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='endtime']"))).send_keys(end_time)
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='satWeekend' and text()='Saturday As Weekend']"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='sunWeekend' and text()='Sunday As Weekend']"))).click()
            time.sleep(3)
            add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(., 'Add')]")))
            driver.execute_script("arguments[0].scrollIntoView(true);", add_button)
            add_button.click()
            time.sleep(10)

        except Exception as e:
            self.take_screenshot("Agent_Listing_failure")
            self.fail(f"Agent Listing failed: {e}")
        


        # ----------------------------------- Make New Skill Test Case -----------------
        # ---------- 1-Skill-BackOffice Positive Test Case -----------------
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[@routerlink='/supervisor/configuration' and span[text()='Configuration']]"))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[@routerlink='skill-management' and text()='Skill Management']"))).click()
            time.sleep(2)

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[span[text()='Add New'] or contains(text(),'Add New')]"))).click()
            time.sleep(1)

            Skill_Name_BackOffice= "BackOffice Test Skill"
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@formcontrolname='name']"))).send_keys(Skill_Name_BackOffice)

            # ----------------- Channel Dropdown -----------------
            channel_text_BackOffice = "BackOffice"
            channel_mat_select = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//mat-select[@formcontrolname='channelId']")))
            channel_trigger = channel_mat_select.find_element(By.CSS_SELECTOR, "div.mat-select-trigger")
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", channel_trigger)
            driver.execute_script("arguments[0].click();", channel_trigger)
            time.sleep(1)
            channel_option = wait.until(EC.presence_of_element_located(
                (By.XPATH, f"//div[contains(@class,'cdk-overlay-pane')]//span[normalize-space()='{channel_text_BackOffice}']")))
            driver.execute_script("arguments[0].click();", channel_option)
            time.sleep(2)

           
            # ----------------- Slider -----------------
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//mat-slider[@formcontrolname='skillLevel']"))).send_keys(Keys.ARROW_RIGHT)

            # ----------------- Description -----------------
            description_text = "This is a sample description"
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//textarea[@formcontrolname='description']"))).send_keys(description_text)

            time.sleep(5)
            
            # ----------------- Add Button -----------------
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@type='submit' and normalize-space()='Add']"))).click()

        except Exception as e:
            self.take_screenshot("Agent_Listing_failure")
            self.fail(f"Agent Listing failed: {e}")




        # ----------------------------------- Make New Skill Test Case-2 -----------------
        # -----------------------------Call Back--------------------------------
        # -----2-Skill-Call Back Positive Test Case -----------------
        try:
            # wait.until(EC.element_to_be_clickable(
            #     (By.XPATH, "//a[@routerlink='/supervisor/configuration' and span[text()='Configuration']]"))).click()
            # time.sleep(1)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[@routerlink='skill-management' and text()='Skill Management']"))).click()
            time.sleep(2)

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[span[text()='Add New'] or contains(text(),'Add New')]"))).click()
            time.sleep(1)

            Skill_Name_Call_Back = "Call Back Test Skill"
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@formcontrolname='name']"))).send_keys(Skill_Name_Call_Back)

            # ----------------- Channel Dropdown -----------------
            channel_text_CallBack = "Call Back"
            channel_mat_select = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//mat-select[@formcontrolname='channelId']")))
            channel_trigger = channel_mat_select.find_element(By.CSS_SELECTOR, "div.mat-select-trigger")
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", channel_trigger)
            driver.execute_script("arguments[0].click();", channel_trigger)
            time.sleep(1)
            channel_option = wait.until(EC.presence_of_element_located(
                (By.XPATH, f"//div[contains(@class,'cdk-overlay-pane')]//span[normalize-space()='{channel_text_CallBack}']")))
            driver.execute_script("arguments[0].click();", channel_option)
            time.sleep(2)

           
            # ----------------- Slider -----------------
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//mat-slider[@formcontrolname='skillLevel']"))).send_keys(Keys.ARROW_RIGHT)

            # ----------------- Description -----------------
            description_text = "This is a sample description"
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//textarea[@formcontrolname='description']"))).send_keys(description_text)

            time.sleep(5)
            
            # ----------------- Add Button -----------------
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@type='submit' and normalize-space()='Add']"))).click()

        except Exception as e:
            self.take_screenshot("Agent_Listing_failure")
            self.fail(f"Agent Listing failed: {e}")
        


        # ----------------------------------- Make New QUEUE Test Case -----------------
        # ----------------- BackOffice Voice Positive Test Case -----------------
        try:
            # Navigate to Backoffice Queue
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[@routerlink='/supervisor/configuration' and span[text()='Configuration']]")
            )).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[@routerlink='queue' and text()='Queue']")
            )).click()
            time.sleep(2)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[@routerlink='backoffice' and normalize-space()='Backoffice']")
            )).click()
            time.sleep(2)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[.//text()[normalize-space()='Add Queue']]")
            )).click()
            time.sleep(2)

            # ----------------- Dynamic Values -----------------
            
            queue_name_backoffice = f"Test Backoffice {uuid4().hex[:3]}"
            # skill_name_backoffice = f"Backend Team Service Request"
            skill_name_backoffice = f"ADC"
            organization_name = f"Meezan Bank"
            Organization_name_in_hirarchy = f"Meezan Bank {uuid4().hex[:4]}"
            department_name = f"Meezan Backend Team"
            business_unit = f"MBL Customer Onboarding Test"
            slider_value = random.randint(10, 90)  # slider between 10 and 90

            # ----------------- Fill Queue Name -----------------
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//input[@formcontrolname='queueName']")
            )).send_keys(queue_name_backoffice)

            # ----------------- Select Skill -----------------
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//mat-select[@formcontrolname='skillId']")
            )).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//span[@class='mat-option-text' and normalize-space()='{skill_name_backoffice}']")
            )).click()
            time.sleep(1)

            # ----------------- Select Organization -----------------
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//mat-select[@formcontrolname='organizationId']")
            )).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//mat-option//span[normalize-space()='{organization_name}']")
            )).click()
            time.sleep(1)

            # ----------------- Select Department -----------------
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//mat-select[@formcontrolname='departmentId']")
            )).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//mat-option//span[normalize-space()='{department_name}']")
            )).click()
            time.sleep(1)

            # ----------------- Select Business Unit -----------------
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//mat-select[@formcontrolname='businessUnitId']")
            )).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//mat-option//span[normalize-space()='{business_unit}']")
            )).click()
            time.sleep(1)



            # Wait until slider is present
            slider = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//mat-slider[@formcontrolname='weight']")
            ))

            # Desired value
            slider_value = 30
            min_val = int(slider.get_attribute("min"))
            max_val = int(slider.get_attribute("max"))

            # Calculate percentage to move
            percent = (slider_value - min_val) / (max_val - min_val)

            # Get slider size and location
            slider_width = slider.size['width']

            # Calculate pixel offset
            x_offset = int(slider_width * percent)

            # Drag thumb using ActionChains
            thumb = slider.find_element(By.CSS_SELECTOR, ".mat-slider-thumb")
            actions = ActionChains(driver)
            actions.click_and_hold(thumb).move_by_offset(x_offset - slider_width // 2, 0).release().perform()

            time.sleep(1)




            

            # ----------------- Click Add -----------------
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@type='submit' and .//span[normalize-space()='Add']]")
            )).click()
            time.sleep(5)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[contains(@class,'modal-header')]//div[contains(@class,'close-modal')]")
                )
            ).click()
            time.sleep(10)


        except Exception as e:
            self.take_screenshot("Agent_Listing_failure")
            self.fail(f"Agent Listing failed: {e}")
        



# --------------------------------------- Workflow Test Case Start--------------------------------
# --------------------------------------- Workflow Test Case Start--------------------------------



# ---------------------------------1-Hirarchy Module start-----------------------------------------------------------------

# ----------------------Hirarchy Making Journey-------------------------------------------
        # -----------------------Positive Test Case Start-----------------------------
        try:
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@routerlink='/supervisor/workflow' and span[text()='Work Flow']]"))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Hierarchy']") )).click()
            time.sleep(5)
            wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//h5[normalize-space()='Add Organization']")
            )).click()
            time.sleep(3)
            # Wait until the input is visible and interactable
            org_input = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@formcontrolname='organizationName' and @placeholder='Organization']")
            ))
            org_input.clear()  # optional, clears any pre-filled text
            # org_input.send_keys(organization_name)
            org_input.send_keys(Organization_name_in_hirarchy)
            

            time.sleep(5)

                        
            

            # List of department names

            for i, dept_name in enumerate(department_names):
                # Locate all current department input fields
                dept_inputs = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH, "//input[@formcontrolname='departmentName']")
                ))

                # Always take the last input field (newly added)
                dept_input = dept_inputs[-1]
                dept_input.clear()
                dept_input.send_keys(dept_name)

                # Click "Add More" for first three, skip for the last
                if i < len(department_names) - 1:
                    add_more_btn = wait.until(EC.element_to_be_clickable(
                        (By.XPATH, "//a[contains(@class,'add-department') and normalize-space()='Add More']")
                    ))
                    add_more_btn.click()
                    time.sleep(1)  # small wait for new input field to appear
                    # ----------------------------FOR LOOP END---------------------------------------

            time.sleep(5)
            # Wait until the button is clickable and click
            wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@class,'btn-save') and .//span[normalize-space()='Add']]")
            )).click()
            time.sleep(3)
            # wait.until(
            #     EC.element_to_be_clickable(
            #         (By.XPATH, "//div[contains(@class,'close-modal')]")
            #     )
            # ).click()

        except Exception as e:
            self.take_screenshot("Floor making failure")
            self.fail(f"Floor making failed: {e}")


                # -----------------------Positive Test Case End------------------------------


          
# ---------------------------------3-RO Module Start-------------------------------------------------------------------  


 # ----------------------First RO Making Journey-------------------------------------------
        # ----------------------RO Making Journey Positive Test Case Start------------------
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@routerlink='/supervisor/workflow' and span[text()='Work Flow']]"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Resolution Owner']") )).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Add RO']")
            )).click()

            # Resolution Owner Name
            owner_input = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@formcontrolname='buownerName' and @placeholder='Resolution Owner Name']")
            ))
            owner_input.send_keys(resolution_owner_name)

            # Owner Email
            email_input = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@formcontrolname='ownerEmail' and @placeholder='Owner Email Address']")
            ))
            email_input.clear()
            email_input.send_keys(owner_email)

            # ------------------- Select Organization Dropdown -------------------
            self.select_mat_dropdown(Select_an_Organization, Organization_name1)
            time.sleep(4)

            # ------------------- Select Department Dropdown -------------------
            self.select_mat_dropdown(Select_a_Department, Department_name1)

            # Escalation Emails
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@formcontrolname='escaltionLevel1EmailAddress' and @placeholder='Email Address']")
            )).send_keys(escalation_level1_email)

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@formcontrolname='escaltionLevel2EmailAddress' and @placeholder='Email Address']")
            )).send_keys(escalation_level2_email)

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@formcontrolname='escaltionLevel3EmailAddress' and @placeholder='Email Address']")
            )).send_keys(escalation_level3_email)

            time.sleep(5)

            # Click Add button
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[.//span[normalize-space()='Add']]")
            )).click()

            time.sleep(5)

        except Exception as e:
            self.take_screenshot("ro_making_journey_failure")
            self.fail(f"RO Making Journey failed: {e}")


        



        






        

# ---------------------------------3-RO Module End-------------------------------------------------------------------       




# ---------------------------------2-Product Module Start-------------------------------------------------------------------       
# ---------------------------Product Making Journey-------------------------------------------
        # ----------------------Positive Test Case Start-----------------------------
        try:
            time.sleep(3)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@routerlink='/supervisor/workflow' and .//span[normalize-space()='Work Flow']]")
                )
            ).click()

            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Product']") )).click()
            wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//button[normalize-space()='Add More'])[1]")
                )
            ).click()
            time.sleep(2)
            wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[normalize-space()='Select an Option']")
            )
            ).click()
            time.sleep(2)
            wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//mat-option//span[normalize-space()='{Business_Unit}']")
            )
            ).click()
            wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@formcontrolname='productName']")
            )
            ).send_keys(product_name)
            time.sleep(3)
            wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Add']")
            )
            ).click()

            time.sleep(4)              

        except Exception as e:
            self.take_screenshot("Floor making failure")
            self.fail(f"Floor making failed: {e}")
        

        # ----------------------Reason Making Journey-------------------------------------------
        # ----------------------Positive Test Case Start-----------------------------
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@routerlink='/supervisor/workflow' and span[text()='Work Flow']]"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Product']") )).click()
            wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//button[normalize-space()='Add More'])[2]")
                )
            ).click()
            time.sleep(4)
            wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class,'mat-select-trigger')]//span[normalize-space()='Select a Product']")
            )
            ).click()

            time.sleep(2)
            wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//mat-option//span[normalize-space()='{product_name_in_Reason_first}']")
            )
            ).click()
            wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@formcontrolname='reason']")
            )
            ).send_keys(reason_name_in_Reason)
            time.sleep(3)
            wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Add']")
            )
            ).click()

            time.sleep(4)              

        except Exception as e:
            self.take_screenshot("Floor making failure")
            self.fail(f"Floor making failed: {e}")
        

        # ----------------------Sub Reason Making Journey-------------------------------------------
        # ----------------------Positive Test Case Start-----------------------------
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@routerlink='/supervisor/workflow' and span[text()='Work Flow']]"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Product']") )).click()
            time.sleep(3)

            # Locate the element
            element = wait.until(EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add More'])[3]")
            ))

            # Scroll element into view (center of screen)
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

            # Small pause to allow scroll animation
            time.sleep(1)

            # Click using JavaScript to avoid interception issues
            driver.execute_script("arguments[0].click();", element)

            time.sleep(3)
            wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//mat-select[@formcontrolname='sRProductId']//div[contains(@class,'mat-select-trigger')]")
            )
            ).click()
            wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//mat-option//span[normalize-space()='{product_name_in_sub_Reason_first}']")
            )
            ).click()

            time.sleep(3)
            wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//mat-select[@formcontrolname='sRReasonId']//div[contains(@class,'mat-select-trigger')]")
            )
            ).click()
            time.sleep(2)

            wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//mat-option//span[normalize-space()='{reason_name_in_sub_Reason_second}']")
            )
            ).click()
            time.sleep(2)
            
            
            wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@formcontrolname='subReason']")
            )
            ).send_keys(sub_reason)
            wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Add']")
            )
            ).click()
            time.sleep(4)

              

        except Exception as e:
            self.take_screenshot("Floor making failure")
            self.fail(f"Floor making failed: {e}")
        


                # -----------------------Positive Test Case End------------------------------


                 # -----------------------Negative Test Case Start-----------------------------

# ---------------------------------2-Product Module End-------------------------------------------------------------------       

# ---------------------------------Service Request Module start------------------------------------------------------------------- 

 # ----------------------Service Request Making Journey-------------------------------------------
        # ----------------------Service RequestPositive Test Case Start-----------------------------
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@routerlink='/supervisor/workflow' and span[text()='Work Flow']]"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@routerlink='service-request' and normalize-space()='Service Request']"))).click()
            wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Add New']")
            )
            ).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='srName' and @formcontrolname='srName']"))).send_keys(SR_NAME)
            wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "(//div[contains(@class,'mat-select-trigger')]//span[normalize-space()='Select an Option'])[1]"
            ))).click()

            time.sleep(2)
            wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//span[contains(@class,'mat-option-text') and normalize-space()='" + product_option + "']"
            ))).click()
            time.sleep(2)
            wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "(//div[contains(@class,'mat-select-trigger')]//span[normalize-space()='Select an Option'])[2]"
            ))).click()
            time.sleep(1)
            

            wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//span[contains(@class,'mat-option-text') and normalize-space()='" + reason_option + "']"
            ))).click()
            time.sleep(2)
            wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "(//div[contains(@class,'mat-select-trigger')]//span[normalize-space()='Select an Option'])[2]"
            ))).click()
            time.sleep(1)
            

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//span[contains(@class,'mat-option-text') and normalize-space()='" + collection_option + "']"
            ))).click()
            time.sleep(3)

            


            # wait.until(EC.element_to_be_clickable((
            # By.XPATH,
            # "(//div[contains(@class,'mat-select-trigger')]//span[normalize-space()='Select an Option'])[2]"
            # ))).click()
            # time.sleep(1)
            

            # wait.until(EC.element_to_be_clickable((
            #     By.XPATH,
            #     "//span[contains(@class,'mat-option-text') and normalize-space()='" + sub_reason + "']"
            # ))).click()
            # time.sleep(3)

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//mat-select[@formcontrolname='srsubReasonId']"
            ))).click()
            time.sleep(1)

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//span[contains(@class,'mat-option-text') and normalize-space()='" + sub_reason + "']"
            ))).click()
            time.sleep(3)


            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='internalTat' and @formcontrolname='internalTat']"))).send_keys(internal_tat)
            time.sleep(1)
           

            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='reOpenTat' and @formcontrolname='reOpenTat']"))).send_keys(reopen_tat)
            

            # wait.until(EC.element_to_be_clickable((
            # By.XPATH,
            # "//div[contains(@class,'mat-select-trigger')]//span[normalize-space()='" + routing_method + "']"
            # ))).click()
            # time.sleep(1)
            # wait.until(EC.element_to_be_clickable((
            # By.XPATH,
            # "(//div[contains(@class,'mat-select-trigger')])[8]"
            # ))).click()
            # time.sleep(1)
            

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//span[contains(@class,'mat-option-text') and normalize-space()='" + priority_option + "']"
            ))).click()
            time.sleep(2)
            

            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='briefSummary' and @formcontrolname='briefSummary']"))).send_keys(brief_summary)
            time.sleep(1)   
            wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='isBranchRelated' and normalize-space()='Branch Related']"))).click()
            time.sleep(2) 
            wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='isBranchRelated' and normalize-space()='Branch Related']"))).click()
            time.sleep(2)
            slider = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-slider[@formcontrolname='level']")))
            actions = ActionChains(driver)

            # Assuming slider min=1, max=10, current=3, move accordingly
            # If the slider is already at 3, no movement needed. Otherwise, calculate offset from current position.
            actions.click(slider).perform()

            time.sleep(2)

            # -----------------------------------Advance Features-------------------------------
            wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='autoAssign' and normalize-space()='Auto Assign']"))).click()
            time.sleep(2)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='autoAssign' and normalize-space()='Auto Assign']"))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='smsNotification' and normalize-space()='SMS Notification']"))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='emailNotification' and normalize-space()='Email Notification']"))).click()
            time.sleep(2)


            # ---------------------------------RO Management--------------------------------------------
            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//div[contains(@class,'mat-select-trigger')]//span[normalize-space()='Select Resolution Owner']"
            ))).click()
            time.sleep(1)
            

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//span[contains(@class,'mat-option-text') and normalize-space()='" + resolution_owner + "']"
            ))).click()
            
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='tat1' and @name='tat1']"))).send_keys(tat1_value)
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='tat2' and @name='tat2']"))).send_keys(tat2_value)
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='tat3' and @name='tat3']"))).send_keys(tat3_value)
            

            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='srStage']"))).send_keys(sr_stage)
            time.sleep(1)
            reopen_bucket = wait.until(EC.presence_of_element_located((By.XPATH, "//label[@for='ReOpenBucket0' and normalize-space()='Re-open Bucket']")))
            driver.execute_script("arguments[0].scrollIntoView(true);", reopen_bucket)
            wait.until(EC.element_to_be_clickable(reopen_bucket)).click()
            time.sleep(5)


            # ----------------------------Service Request Fields-------------------------------

            # ----------------------------First Fields (Text)-------------------------------
            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//a[contains(@class,'btn-save') and normalize-space()='Add Field']"
            ))).click()
            time.sleep(2)
            

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//input[@formcontrolname='label' and @type='text']"
            ))).send_keys(label_value_text)
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//div[contains(@class,'mat-select-trigger')]//span[normalize-space()='Select a SR Format']"
            ))).click()
            time.sleep(1)
            

            wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//span[contains(@class,'mat-option-text') and normalize-space()='" + field_type_text + "']"
            ))).click()
            time.sleep(2)
            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "(//div[contains(@class,'mat-select-trigger')]//span[normalize-space()='Select an Option'])[last()]"
            ))).click()
            time.sleep(1)
            

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//span[contains(@class,'mat-option-text') and normalize-space()='" + data_format_text + "']"
            ))).click()
            time.sleep(1)

            

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//input[@formcontrolname='screenPosition' and @type='number']"
            ))).send_keys(screen_position_1)
            time.sleep(1)

            # wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='isRequired' and normalize-space()='Required']"))).click()
            # time.sleep(1)
            # ----------------------------Autofill check---------------------------------------
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//label[@for='isAutoFill']")
                )
            ).click()
            time.sleep(2)
            wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//mat-select[@formcontrolname='srautoFillId']")
                    )
                ).click()
            time.sleep(1)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//mat-option//span[normalize-space()='Account Number']")
                )
            ).click()
            time.sleep(2)

            # ----------------------------Masked check---------------------------------------
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//label[@for='isMasked']")
                )
            ).click()

            time.sleep(2)


            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//button[@type='submit' and contains(@class,'btn-save') and normalize-space()='Add']"
            ))).click()
            time.sleep(3)

            







            # ----------------------------Second Fields (CheckBox)-------------------------------
            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//a[contains(@class,'btn-save') and normalize-space()='Add Field']"
            ))).click()
            time.sleep(2)
            

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//input[@formcontrolname='label' and @type='text']"
            ))).send_keys(label_value_checkBox)
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//div[contains(@class,'mat-select-trigger')]//span[normalize-space()='Select a SR Format']"
            ))).click()
            time.sleep(1)
            

            wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//span[contains(@class,'mat-option-text') and normalize-space()='" + field_type_checkbox + "']"
            ))).click()
            time.sleep(2)

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "(//div[contains(@class,'mat-select-trigger')]//span[normalize-space()='Select an Option'])[last()]"
            ))).click()
            time.sleep(1)
            

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//span[contains(@class,'mat-option-text') and normalize-space()='" + data_format_checkbox + "']"
            ))).click()
            time.sleep(1)

            

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//input[@formcontrolname='screenPosition' and @type='number']"
            ))).send_keys(screen_position_2)
            time.sleep(1)

            # wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='isRequired' and normalize-space()='Required']"))).click()
            # time.sleep(1)


            # ----------------------------Autofill check---------------------------------------
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//label[@for='isAutoFill']")
                )
            ).click()
            time.sleep(2)
            wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//mat-select[@formcontrolname='srautoFillId']")
                    )
                ).click()
            time.sleep(1)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//mat-option//span[normalize-space()='Account Number']")
                )
            ).click()
            time.sleep(2)

            # ----------------------------Masked check---------------------------------------
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//label[@for='isMasked']")
                )
            ).click()

            time.sleep(2)


            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//button[@type='submit' and contains(@class,'btn-save') and normalize-space()='Add']"
            ))).click()
            time.sleep(3)
            


        # ----------------------------Third Fields (Dropdown)-------------------------------
            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//a[contains(@class,'btn-save') and normalize-space()='Add Field']"
            ))).click()
            time.sleep(2)
            

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//input[@formcontrolname='label' and @type='text']"
            ))).send_keys(label_value_dropdown)
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//div[contains(@class,'mat-select-trigger')]//span[normalize-space()='Select a SR Format']"
            ))).click()
            time.sleep(1)


            

            wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//span[contains(@class,'mat-option-text') and normalize-space()='" + field_type_dropdown + "']"
            ))).click()
           
            time.sleep(1)

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//textarea[@formcontrolname='query']"
            ))).send_keys(Enter_dropdown_options)
            

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "(//div[contains(@class,'mat-select-trigger')]//span[normalize-space()='Select an Option'])[last()]"
            ))).click()
            time.sleep(1)
            

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//span[contains(@class,'mat-option-text') and normalize-space()='" + data_format_dropdown + "']"
            ))).click()
            time.sleep(1)

            

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//input[@formcontrolname='screenPosition' and @type='number']"
            ))).send_keys(screen_position_3)
            time.sleep(1)

            # wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='isRequired' and normalize-space()='Required']"))).click()
            # time.sleep(1)

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//button[@type='submit' and contains(@class,'btn-save') and normalize-space()='Add']"
            ))).click()
            time.sleep(3)


        # ----------------------------Forth Fields (RadioButton)-------------------------------
            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//a[contains(@class,'btn-save') and normalize-space()='Add Field']"
            ))).click()
            time.sleep(2)
            

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//input[@formcontrolname='label' and @type='text']"
            ))).send_keys(label_value_radiobutton)
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//div[contains(@class,'mat-select-trigger')]//span[normalize-space()='Select a SR Format']"
            ))).click()
            time.sleep(1)


            

            wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//span[contains(@class,'mat-option-text') and normalize-space()='" + field_type_radiobutton + "']"
            ))).click()
           
            time.sleep(1)

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//textarea[@formcontrolname='query']"
            ))).send_keys(Enter_radiobutton_options)
            

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "(//div[contains(@class,'mat-select-trigger')]//span[normalize-space()='Select an Option'])[last()]"
            ))).click()
            time.sleep(1)
            

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//span[contains(@class,'mat-option-text') and normalize-space()='" + data_format_radiobutton + "']"
            ))).click()
            time.sleep(1)

            

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//input[@formcontrolname='screenPosition' and @type='number']"
            ))).send_keys(screen_position_4)
            time.sleep(1)

            # wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='isRequired' and normalize-space()='Required']"))).click()
            # time.sleep(1)

            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//button[@type='submit' and contains(@class,'btn-save') and normalize-space()='Add']"
            ))).click()
            time.sleep(4)
            add_sr_button = wait.until(EC.presence_of_element_located((
                By.XPATH,
                "//button[normalize-space()='Add SR']"
            )))
            driver.execute_script("arguments[0].scrollIntoView(true);", add_sr_button)
            time.sleep(5)
            wait.until(EC.element_to_be_clickable(add_sr_button)).click()
            time.sleep(5)                

        except Exception as e:
            self.take_screenshot("Floor making failure")
            self.fail(f"Floor making failed: {e}")

        
# ------------------------------- Workflow tab Ends here ---------------------------------------------
# ------------------------------- Workflow tab Ends here ---------------------------------------------



# -------------------------------Make agent ,assign skill and add in campaign------------------------
 # ---------------------- Agent Making Journey Positive (Start) ------------------------------------
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[@routerlink='/supervisor/agents']//span[text()='Agents']"))
            ).click()

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[@routerlink='all-agents' and normalize-space(text())='Listing']"))
            ).click()

            time.sleep(2)

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[@routerlink='manage-agents' and text()='Manage Agents']"))
            ).click()

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Add Resources')]"))
            ).click()

            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//input[@formcontrolname='agentName']"))
            ).send_keys("Test Agent")

            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//input[@formcontrolname='emailAddress']"))
            ).send_keys("test@example.com")

            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//input[@formcontrolname='contactNumber']"))
            ).send_keys("03001234567")

            # ---------------- Role Dropdown ----------------
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class,'mat-select-value')]"))
            ).click()

            time.sleep(2)

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//span[@class='mat-option-text' and text()='Agent']"))
            ).click()

            # ---------------- Add Skill ----------------
            time.sleep(2)
            skills_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Add new Skills')]"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", skills_button)
            driver.execute_script("arguments[0].click();", skills_button)

            # ---------------- Skill Dropdown ----------------
            time.sleep(3)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class,'mat-select-value') and .//span[contains(@class,'mat-select-placeholder')]]"))
            ).click()

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//span[@class='mat-option-text' and normalize-space(text())='CallBack']"))
            ).click()

            # ---------------- Level Dropdown ----------------
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class,'mat-select-value')]//span[contains(text(),'Choose a level')]"))
            ).click()

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//span[@class='mat-option-text' and normalize-space(text())='1']"))
            ).click()

            # ---------------- Create User (FIXED CLICK) ----------------
            create_btn = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//button[.//span[text()='Create User']]"))
            )
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", create_btn)
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, -150);")
            time.sleep(1)
            driver.execute_script("arguments[0].click();", create_btn)
            time.sleep(8)

            # ---------------------- Add Agent to Campaign and give Rights ----------------------------------
            self.fast_wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@routerlink='/supervisor/campaigns' and .//span[normalize-space()='Campaigns']]"))
            ).click()

            self.fast_wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@routerlink='manage-campaign' and normalize-space()='Manage Campaigns']"))
            ).click()

            elem = self.fast_wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[normalize-space()='Raqami Call back']"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center', behavior:'smooth'});", elem)
            time.sleep(0.5)
            elem.click()

            edit_button = self.fast_wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@title='Edit']"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center', behavior:'smooth'});", edit_button)
            time.sleep(0.5)
            edit_button.click()

            assign_button = self.fast_wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(@class,'assign-button') and contains(text(),'Assign / Remove Agent')]"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center', behavior:'smooth'});", assign_button)
            time.sleep(0.5)
            assign_button.click()

            search_input = self.fast_wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//input[@type='text' and @placeholder='Search']"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center', behavior:'smooth'});", search_input)
            search_input.clear()
            search_input.send_keys("rashid.minha")

            self.fast_wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//li[contains(@class,'list-group-item') and normalize-space()='rashid.minha']"))
            ).click()
            time.sleep(3)

            self.fast_wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(@class,'btn-save') and .//span[normalize-space()='Update']]"))
            ).click()
            time.sleep(3)

        except Exception as e:
            self.take_screenshot("Agent_making_failure")
            self.fail(f"Agent making failed: {e}")






        

    


















         # ------------------------------- Logout start -----------------------------------
        try:
            logout_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Log Out']"))
            )
            driver.execute_script("arguments[0].click();", logout_btn)
            time.sleep(2)
            confirm_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Yes']"))
            )
            driver.execute_script("arguments[0].click();", confirm_btn)
            time.sleep(2)

            print("Logout successful!")

        except Exception as e:
            self.take_screenshot("logout_failure")
            self.fail(f"Logout failed: {e}")
        # ----------------- Logout End -----------------

         
# ----------------- Report generation --------------------------
if __name__ == "__main__":
    output_dir = os.path.join(os.getcwd(), "Reports")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=output_dir,
            report_title="SBOSS Registration Test Report",
            combine_reports=True,
            add_timestamp=True
        ),
        verbosity=2
    )