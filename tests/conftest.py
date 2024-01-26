import subprocess
import time
import pytest
from appium import webdriver
import logging
import re

from utils.android_utils import android_get_desired_capabilities


def get_connected_devices():
    try:
        result = subprocess.run(['adb', 'devices'], capture_output = True, text = True, shell = True)
        device_lines = result.stdout.split('\n')[1:]
        devices = [re.match(r'^(\S+)', line).group(1) for line in device_lines if line.strip()]
        logging.info("Getting list of devices")
        return devices
    except subprocess.CalledProcessError:
        logging.critical("Called process error")
        return None


def get_first_connected_device():
    devices = get_connected_devices()

    if devices:
        logging.info(f'Device name: {devices[0]}')
        return devices[0]
    else:
        logging.error('Any connected devices')
        return None


@pytest.fixture(scope='session')
def run_appium_server():
    appium_process = subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)
    yield

    try:
        subprocess.run(['taskkill', '/F', '/PID', str(appium_process.pid)], check=True)
    except subprocess.CalledProcessError:
        pass

    return_code = appium_process.wait()
    print(f"Appium process terminated with return code: {return_code}")



@pytest.fixture(scope='session')
def driver(run_appium_server):
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(filename='file.log', filemode='w', encoding='utf-8', level=logging.INFO)
    desired_capabilities = android_get_desired_capabilities()
    udid = get_first_connected_device()
    desired_capabilities['udid'] = udid
    logging.info('Device name added to capabilities')

    try: 
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
        logging.info('Connection installed')
        yield driver
        driver.quit()
    except Exception as e:
        logging.critical('No connection could be made')
        pytest.fail(f"Failed connection Appium. Error: {str(e)}")
