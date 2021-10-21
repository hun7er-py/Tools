import winreg
import ctypes
keys = [r"SOFTWARE\WOW6432Node\Portima\ASWeb\Plugins\Update",r"SOFTWARE\WOW6432Node\Portima\PortimaUpd"]
key_val = ["RebootNeeded", "Reboot.Needed"]
for i in range(2):
	reg_key = keys[i]
	print (reg_key)
	with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as hkey:
		with winreg.OpenKey(hkey, reg_key, 0, winreg.KEY_ALL_ACCESS) as sub_key:

			try:
				#key = reg.OpenKey(hkey, reg_key, 0, reg.KEY_ALL_ACCESS)
				print("Key opened")
				print("trying to write to key")
				winreg.SetValueEx(sub_key, key_val[i], 0, winreg.REG_DWORD, 0)
				print("Writing done...")
				print("trying to close key")
				winreg.CloseKey(sub_key)
				print("Key closed")
			except Exception as e:
				print(e)

	"""reg_key = r"SOFTWARE\WOW6432Node\Portima\PortimaUpd"
	print (reg_key)
	with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as hkey:
		with winreg.OpenKey(hkey, reg_key, 0, winreg.KEY_ALL_ACCESS) as sub_key:

			try:
				#key = reg.OpenKey(hkey, reg_key, 0, reg.KEY_ALL_ACCESS)
				print("Key opened")
				print("trying to write to key")
				winreg.SetValueEx(sub_key, "RebootNeeded", 0, winreg.REG_DWORD, 0)
				print("Writing done...")
				print("trying to close key")
				winreg.CloseKey(sub_key)
				print("Key closed")
				
			except Exception as e:
				print(e)
"""
else:
	print("Done!")

"""HWND_BROADCAST = 0xFFFF
WM_SETTINGCHANGE = 0x1A
SMTO_ABORTIFHUNG = 0x0002
result = ctypes.c_long()
SendMessageTimeoutW = ctypes.windll.user32.SendMessageTimeoutW
SendMessageTimeoutW(HWND_BROADCAST, WM_SETTINGCHANGE, 0, sub_key, SMTO_ABORTIFHUNG, 5000, ctypes.byref(result),) 
"""
