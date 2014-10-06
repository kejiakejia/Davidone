import urllib


url0 = [''] * 5000

str0_0_0 = urllib.urlopen("http://blog.so8848.com/2013/06/downloads-open-courses-of-computer.html").read()

str0_1_0 = str0_0_0.find(r'<h1 id="downloads"')
str0_2_0 = str0_0_0.find(r'id="comments"')
str1_0 = str0_0_0[str0_1_0:str0_2_0]
j = 0

href0 = str1_0.find(r'href="')
title0 = str1_0.find(r'" style="color: #2685aa;',href0)

# href0 = str1[href+9:title+4]
# title0 = str1[href+43:title+4]

# print href,"\n",title,"\n"
# url0 = str1[href+6:title]
# print url

while href0 != -1 and title0 != -1 and j < 80:
	url0[j] = str1_0[href0+6:title0]
	print url0[j]

	href0 = str1_0.find(r'href="',title0)
	title0 = str1_0.find(r'" style="color: #2685aa;',href0)

	j += 1



# urls = ["https://www.udacity.com/wiki/cs101/downloads","https://www.udacity.com/wiki/cs215/downloads","https://www.udacity.com/wiki/cs212/downloads","https://www.udacity.com/wiki/cs313/downloads","https://www.udacity.com/wiki/cs046/downloads","https://www.udacity.com/wiki/st095/downloads","https://www.udacity.com/wiki/ps001/downloads","https://www.udacity.com/wiki/cs046/downloads"]
n = 0

while n < len(url0):
	htmlfile = urllib.urlopen(url0[n])
	str0_0 = htmlfile.read(urllib.urlopen(url0[n]))

	str0_1 = str0_0.find(r'<h2')
	str0_2 = str0_0.find(r'<div id="wiki-footer">')
	str1 = str0_0[str0_1:str0_2]
	i = 0

	href = str1.find(r'<a href="')
	title = str1.find(r'.zip">',href)

	# href0 = str1[href+9:title+4]
	# title0 = str1[href+43:title+4]

	# print href0,"\n",title0
	# url = str1[href+9:title+4]
	# print url
	url = [''] * 10000
	while href != -1 and title != -1 and i < 80:
		url[i] = str1[href+9:title+4]+'\n'
		# every single line needs a line break
		print url[i]

		href = str1.find(r'<a href="',title)
		title = str1.find(r'.zip">',href)
		x = open('test.txt','a')
		x.writelines(url[i])
		# writelines allowed to write arrays;.write() is only allowed to write str or num in files
		x.close()

		i += 1
	else:
		print "Find end!"

	n += 1
