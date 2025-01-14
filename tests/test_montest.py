import  pytest
import pytest_bdd
import time
from selenium.webdriver.common.keys import Keys
from pytest_bdd import parsers
from selenium import webdriver  # Import the Selenium Webdriver
from selenium.webdriver.common.by import By # Import the By class
from pytest_bdd import given, when, then, scenario

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

#1er scenario, je teste la présence des éléments sur la page
@scenario('features/contact_form.feature', 'Fill out and submit the form')

def test_input_field_presence():
    pass #

@given('I am on the contact page')
def open_contact_page(browser):
    browser.get('https://demoqa.com/automation-practice-form')

@when('I fill out the form and verify the data sent')
def fill_out_form(browser):
    # First name 
    first_name_input = browser.find_element(By.ID, 'firstName')
    assert first_name_input.is_displayed(), "First Name input field is not visible"
    first_name_input.send_keys("John")
    assert browser.find_element(By.ID, 'firstName').get_attribute("value") == "John", "First Name value is incorrect"

    # Last name
    last_name_input = browser.find_element(By.ID, 'lastName')
    assert last_name_input.is_displayed(), "Last Name input field is not visible"
    last_name_input.send_keys("Doe")
    assert browser.find_element(By.ID, 'lastName').get_attribute("value") == "Doe", "Last Name value is incorrect"

    # Email
    email_input = browser.find_element(By.ID, 'userEmail')
    assert email_input.is_displayed(), "Email input field is not visible"
    email_input.send_keys("john@doe.com")
    assert browser.find_element(By.ID, 'userEmail').get_attribute("value") == "john@doe.com", "Email value is incorrect"

    # Gender 
    gender_radio = browser.find_element(By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[1]/label')
    assert gender_radio.is_displayed(), "Gender radio button is not visible"
    gender_radio.click()
    gender_radio_selected = browser.find_element(By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[1]/input')
    assert gender_radio_selected.is_selected(), "Gender radio button is not selected"

    # Mobile number
    mobile_input = browser.find_element(By.ID, 'userNumber')
    assert mobile_input.is_displayed(), "Mobile input field is not visible"
    mobile_input.send_keys("123456789")
    assert browser.find_element(By.ID, 'userNumber').get_attribute("value") == "123456789", "Mobile value is incorrect"

    # Date of Birth
    date_of_birth_input = browser.find_element(By.ID, 'dateOfBirthInput')
    assert date_of_birth_input.is_displayed(), "Date of Birth input field is not visible"
    time.sleep(3)
    browser.execute_script("arguments[0].value = '16 May 2025';", date_of_birth_input)
    assert browser.find_element(By.ID, 'dateOfBirthInput').get_attribute("value") == "16 May 2025", "Date of Birth value is incorrect"

    # Subjects
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
    # Hobbies
    hobbies_chosen = browser.find_element(By.XPATH, '//label[text()="Sports"]') # Locate the label for the checkbox
    # assert hobbies_chosen.is_displayed(), "Hobbies label is not visible"
    hobbies_chosen.click()  # Click on the label to select the checkbox

    # Scroll to the element to ensure it is visible
    browser.execute_script("arguments[0].scrollIntoView(true);", hobbies_chosen)

    # Click using JavaScript to avoid click interception
    browser.execute_script("arguments[0].click();", hobbies_chosen)

    # Verify that the checkbox is selected
    #assert hobbies_chosen.is_selected(), "Hobbies checkbox is not selected"

    # Submit form 
    submit_button = browser.find_element(By.ID, 'submit')
    assert submit_button.is_displayed(), "Submit button is not visible"
    time.sleep(3)
    submit_button.click()
    browser.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    browser.execute_script("arguments[0].click();", submit_button)

@then('the form should be successfully submitted')
def verify_form_submission(browser):
    # Verify the modal dialog appears
    modal = browser.find_element(By.XPATH, '/html/body/div[4]/div/div')
    assert modal.is_displayed(), "Form submission modal is not displayed"
    #assert modal.text == "Thanks for submitting the form", "Form submission message is incorrect"
