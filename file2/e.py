import re

p = re.compile(r"Windows NT|Mac OS|Linux|GoogleMaps")
def search(file):
	ctn = []
	with open(file,'r') as f:
		for fr in f.readlines():
			a = p.findall(fr)
			ctn.extend(a)
			pass
	# print(ctn)
	return ctn


if __name__ == "__main__":
	file = r'F:\py学习\file1.txt'
	ctn = search(file)
	WindowsNT = ctn.count("Windows NT")
	MacOS = ctn.count("Mac OS")
	Linux = ctn.count("Linux")
	GoogleMaps = ctn.count("GoogleMaps")
	print("WindowsNT出现的次数：%d,MacOS出现的次数：%d,Linux出现的次数：%d,GoogleMaps出现的次数：%d"%(WindowsNT,MacOS,Linux,GoogleMaps))