from contextlib import nullcontext as does_not_raise
from selenium.common.exceptions import TimeoutException
import logging
import pytest

@pytest.mark.parametrize("login, password, expectation", [
    ('qa.ajax.app.automation@gmail.com6', 'qa_automation_password', pytest.raises(TimeoutException)),
    ('qa.ajax.app.automation@gmail.com', 'qa_automation_password3', pytest.raises(TimeoutException)),
    ('qa.ajax.app.automation@gmail.com', 'qa_automation_password', does_not_raise())
    ])
def test_user_login(user_login_fixture, login, password, expectation):

    logging.info(f"Test for login={login}, password={password}")
    logging.info("Finding input elements and button")
    email_input = user_login_fixture.find_element('//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginEmail"]')
    password_input = user_login_fixture.find_element('//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginPassword"]')
    login_button = user_login_fixture.find_element('(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[4]/android.view.View/android.view.View/android.widget.Button')   
    
    logging.info("Clear input fields")
    user_login_fixture.clear_input(email_input)
    user_login_fixture.clear_input(password_input)

    logging.info("Input text to fields and click a login button")
    user_login_fixture.input_text(email_input, login)
    user_login_fixture.input_text(password_input, password)
    user_login_fixture.click_element(login_button)

    with expectation:
        assert user_login_fixture.wait_for_element('//android.widget.LinearLayout[@resource-id="com.ajaxsystems:id/noHubs"]/android.view.ViewGroup/android.widget.LinearLayout')==None or True
