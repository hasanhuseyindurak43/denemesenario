import os

def toggle_mobile_data(action):
    if action == 'open':
        os.system('termux-telephony-radio on')
    elif action == 'close':
        os.system('termux-telephony-radio off')
    else:
        print("Invalid action. Use 'open' to turn on and 'close' to turn off mobile data.")

# Mobil veriyi açmak için:
toggle_mobile_data('open')

# Mobil veriyi kapatmak için:
toggle_mobile_data('close')
