# Wi-Fi-Password-Extractor-Windows-Only-
This tool extracts saved Wi-Fi SSIDs and their passwords using Windows’ built-in netsh command, then parses and presents the results cleanly.
🧠 How It Works
Component	Description
netsh wlan show profiles	Lists saved Wi-Fi SSIDs
netsh wlan show profile <SSID> key=clear	Reveals security key
re.findall() & re.search()	Used to extract key parts
Optional file output	Saves results for later
# 📡 Windows Wi-Fi Password Extractor (Python)

> ⚠️ Windows-only tool to extract saved Wi-Fi passwords (educational use)

This tool lists saved Wi-Fi profiles and reveals their passwords using the `netsh` command.

---

## 🚀 Features

- 🔍 Extract saved SSID profiles
- 🔐 View actual passwords (Key Content)
- 🧾 Optionally save results to file
- 💻 Requires no 3rd party modules
- ✔️ Clean output format

---

## 🖥️ Usage


python wifi_password_extractor.py

📦 Requirements

No extra installation needed — uses Python’s built-in libraries.

Works only on:

    ✅ Windows 7+

    ✅ Python 3.6+

  📸 Sample Output
  📡 Saved Wi-Fi Networks:
----------------------------------------
SSID     : HomeWiFi
Password : mysecretpass
Security : WPA2-Personal
----------------------------------------
💾 Save Results

Choose to save the output to wifi_passwords.txt by entering y when prompted.

⚠️ Disclaimer

This tool is for educational & personal use only. Do not use this on systems you don't own or without permission.
