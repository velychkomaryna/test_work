import pytest
import logging

from framework.login_page import LoginPage

@pytest.fixture(scope='session')
def user_login_fixture(driver):
    page = LoginPage(driver)
    logging.info("An instance of the LoginPage class has been created")
    element = page.find_element('(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[1]/android.view.View/android.view.View/android.widget.Button')
    page.click_element(element)
    page.wait_for_element('//androidx.recyclerview.widget.RecyclerView[@resource-id="com.ajaxsystems:id/content"]')
    logging.info("Go to login page")
    yield page
