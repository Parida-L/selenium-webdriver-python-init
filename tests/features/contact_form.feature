Feature: Contact form validation
    As a visitor
    I want to ensure that the contact form on the contact page works correctly

    Scenario: Fill out and submit the form
        Given I am on the contact page
        When I fill out the form and verify the data sent
        Then the form should be successfully submitted


            # Scenario: Verify the presence of the input fields
    #     Given I am on the contact page
    #     Then I should see the "name" input field "text"
    #     And I should see the "email" input field "email"
    #     And I should see the gender radio buttons
    #     And I should see the mobile number input field "tel"
    #     And the date of birth input field "date"