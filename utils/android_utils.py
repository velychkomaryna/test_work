def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '11',
        'resetKeyboard': True,
        'systemPort': 8306,
        'takesScreenshot': True,
        'udid': '',
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity',
        'newCommandTimeout': 500,
}
