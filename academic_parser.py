import requests
import re

request_url = 'https://dic.academic.ru/searchall.php';
term = 'Вычислительная лингвистика'

request_page = requests.post(request_url, data={'SWord':term, 'stype':0, 'p':0})

# Находим участок кода с результатами поиска
search = re.split(r'<div id="search_results">', request_page.text)
search = re.split(r'<div class="page-nav">', search[1])
search_result = search[0]


# Ищем все теги <li> ... </li>
result_links = re.findall(r'<li>.*\n', search_result)

for key in result_links:
	link_a = re.search(r'<a\s[a-zA-Z0-9].[^<>]*>.[^<>]*</a>', key)
	split_link = re.split(r'"', link_a.group(0), maxsplit=2)
	split_li = re.split(r'</strong>', key, maxsplit=1)
	
	#print('split_li = '+str(split_li))
	
	url = split_link[1]
	text = re.search(r'[а-яА-Я0-9]+', split_link[2])
	#definition = re.search(r'[а-яА-Я0-9\t\n\r.,():]*', split_li[1])
	definition = re.split(r'</p>', split_li[1], maxsplit=1)[0]
	
	print('url = ' + url)
	print('text = ' + text.group(0))
	print('definition = ' + definition)
	#print('link = ' + link_a.group(0))
	#print('key = ' + key)
	print('-------------------------------------')
	
	


#print('code = ' + str(request_page.status_code))

#f = open('academic_html.txt', 'w')
#f.write(request_page.text)
#f.close()

#print(request_page.text)
