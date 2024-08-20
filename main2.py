import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def toggle_mobile_data(action):
    if action == 'open':
        os.system('termux-telephony-radio on')
    elif action == 'close':
        os.system('termux-telephony-radio off')
    else:
        print("Invalid action. Use 'open' to turn on and 'close' to turn off mobile data.")

# Mobil veriyi açmak için:
toggle_mobile_data('open')

# Selenium için Chrome ayarları
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# ChromeDriver ile tarayıcı başlatma
driver = webdriver.Chrome(options=chrome_options)

# Web sayfasına gitme
driver.get('https://www.ipaddress.my/?lang=tr')
print(driver.title())

# Tarayıcıyı kapatma
driver.quit()

# Mobil veriyi kapatmak için:
toggle_mobile_data('close')

