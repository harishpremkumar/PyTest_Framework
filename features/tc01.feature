Feature: Login Page

    Scenario: Successful Application Login With User 1
        Given User is on login page
        When User enter username "standard_user" and password "secret_sauce"
        Then User should be able to login successfully and new page open "Swag Labs"

    Scenario: Successful Application Login With User 2
        Given User is on login page
        When User enter username "error_user" and password "secret_sauce"
        Then User should be able to login successfully and new page open "Swag Labs"   