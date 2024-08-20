import os
from playwright.sync_api import sync_playwright

def toggle_mobile_data(action):
    if action == 'open':
        os.system('termux-telephony-radio on')
    elif action == 'close':
        os.system('termux-telephony-radio off')
    else:
        print("Invalid action. Use 'open' to turn on and 'close' to turn off mobile data.")

# Mobil veriyi açmak için:
toggle_mobile_data('open')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://example.com')
    print(page.title())
    browser.close()

# Mobil veriyi kapatmak için:
toggle_mobile_data('close')
