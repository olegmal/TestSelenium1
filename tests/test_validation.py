from pages.auth_page import FormAuthentication



def test_form_authentication(driver):
    form = FormAuthentication(driver)

    # form.navigate_to_form_page()
    form.enter_login_username("performance_glitch_user")
    form.enter_login_password("secret_sauce")
    form.click_login_button()

