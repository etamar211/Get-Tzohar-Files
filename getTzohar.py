import urllib

y = 2
p = 1
url = "http://www.tzohar.org.il/wp-content/uploads/"

for y in range (43, 48):
	for p in range (1, 40):
		if p < 10:
			num = str(y) + '_0' + str(p) + ".pdf"
		else:
			num = str(y) + '_' + str(p) + ".pdf"
		urllib.urlretrieve (url + num, num)
