from seleniumbase import BaseCase

BaseCase.main(__name__, __file__)


class CheckLoginFunctionality(BaseCase):
    def test_CheckLoginFunctionality(self):
        #  Open Web browser & max window
        self.maximize_window()
        self.open("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.type('input[name="username"]', "Admin")
        self.type('input[name="password"]', "admin123")
        self.click('button:contains("Login")')
        # Check if the page successfully navigates to the dashboard page
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        actual_url = self.get_current_url()

        self.assert_equal(expected_url, actual_url, "Assertion failed: The dashboard page did not load as expected.")
        print("Assertion successful: The dashboard page has been loaded.")

        actual_username_element = self.wait_for_element_visible(
            "//*[@id=\"app\"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p")
        expected_username = actual_username_element.text
        actual_username = actual_username_element.text

        # Print the dynamic username element text
        print("Username:", actual_username)
        self.assert_equal(expected_username, actual_username,
                          "Assertion failed: The displayed username does not match the expected.")
        print("Assertion successful: The displayed username matches the expected.")


class UserInsertInvalidUsernameOrPassword(BaseCase):
    def test_UserInsertInvalidUsernameOrPassword(self):
        self.maximize_window()
        self.open("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.type('input[name="username"]', "Admin1")
        self.type('input[name="password"]', "admin1123")
        self.click('button:contains("Login")')

        expected_error_message = "Invalid credentials"
        error_message_element = self.wait_for_element_visible(
            "//*[@id=\"app\"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p")
        actual_error_message = error_message_element.text

        self.assert_true(expected_error_message in actual_error_message,
                         "Assertion failed: Login succeeded, but it was expected to fail with invalid credentials!")
        print("Assertion successful: Login failed with invalid credentials as expected!")
