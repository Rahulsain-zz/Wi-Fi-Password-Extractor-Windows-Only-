import subprocess
import re
import os

def get_saved_profiles():
    profiles_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], text=True)
    return re.findall(r"All User Profile\s*:\s(.*)", profiles_data)

def get_profile_password(profile):
    try:
        result = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profile', profile.strip(), 'key=clear'], text=True, stderr=subprocess.DEVNULL
        )
        password_match = re.search(r"Key Content\s*:\s(.*)", result)
        auth_match = re.search(r"Authentication\s*:\s(.*)", result)
        password = password_match.group(1).strip() if password_match else "N/A"
        auth = auth_match.group(1).strip() if auth_match else "N/A"
        return {"SSID": profile.strip(), "Password": password, "Security": auth}
    except subprocess.CalledProcessError:
        return {"SSID": profile.strip(), "Password": "Error", "Security": "N/A"}

def main():
    profiles = get_saved_profiles()
    wifi_list = []

    if not profiles:
        print("[!] No Wi-Fi profiles found.")
        return

    for profile in profiles:
        wifi_info = get_profile_password(profile)
        wifi_list.append(wifi_info)

    print("\n📡 Saved Wi-Fi Networks:\n" + "-" * 40)
    for wifi in wifi_list:
        print(f"SSID     : {wifi['SSID']}")
        print(f"Password : {wifi['Password']}")
        print(f"Security : {wifi['Security']}")
        print("-" * 40)

    # Save to file
    save = input("💾 Save results to wifi_passwords.txt? (y/n): ").lower()
    if save == 'y':
        with open("wifi_passwords.txt", "w") as f:
            for wifi in wifi_list:
                f.write(f"SSID: {wifi['SSID']}\nPassword: {wifi['Password']}\nSecurity: {wifi['Security']}\n{'-'*40}\n")
        print("[+] Results saved to wifi_passwords.txt")

if __name__ == "__main__":
    if os.name == 'nt':
        main()
    else:
        print("❌ This tool only works on Windows.")
