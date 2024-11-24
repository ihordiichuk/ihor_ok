import qrcode

qr = qrcode.QRCode(
    version=1,  # size of the qr code from 1 to 21x21 matrix
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

ssid = "Trust WiFi"
password = "9M4Dxwetg7"
encryption = "WPA"  # "WPA" or "WEP" or "None"

wifi_qr = f"WIFI:T:{encryption};S:{ssid};P:{password};;"
qr = qrcode.make(wifi_qr)
qr.save("wifi_qr_code.png")
