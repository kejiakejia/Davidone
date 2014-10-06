import urllib
import re
#encoding:cp936

# 代购
url = ['']*40
str = urllib.urlopen("http://v.163.com/special/opencourse/bianchengdaolun.html").read()

title = str.find(r'<td class="u-ctitle"')
href = str.find(r'.html">',title)



i = 0
while title != -1 and href != -1 and i < 35:
	url[i] = str[title+25:href+5]
	c = url[i].replace('"','')
	d = c.replace('<a','')
	e = d.replace(' ','')
	print unicode(e, "cp936")

	title = str.find(r'<td class="u-ctitle"',href)
	href = str.find(r'.html">',title)


	i += 1