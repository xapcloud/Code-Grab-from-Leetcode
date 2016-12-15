import requests
import json
from bs4 import BeautifulSoup
import os
import re
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')
# above is to solve the problem 'UnicodeEncodeError: 'ascii' codec can't encode character...'
# for python 2.7 is based on ascii, when character is out of ascii, it will post an error

s = requests.Session()
headers_base = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
	'Connection':'keep-alive',
	'Host': 'leetcode.com',
	'Referer':'https://leetcode.com/accounts/login/',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
	}	


def login():
	url = "https://leetcode.com/accounts/login/"
	res = s.get(url=url,headers=headers_base)
	#get csrftoken from cookie
	print res.cookies['csrftoken']

	login_data={}
	login_data['csrfmiddlewaretoken']=res.cookies['csrftoken']
	login_data['login'] = "xapcloud"
	login_data['password'] = "911223"
	login_data['remember'] ='on'
	res = s.post(url,headers = headers_base,data=login_data)
	print res.status_code
	return res.cookies

def get_bs(url):
	try:
		 page = s.get(url)
	except (requests.exceptions.ReadTimeout,requests.exceptions.ConnectTimeout):
        	print('time out')
        	return 'time out'
	bs = BeautifulSoup(page.text, "html.parser")
	return bs   	

#get the ac solution url
def get_ac_url(alg_name_slug):
	url = 'https://leetcode.com/problems/'+alg_name_slug+'/submissions/'
	bs = get_bs(url)

	ac_solutions = bs.find_all("a","text-danger status-accepted")#get all ac solution
	return 'https://leetcode.com'+ ac_solutions[0]["href"]#choose the first one

def get_ac_code(url):
	bs = get_bs(url)
	ac_code = bs.find_all('script')
	final_code = txt_wrap_by('submissionCode:','editCodeUrl:',ac_code[11].text)
	final_code = re.sub('/\\*.*\\*/','',final_code)#remove annotation to prevent chinese
	return final_code.decode('unicode-escape')


#get the algorithm content by name
def get_alg_content(name):
	url = 'https://leetcode.com/problems/' + name
	try:
		 page = requests.get(url)
	except (requests.exceptions.ReadTimeout,requests.exceptions.ConnectTimeout):
        	print('time out')
        	return 'time out'
	alg_page = BeautifulSoup(page.text, "html.parser")
	alg_contents = alg_page.select('.question-content')

	alg_text = ''
	#for some special case(such as subscribe needed), 
	#the alg_contents' length will be 0
	if len(alg_contents) > 0:
		contents = alg_contents[0].find_all(['p','pre'])

		for ctt in contents:
			alg_text += ctt.get_text()

	page.close
	return alg_text

#get the code from the js code by fetch 
#content between submissionCode: &  editCodeUrl:	
def txt_wrap_by(start_str, end, html):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start+2:end-5].strip()

def save_all(content):
	name = str(content['id'])+'_'+content['name']+'.md'
	f = open(name,'wb')
	f.write('###'+str(content['id'])+' '+content['title']+'\n')
	f.write(content['subject']+'\n')
	f.write('###Solution'+'\n')
	f.write('```java'+'\n')
	f.write(content['code'])
	f.close()	

if not os.path.exists('leetcode_with_solution'):
    os.mkdir('leetcode_with_solution')
#change directory to leetcode for convinient
os.chdir('leetcode_with_solution')	

#login and get the login data
login()
#print(mycookie['csrftoken'])

r = s.get(url='https://leetcode.com/api/problems/algorithms/')
#get the json data
data_json = json.loads(r.text)
#get the algorithm list
alg_list = data_json['stat_status_pairs']

for alg_json in alg_list:
	if alg_json['status'] == 'ac':
		#get the meta info of algorithms
		alg_stat = alg_json['stat']
		alg_difficulty = alg_json['difficulty']['level']
		alg_paid = alg_json['paid_only']

		alg_name = alg_stat['question__title']
		alg_name_slug = alg_stat['question__title_slug'] 
		alg_id = alg_stat['question_id']
		alg_acs = alg_stat['total_acs']
		alg_submitted = alg_stat['total_submitted']

		print('writing '+str(alg_id)+' '+alg_name+'...')
		url = get_ac_url(alg_name_slug)
		code = get_ac_code(url)
		subject = get_alg_content(alg_name_slug)
		content = {'id': alg_id, 'title':alg_name,'name':alg_name_slug,'difficulty':alg_difficulty,'subject':subject,'code':code}

		save_all(content)

		print('Done!')
		#time.sleep(1)










