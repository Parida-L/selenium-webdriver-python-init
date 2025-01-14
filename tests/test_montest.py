import time
import  pytest
import pytest_bdd
from selenium import webdriver  # Import the Selenium Webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from pytest_bdd import parsers
from selenium.webdriver.common.by import By # Import the By class
from pytest_bdd import given, when, then, scenario
from selenium.webdriver.chrome.options import Options # Import the Options class
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Fixture for initializing and quitting the browser
@pytest.fixture
def browser():
    driver = webdriver.Chrome() # Start a new Chrome browser session
    yield driver # Provide the driver to the tests
    driver.quit() # Quit the browser session after tests

# Scenario definition: Fill out and submit the contact form
@scenario('features/contact_form.feature', 'Fill out and submit the form')

def test_input_field_presence():
    pass # Placeholder for the scenario steps

# Step 1: Navigate to the contact page
@given('I am on the contact page')
def open_contact_page(browser):
    browser.get('https://demoqa.com/automation-practice-form')

# Step 2: Fill out the form and verify the entered data
@when('I fill out the form and verify the data sent')
def fill_out_form(browser):
    # Fill the "First Name" field and verify its value
    first_name_input = browser.find_element(By.ID, 'firstName')
    assert first_name_input.is_displayed(), "First Name input field is not visible"
    first_name_input.send_keys("John")
    assert browser.find_element(By.ID, 'firstName').get_attribute("value") == "John", "First Name value is incorrect"

    # Fill the "Last Name" field and verify its value
    last_name_input = browser.find_element(By.ID, 'lastName')
    assert last_name_input.is_displayed(), "Last Name input field is not visible"
    last_name_input.send_keys("Doe")
    assert browser.find_element(By.ID, 'lastName').get_attribute("value") == "Doe", "Last Name value is incorrect"

    # Fill the "Email" field and verify its value
    email_input = browser.find_element(By.ID, 'userEmail')
    assert email_input.is_displayed(), "Email input field is not visible"
    email_input.send_keys("john@doe.com")
    assert browser.find_element(By.ID, 'userEmail').get_attribute("value") == "john@doe.com", "Email value is incorrect"

    # Select the "Male" gender radio button 
    gender_radio = browser.find_element(By.ID, "gender-radio-1")
    # Scroll to the gender radio button to make it visible in the viewport
    browser.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", gender_radio)
    # Wait for obstructing elements to disappear
    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element((By.CLASS_NAME, "col-12 mt-4 col-md-6"))
    )
    # Click on the gender radio button using JavaScript
    browser.execute_script("arguments[0].click();", gender_radio)
    # Verify that the radio button is selected
    gender_radio_selected = browser.find_element(By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[1]/input')
    assert gender_radio_selected.is_selected(), "Gender radio button is not selected"

    # Fill the "Mobile Number" field and verify its value
    mobile_input = browser.find_element(By.ID, 'userNumber')
    assert mobile_input.is_displayed(), "Mobile input field is not visible"
    mobile_input.send_keys("123456789")
    assert browser.find_element(By.ID, 'userNumber').get_attribute("value") == "123456789", "Mobile value is incorrect"

    # Set the "Date of Birth"
    date_of_birth_input = browser.find_element(By.ID, 'dateOfBirthInput')
    assert date_of_birth_input.is_displayed(), "Date of Birth input field is not visible"
    time.sleep(3)
    browser.execute_script("arguments[0].value = '16 May 2025';", date_of_birth_input)
    assert browser.find_element(By.ID, 'dateOfBirthInput').get_attribute("value") == "16 May 2025", "Date of Birth value is incorrect"

    # Fill the "Subjects" field and verify its value
    subjects_input = browser.find_element(By.ID, 'subjectsInput')
    assert subjects_input.is_displayed(), "Subjects input field is not visible"
    subjects_input.send_keys("Maths")
    time.sleep(5)
    subjects_input.send_keys(Keys.ENTER)
    assert browser.find_element(By.XPATH, '//div[@class="css-12jo7m5 subjects-auto-complete__multi-value__label"]').is_displayed(), "Subjects value is incorrect"
    assert browser.find_element(By.XPATH, '//div[@class="css-12jo7m5 subjects-auto-complete__multi-value__label"]').text == "Maths", "Subjects value is incorrect"

    element = browser.find_element(By.ID, "submit")
    browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    time.sleep(3)

    # Scroll to and select a hobby (e.g., "Sports")
    hobbies_chosen = browser.find_element(By.XPATH, '//label[text()="Sports"]') # Locate the label for the checkbox
    hobbies_chosen.click()  # Click on the label to select the checkbox
    # Scroll to the element to ensure it is visible
    browser.execute_script("arguments[0].scrollIntoView(true);", hobbies_chosen)
    # Click using JavaScript to avoid click interception
    browser.execute_script("arguments[0].click();", hobbies_chosen)

    # Submit form 
    submit_button = browser.find_element(By.ID, 'submit')
    assert submit_button.is_displayed(), "Submit button is not visible"
    time.sleep(3)
    submit_button.click()
    browser.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    browser.execute_script("arguments[0].click();", submit_button)
    time.sleep(3)

# Step 3: Verify the form submission modal
@then('the form should be successfully submitted')
def verify_form_submission(browser):
    # Wait for modal dialog to appear
    try:
        modal = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@role='dialog' and contains(@class, 'modal')]"))
        )
        print("Modal is displayed.")

        # Validate modal title
        modal_title = browser.find_element(By.XPATH, "//div[@id='example-modal-sizes-title-lg']")
        assert modal_title.text == "Thanks for submitting the form", "Modal title is incorrect"
        print("Modal title is correct.")

        # Get all table rows in the modal body
        table_rows = browser.find_elements(By.XPATH, "//table[@class='table']/tbody/tr")
        for row in table_rows:
            label = row.find_element(By.XPATH, "./td[1]").text
            value = row.find_element(By.XPATH, "./td[2]").text
            print(f"{label}: {value}")

            # Add specific checks
            if label == "Student Name":
                assert value == "John Doe", "Name value is incorrect"
            elif label == "Student Email":
                assert value == "john@doe.com", "Student Email value is incorrect"
            elif label == "Gender":
                assert value == "Male", "Gender value is incorrect"

        # Close the modal
        close_button = browser.find_element(By.ID, "closeLargeModal")
        close_button.click()
        print("Modal closed.")

    except Exception as e:
        print("Error handling modal:", e)
