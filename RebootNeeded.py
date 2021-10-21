#Instead of changing regkeys manually, we're going to have a small script take care of it!
#Copyright Hun7er
#Github.com/hun7er-py


#importing necessary libs
import winreg
import ctypes

#defining the path where our keys are
keys = [r"SOFTWARE\WOW6432Node\Portima\ASWeb\Plugins\Update",r"SOFTWARE\WOW6432Node\Portima\PortimaUpd"]

#defining the keys in an array of strings
key_val = ["RebootNeeded", "Reboot.Needed"]

#replace 2 key values, so for loop with 2 iterations
for i in range(2):

	#take first value
	reg_key = keys[i]

	print (reg_key) #debugging

	#calling connection to the reg key p1
	with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as hkey:

		# now we're opening the key with our hkey, reg_key (from array) and this value we're putting in sub_key
		with winreg.OpenKey(hkey, reg_key, 0, winreg.KEY_ALL_ACCESS) as sub_key:

			#trying to write the value [i] into key [i]	
			try:
				#key = reg.OpenKey(hkey, reg_key, 0, reg.KEY_ALL_ACCESS)
				print("Key opened") 											#debugging
				print("trying to write to key")									#debugging
				winreg.SetValueEx(sub_key, key_val[i], 0, winreg.REG_DWORD, 0)	#actually writing value
				print("Writing done...")										#debugging
				print("trying to close key")									#debugging
				winreg.CloseKey(sub_key)										#closing and saving key
				print("Key closed")												#debugging
			except Exception as e:
				print(e)														#if exception, print it


#=================================================================
#=====  FOLLOWING BLOCK OPTIONAL IN CASE OF NO ITERATION USAGE ===
#=================================================================
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
#============================== END BLOCK =========================

else:
	print("Done!")#debugging

"""HWND_BROADCAST = 0xFFFF
WM_SETTINGCHANGE = 0x1A
SMTO_ABORTIFHUNG = 0x0002
result = ctypes.c_long()
SendMessageTimeoutW = ctypes.windll.user32.SendMessageTimeoutW
SendMessageTimeoutW(HWND_BROADCAST, WM_SETTINGCHANGE, 0, sub_key, SMTO_ABORTIFHUNG, 5000, ctypes.byref(result),) 
"""
