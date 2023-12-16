import requests
class Client():
	def __init__(self):
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
		self.api='https://api.newmanga.org/v2'
		self.api_v3='https://api.newmanga.org/v3'
		self.user_id=None
	def login(self,email,password):
	    data={"credentials":email,"password":password}
	    req=requests.post(f'{self.api}/login',json=data,headers=self.headers)
	    self.headers=reg.headers
	    self.user_id=self.get_account_info()['id']
	    return req
	def friendship_request(self,user_id):
	    return requests.post(f'{self.api}/user/friendships/requests?user_id={user_id}',headers=self.headers).json()
	def register(self,login,email,password):
	    data={"login":login,"email":email,"password":password}
	    return requests.post(f'{self.api}/register',json=data,headers=self.headers)
	def forgot_password(self,credentials):
	    data={"credentials":credentials}
	    return requests.post(f'{self.api}/forgot_password',json=data,headers=self.headers)
	def get_account_info(self):
	    return requests.get(f'{self.api}/user',headers=self.headers).json()
	def slides(self):
	    return requests.get(f'{self.api}/slides',headers=self.headers).json()
	def projects_trending(self):
	    return requests.get(f'{self.api}/projects/trending',headers=self.headers).json()
	def tags(self):
	    return requests.get(f'{self.api}/tags',headers=self.headers).json()
	def user_subscriptions(self):
	    return requests.get(f'{self.api}/user/branches/subscriptions',headers=self.headers).json()
	def user_notifications(self):
	    return requests.get(f'{self.api}/user/notifications/',headers=self.headers).json()
	def user_translators(self):
	    return requests.get(f'{self.api}/user/translators',headers=self.headers).json()
	def genres(self):
	    return requests.get(f'{self.api}/user/translators',headers=self.headers).json()
	def my_statistic(self):
	    return requests.get(f'{self.api}/users/{self.user_id}/statistic',headers=self.headers).json()
	def my_badges(self):
	    return requests.get(f'{self.api}/users/{self.user_id}/badges',headers=self.headers).json()
	def my_activity(self,scope):
	    return requests.get(f'{self.api}/users/{self.user_id}/activity?scope={scope}',headers=self.headers).json()
	def projects_updates(self,only_bookmarks:bool=False,page:int=1,size:int=5):
	    return requests.get(f'{self.api}/projects/updates?only_bookmarks={only_bookmarks}&page={page}&size={size}',headers=self.headers).json()
	def projects_popular(self,size:int=5):
	    return requests.get(f'{self.api}/projects/popular?size={size}',headers=self.headers).json()
	def search(self,query,size:int=5,page:int=1):
	    return requests.get(f'{self.api}/teams/search?query={query}b&page={page}&size={size}',headers=self.headers).json()
	def edit_profile(self,site:str=None,about:str=None,gender:str=None):
	    data={}
	    if gender:data['gender']=gender
	    if about:data['about']=about
	    if site:data['site']=site
	    return requests.patch(f'{self.api}/user',json=data,headers=self.headers)
	def send_comment(self,patch,text,parent_id:int=None):
	    data={"html":text}
	    if parent_id:data['parent_id']=parent_id
	    return requests.post(f'{self.api}/projects/{patch}/comments',json=data,headers=self.headers).json()
	def get_comments(self,patch):
	    return requests.get(f'{self.api}/projects/{patch}/comments?sort_by=new',headers=self.headers).json()
	def bookmark(self,type,patch):
	    data={"type":type}
	    return requests.post(f'{self.api}/projects/{patch}/bookmark',json=data,headers=self.headers).json()
	def report(self,reason,description,patch):
	    data={"reason":reason,"description":description}
	    return requests.post(f'{self.api}/projects/{patch}/report',json=data,headers=self.headers).json()
	def heart(self,comment_id,value:bool=True):
	    data={"value":value}
	    return requests.post(f'{self.api}/chapters/{comment_id}/heart',json=data,headers=self.headers).json()
	def mark(self,comment_id,value:bool=True):
	    data={"value":value}
	    return requests.post(f'{self.api}/comments/{comment_id}/mark',json=data,headers=self.headers).json()
	def get_friendships_requests(self):
	    return requests.get(f'{self.api}/user/friendships/requests?outgoing=true',headers=self.headers).json()
	def get_team_requests(self):
	    return requests.get(f'{self.api}/user/teams/requests',headers=self.headers).json()
	def get_team_invites(self):
	    return requests.get(f'{self.api}/user/team_invites',headers=self.headers).json()
