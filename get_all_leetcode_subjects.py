import requests
import json
from bs4 import BeautifulSoup
import os
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# above is to solve the problem 'UnicodeEncodeError: 'ascii' codec can't encode character...'
# for python 2.7 is based on ascii, when character is out of ascii, it will post an error


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

# save algorithm
def save_alg(content):
	name = str(content['id'])+' '+content['title']
	f = open(name,'wb')
	f.write(content['content'])
	f.close()



#get all the algorithm list
r = requests.get(url='https://leetcode.com/api/problems/algorithms/')
#get the json data
data_json = json.loads(r.text)
#get the algorithm list
alg_list = data_json['stat_status_pairs']


if not os.path.exists('leetcode'):
    os.mkdir('leetcode')
#change directory to leetcode for convinient
os.chdir('leetcode')

for alg_json in alg_list:
	#get the meta info of algorithm
	alg_stat = alg_json['stat']
	alg_difficulty = alg_json['difficulty']['level']
	alg_paid = alg_json['paid_only']

	alg_name = alg_stat['question__title']
	alg_name_slug = alg_stat['question__title_slug'] 
	alg_id = alg_stat['question_id']
	alg_acs = alg_stat['total_acs']
	alg_submitted = alg_stat['total_submitted']

	content = get_alg_content(alg_name_slug)
	print('writing '+str(alg_id)+' '+alg_name+'...')
	alg_dict = {'id': alg_id, 'title':alg_name,'difficulty':alg_difficulty,'content':content}

	save_alg(alg_dict)
	print('Done!')

r.close()












