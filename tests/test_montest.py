import  pytest
import pytest_bdd
from pytest_bdd import parsers
from selenium import webdriver  # Import the Selenium Webdriver
from selenium.webdriver.common.by import By # Import the By class
from pytest_bdd import given, when, then, scenario

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    