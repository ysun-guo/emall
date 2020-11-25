from selenium.webdriver.chrome.options import Options


def return_driver_option():
    mobile_emulation = {"deviceName": "iPhone 8"}
    options = Options()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_argument("--auto-open-devtools-for-tabs")
    return options

test_host='https://emall.namektest.xyz'
host='https://emallh5.namek.com.cn'